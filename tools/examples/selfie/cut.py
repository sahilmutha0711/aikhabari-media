import wave,numpy as np,json
w=wave.open('audio48.wav');sr=w.getframerate();a=np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(np.float32)/32768
db=np.load('work/db.npy')  # 10ms frames
W=json.load(open('work/words.json'))
EDL=[(4.05,7.2),(10.75,13.55),(14.35,18.85),(21.3,22.1),(30.7,31.3),(32.6,34.98),(36.2,40.65),(45.82,50.2),
     (52.9,56.15),(56.38,59.6),(59.82,61.3),(62.12,65.3),(66.05,68.68),(70.68,72.62),(73.26,74.26),(74.9,78.85),(79.9,85.65),
     (100.6,109.1),(110.0,114.5),(115.65,119.55),(121.18,121.9)]
THR=-38.0;MAXGAP=0.12
STRICT_S={(21.3,22.1),(30.7,31.3),(59.82,61.3),(70.68,72.62),(73.26,74.26),(56.38,59.6)}
STRICT_E={(56.38,59.6),(14.35,18.85)}
def quiet(i,n=10,t=-40): return (db[i:i+n]<t).all()
def fwd(e):
    i=int(e*100)
    for k in range(i,i+60):
        if quiet(k): return k/100+0.04
    return e+0.3
def back(s):
    i=int(s*100)
    for k in range(i,i-40,-1):
        if quiet(k-10): return k/100-0.04
    return s-0.1
def snap(t,lo,hi):
    i0,i1=int((t+lo)*100),int((t+hi)*100);k=i0+int(np.argmin(db[i0:i1+1]));return k/100
pieces=[]
for s,e in EDL:
    s0=s
    if (s,e) in STRICT_S: s=snap(s,-0.04,0.04)
    else: s=back(s)
    if (s0,e) in STRICT_E: e=snap(e,-0.03,0.05)
    else: e=fwd(e)
    # split by long silences
    i0,i1=int(s*100),int(e*100);q=db[i0:i1]<THR;cur=s;k=0
    while k<len(q):
        if q[k]:
            j=k
            while j<len(q) and q[j]: j+=1
            L=(j-k)/100
            if L>0.28:
                gs=(i0+k)/100;ge=(i0+j)/100
                if gs>cur: pieces.append((cur,gs+MAXGAP/2))
                cur=ge-MAXGAP/2
            k=j
        else: k+=1
    if e>cur: pieces.append((cur,e))
pieces=[(round(x*60)/60,round(y*60)/60) for x,y in pieces if y-x>0.05]
# build audio with 8ms fades
out=[];fade=int(0.008*sr);tl=[];T=0
for s,e in pieces:
    seg=a[int(s*sr):int(e*sr)].copy();r=np.linspace(0,1,fade);seg[:fade]*=r;seg[-fade:]*=r[::-1]
    out.append(seg);tl.append((s,e,T));T+=e-s
y=np.concatenate(out);ww=wave.open('work/cut48.wav','w');ww.setnchannels(1);ww.setsampwidth(2);ww.setframerate(sr);ww.writeframes((np.clip(y,-1,1)*32767).astype(np.int16).tobytes());ww.close()
json.dump({'pieces':pieces,'tl':tl},open('work/pieces.json','w'))
print('pieces',len(pieces),'duration',round(T,2))
