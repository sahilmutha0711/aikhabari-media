import subprocess,os
from PIL import Image
D='/home/claude/reels/outage';os.makedirs(f'{D}/bseg',exist_ok=True)
V={'b3':'/home/claude/reels/wallet/broll/b3.mp4','b5':'/home/claude/reels/wallet/broll/b5.mp4','b7':'/home/claude/reels/wallet/broll/b7.mp4','dusk':'/home/claude/reels/vc/img/dusk.mp4','sf':'/home/claude/reels/vc/img/sf.mp4'}
P=[(0,9.75,'black',0),(9.75,11.4,'b5',0),(11.4,16.5,'msft',0),(16.5,23.0,'b3',0),(23.0,25.2,'b7',1),(25.2,29.5,'yyz2',0),(29.5,32.1,'tower',0),
(32.1,36.6,'router',0),(36.6,40.9,'chase',0),(40.9,48.2,'apple',0),(48.2,50.6,'black',0),(50.6,52.6,'dusk',0),(52.6,56.0,'b7',3),(56.0,59.4,'sf',1),(59.4,63.5,'yale',0),(63.5,69.2,'black',0)]
AN={'chase':0.45,'apple':0.5,'yyz2':0.35,'router':0.4}
L=[]
for i,(a,b,k,o) in enumerate(P):
    Dd=round(b-a,3);out=f'{D}/bseg/{i:02d}.mp4';n=round(b*30)-round(a*30)
    if k=='black': inp=['-f','lavfi','-i','color=black:s=1080x1920:r=30'];vf='null'
    elif k in V:
        inp=['-ss',str(o),'-stream_loop','-1','-i',V[k]];vf=f"scale=w='1080*(1.06+0.08*t/{Dd})':h=-2:eval=frame,crop=1080:1920:(iw-1080)/2+20*sin(t*0.9):(ih-1920)/2"
    else:
        w,h=Image.open(f'{D}/img/{k}.jpg').size;s=max(1080/w,1920/h)*1.04;an=AN.get(k,0.5);d=1 if i%2 else -1
        inp=['-loop','1','-framerate','30','-i',f'{D}/img/{k}.jpg']
        vf=(f"scale=w='{w*s:.1f}*(1+0.10*t/{Dd})':h=-2:eval=frame,crop=1080:1920:'(iw-1080)*({an}+{d}*0.15*(t/{Dd}-0.5))':'(ih-1920)/2'")
    subprocess.run(['ffmpeg','-nostdin','-y','-v','error',*inp,'-vf',vf+',fps=30,format=yuv420p','-frames:v',str(n),'-an','-c:v','libx264','-crf','16','-preset','fast',out],check=True)
    L.append(f"file '{out}'")
open(f'{D}/blist.txt','w').write('\n'.join(L))
subprocess.run(['ffmpeg','-nostdin','-y','-v','error','-f','concat','-safe','0','-i',f'{D}/blist.txt','-c','copy',f'{D}/broll_track.mp4'],check=True)
