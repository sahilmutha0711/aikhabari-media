import numpy as np,subprocess,sys
sys.path.insert(0,'work');from seg import mask
from PIL import Image
W,H=1080,1560;N=2629
rd=subprocess.Popen(['ffmpeg','-loglevel','error','-i','work/proxy.mp4','-vf','crop=1080:1560:0:360,scale=320:320:flags=bilinear','-f','rawvideo','-pix_fmt','rgb24','-'],stdout=subprocess.PIPE)
wr=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','rawvideo','-pix_fmt','gray','-s','540x780','-r','30','-i','-','-c:v','libx264','-crf','12','-pix_fmt','yuv420p','work/mask.mp4'],stdin=subprocess.PIPE)
prev=None;pend=False;i=0
def out(m):
    a=(np.asarray(Image.fromarray((np.clip(m,0,1)*255).astype(np.uint8)).resize((540,780),Image.BILINEAR))).astype(np.uint8)
    wr.stdin.write(a.tobytes())
while True:
    b=rd.stdout.read(320*320*3)
    if len(b)<320*320*3: break
    if i%2==0:
        m=mask(Image.frombytes('RGB',(320,320),b))
        if pend: out((prev+m)/2)
        out(m);prev=m;pend=False
    else: pend=True
    i+=1
    if i%300==0: print(i,flush=True)
if pend: out(prev)
wr.stdin.close();wr.wait();print('done',i,flush=True)
