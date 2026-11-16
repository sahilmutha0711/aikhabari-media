import subprocess
from PIL import Image
D='/home/claude/reels/vc'
P=[(0,13.3,'black',0),(13.3,15.25,'a16z_bldg',0),(15.25,18.2,'marc',0),(18.2,21.35,'sf',0),(21.35,25.0,'ben',0),
(25.0,28.95,'dusk',0),(28.95,32.6,'sandhill',0),(32.6,35.1,'coffee2',0),(35.1,36.9,'tc1',0),(36.9,38.5,'coffee1',0),(38.5,41.4,'tc2',0),
(41.4,44.2,'lean',0),(44.2,49.25,'dusk',3),(49.25,52.6,'b3',1),(52.6,56.6,'coffee1',0),(56.6,64.0,'black',0)]
AN={'a16z_bldg':0.2,'ben':0.75,'coffee1':0.3}
L=[]
for i,(a,b,k,o) in enumerate(P):
    Dd=round(b-a,3);out=f'{D}/seg2/{i:02d}.mp4';n=round(b*30)-round(a*30)
    if k=='black': inp=['-f','lavfi','-i','color=black:s=1080x1920:r=30'];vf='null'
    elif k in('sf','dusk','b3'):
        src=f'{D}/img/{k}.mp4' if k!='b3' else '/home/claude/reels/wallet/broll/b3.mp4'
        inp=['-ss',str(o),'-i',src];vf=f"scale=w='1080*(1.06+0.08*t/{Dd})':h=-2:eval=frame,crop=1080:1920:(iw-1080)/2+20*sin(t*0.9):(ih-1920)/2"
    else:
        w,h=Image.open(f'{D}/img/{k}.jpg').size;s=max(1080/w,1920/h)*1.04;an=AN.get(k,0.5);d=1 if i%2 else -1
        inp=['-loop','1','-framerate','30','-i',f'{D}/img/{k}.jpg']
        vf=(f"scale=w='{w*s:.1f}*(1+0.10*t/{Dd})':h=-2:eval=frame,crop=1080:1920:'(iw-1080)*({an}+{d}*0.15*(t/{Dd}-0.5))':'(ih-1920)/2'")
    subprocess.run(['ffmpeg','-nostdin','-y','-v','error',*inp,'-vf',vf+',fps=30,format=yuv420p','-frames:v',str(n),'-an','-c:v','libx264','-crf','16','-preset','fast',out],check=True)
    L.append(f"file '{out}'")
open(f'{D}/blist2.txt','w').write('\n'.join(L))
subprocess.run(['ffmpeg','-nostdin','-y','-v','error','-f','concat','-safe','0','-i',f'{D}/blist2.txt','-c','copy',f'{D}/broll_track.mp4'],check=True)
