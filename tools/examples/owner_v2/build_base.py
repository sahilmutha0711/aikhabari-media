import json,sys,wave,numpy as np,subprocess
mode=sys.argv[1]
d=json.load(open(f'work/edit_{mode}.json'));P=d['pieces'];words=d['words']
w=wave.open('work/clean48.wav');sr=w.getframerate();a=np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(np.float32)/32768
fade=int(0.012*sr);out=[]
for s,e in P:
    seg=a[int(s*sr):int(e*sr)].copy();r=np.linspace(0,1,fade);seg[:fade]*=r;seg[-fade:]*=r[::-1];out.append(seg)
y=np.concatenate(out);ww=wave.open(f'work/voice_{mode}.wav','w');ww.setnchannels(1);ww.setsampwidth(2);ww.setframerate(sr);ww.writeframes((np.clip(y,-1,1)*32767).astype(np.int16).tobytes());ww.close()
# zoom segments by output time: change zoom at each new segment label start
segs=[];last=None
for x in words:
    if x['seg'].rstrip('0123456789')!=last:
        segs.append(x['s']);last=x['seg'].rstrip('0123456789')
# also add zoom flip at each piece boundary (jump cut)
T=0;bounds=[]
for s,e in P: bounds.append(T);T+=e-s
cuts=sorted(set([round(b,3) for b in bounds]+[round(s,3) for s in segs]))
cuts=[c for c in cuts]+[T]
zs=[];z=1.0
for i in range(len(cuts)-1):
    t0,t1=cuts[i],cuts[i+1]
    if t1-t0<0.4 and zs: zs[-1]=(zs[-1][0],t1,zs[-1][2]);continue
    z=1.12 if (len(zs)%2==1) else 1.0
    zs.append((t0,t1,z))
expr='1'
for t0,t1,z in reversed(zs):
    expr=f"if(between(t,{t0:.3f},{t1:.3f}),{z}+0.02*(t-{t0:.3f})/({t1-t0:.3f}),{expr})"
sel='+'.join(f"between(t,{s-0.005:.4f},{e-0.005:.4f})" for s,e in P)
vf=f"select='{sel}',setpts=N/30/TB,scale=w='trunc(1080*({expr})/2)*2':h='trunc(1920*({expr})/2)*2':eval=frame:flags=bicubic,crop=1080:1920:(iw-1080)/2:(ih-1920)*0.32,eq=contrast=1.05:saturation=1.08:brightness=0.01,format=yuv420p"
open(f'work/vf_{mode}.txt','w').write(vf)
r=subprocess.run(['ffmpeg','-y','-loglevel','error','-i','work/proxy.mp4','-filter_script:v',f'work/vf_{mode}.txt','-an','-r','30','-c:v','libx264','-preset','fast','-crf','17',f'work/base_{mode}.mp4'])
print(mode,'audio',round(len(y)/sr,2),'zoom segs',len(zs),'ret',r.returncode)
