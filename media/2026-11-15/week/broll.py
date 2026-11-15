import subprocess
from PIL import Image
I='/home/claude/aikhabari-media/media/2026-11-15/week/img/';B='/home/claude/reels/wallet/broll/';D='/home/claude/reels/week'
P=[(0,7.30,'black',0),(7.30,9.88,'nvda_hq',0),(9.88,11.90,'jensen',0),(11.90,14.80,'nasdaq',0),(14.80,16.15,'nvda_sign',0),
(16.15,16.95,'amd',0),(16.95,17.50,'avgo',0),(17.50,18.02,'mu',0),(18.02,19.55,'tsmc',0),(19.55,20.75,'b5',0.5),(20.75,22.05,'b7',2),
(22.05,24.40,'nasdaq2',0),(24.40,26.35,'amzn',0),(26.35,29.05,'googl',0),(29.05,42.6,'black',0)]
L=[]
for i,(a,b,k,o) in enumerate(P):
    D_=round(b-a,3);out=f'{D}/bseg/{i:02d}.mp4';n=round(b*30)-round(a*30)
    if k=='black': inp=['-f','lavfi','-i','color=black:s=1080x1920:r=30'];vf='null'
    elif k.startswith('b'): inp=['-ss',str(o),'-i',B+k+'.mp4'];vf=f"scale=w='1080*(1.06+0.08*t/{D_})':h=-2:eval=frame,crop=1080:1920:(iw-1080)/2+20*sin(t*0.9):(ih-1920)/2"
    else:
        w,h=Image.open(I+k+'.jpg').size;s=max(1080/w,1920/h)*1.04
        inp=['-loop','1','-framerate','30','-i',I+k+'.jpg']
        d=1 if i%2 else -1
        vf=(f"scale=w='{w*s:.1f}*(1+0.10*t/{D_})':h=-2:eval=frame,"
            f"crop=1080:1920:'(iw-1080)*(0.5+{d}*0.25*(t/{D_}-0.5))':'(ih-1920)/2'")
    subprocess.run(['ffmpeg','-nostdin','-y','-v','error',*inp,'-vf',vf+',fps=30,format=yuv420p','-frames:v',str(n),'-an','-c:v','libx264','-crf','16','-preset','fast',out],check=True)
    L.append(f"file '{out}'")
open(f'{D}/blist.txt','w').write('\n'.join(L))
subprocess.run(['ffmpeg','-nostdin','-y','-v','error','-f','concat','-safe','0','-i',f'{D}/blist.txt','-c','copy',f'{D}/broll_track.mp4'],check=True)
