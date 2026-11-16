import subprocess
from PIL import Image
D='/home/claude/reels/vc';FW,FH,X,Y=900,980,90,470
P=[(0,13.3,'black',0,None),(13.3,15.25,'a16z_bldg',0,'arch'),(15.25,18.2,'marc',0,'slant'),(18.2,21.35,'sf',0,'hex'),(21.35,25.0,'ben',0,'ticket'),
(25.0,28.95,'dusk',0,'arch'),(28.95,35.1,'sandhill',0,'slant'),(35.1,36.9,'tc1',0,'hex'),(36.9,38.5,'coffee2',0,'ticket'),(38.5,41.4,'tc2',0,'arch'),
(41.4,44.2,'lean',0,'slant'),(44.2,49.25,'dusk',3,'hex'),(49.25,52.6,'b3',1,'ticket'),(52.6,56.6,'coffee1',0,'arch'),(56.6,64.0,'black',0,None)]
L=[];AN={'a16z_bldg':0.15,'ben':0.7}
for i,(a,b,k,o,sh) in enumerate(P):
    Dd=round(b-a,3);n=round(b*30)-round(a*30);out=f'{D}/seg/{i:02d}.mp4'
    if k=='black':
        cmd=['-f','lavfi','-i','color=black:s=1080x1920:r=30','-vf','format=yuv420p']
    else:
        if k in('sf','dusk','b3'):
            src=f'{D}/img/{k}.mp4' if k!='b3' else '/home/claude/reels/wallet/broll/b3.mp4'
            inp=['-ss',str(o),'-i',src];w,h=1080,1920
        else:
            src=f'{D}/img/{k}.jpg';w,h=Image.open(src).size;inp=['-loop','1','-framerate','30','-i',src]
        sb=max(1080/w,1920/h);sf=max(FW/w,FH/h)*1.02
        fc=(f"[0:v]fps=30,split[a][b];[a]scale={w*sb:.0f}:{h*sb:.0f},crop=1080:1920,boxblur=28:2,eq=brightness=-0.22:saturation=0.8[bg];"
            f"[b]scale=w='{w*sf:.1f}*(1+0.09*t/{Dd})':h=-2:eval=frame,crop={FW}:{FH}:'(iw-{FW})*({AN.get(k,0.5)}+0.2*(t/{Dd}-0.5))':'(ih-{FH})/2',format=rgba[fg0];"
            f"[1:v]format=gray,scale={FW}:{FH}[m];[fg0][m]alphamerge[fg];[bg][fg]overlay={X}:{Y},format=yuv420p")
        cmd=[*inp,'-loop','1','-i',f'{D}/masks/{sh}.png','-filter_complex',fc]
    subprocess.run(['ffmpeg','-nostdin','-y','-v','error',*cmd,'-frames:v',str(n),'-r','30','-an','-c:v','libx264','-crf','16','-preset','fast',out],check=True)
    L.append(f"file '{out}'")
open(f'{D}/blist.txt','w').write('\n'.join(L))
subprocess.run(['ffmpeg','-nostdin','-y','-v','error','-f','concat','-safe','0','-i',f'{D}/blist.txt','-c','copy',f'{D}/broll_track.mp4'],check=True)
