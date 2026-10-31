import cv2,numpy as np,subprocess,sys
import mediapipe as mp
from mediapipe.tasks import python as mpt
from mediapipe.tasks.python import vision
from PIL import Image,ImageDraw,ImageFont
SRC='/mnt/user-data/uploads/1793476144811624.mov'
M='/home/claude/aikhabari-media/tools/vendor/claude-video-effects/models/selfie_segmenter.tflite'
seg=vision.ImageSegmenter.create_from_options(vision.ImageSegmenterOptions(base_options=mpt.BaseOptions(model_asset_path=M),running_mode=vision.RunningMode.IMAGE,output_confidence_masks=True))
F='/mnt/skills/examples/canvas-design/canvas-fonts/BricolageGrotesque-Bold.ttf'
def make(name,t0,t1,word,col,size,y):
    dur=t1-t0;n=int(dur*30)
    raw=subprocess.run(['ffmpeg','-v','error','-ss',str(t0),'-t',str(dur),'-i',SRC,'-vf','scale=540:960,fps=30,format=rgb24','-f','rawvideo','-'],capture_output=True).stdout
    frames=np.frombuffer(raw,np.uint8).reshape(-1,960,540,3)
    font=ImageFont.truetype(F,size)
    out=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgba','-s','1080x1920','-r','30','-i','-','-c:v','png','-pix_fmt','rgba',f'{name}.mov'],stdin=subprocess.PIPE)
    for i,fr in enumerate(frames[:n]):
        t=i/30
        r=seg.segment(mp.Image(image_format=mp.ImageFormat.SRGB,data=np.ascontiguousarray(fr)))
        m=r.confidence_masks[0].numpy_view().copy()
        if m.mean()<0.2 and len(r.confidence_masks)>1: m=1-r.confidence_masks[0].numpy_view()
        m=cv2.GaussianBlur(cv2.resize(m,(1080,1920)),(9,9),0)
        img=Image.new('RGBA',(1080,1920),(0,0,0,0));d=ImageDraw.Draw(img)
        p=min(1,t/0.35);sc=1.25-0.25*(1-(1-p)**3)
        f2=ImageFont.truetype(F,int(size*sc))
        while d.textlength(word,font=f2)>1040: size=int(size*0.95); f2=ImageFont.truetype(F,int(size*sc))
        w=d.textlength(word,font=f2);d.text(((1080-w)/2,y-int(size*sc)/2),word,font=f2,fill=col+(int(255*min(1,t/0.2)),))
        a=np.array(img).astype(np.float32);a[...,3]*= (1-np.clip(m,0,1))
        out.stdin.write(a.astype(np.uint8).tobytes())
    out.stdin.close();out.wait();print(name,len(frames))
make('bd_illegal',12.6,14.05,'ILLEGAL',(58,24,18),330,330)
make('bd_redflag',66.6,68.75,'RED FLAG',(214,58,84),300,330)
