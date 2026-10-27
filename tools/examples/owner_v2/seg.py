import sys,numpy as np,onnxruntime as ort,subprocess,os
from PIL import Image,ImageFilter
so=ort.SessionOptions();so.intra_op_num_threads=2
S=ort.InferenceSession('/home/claude/models/u2net_human_seg.onnx',so);IN=S.get_inputs()[0].name
def mask(im):
    x=np.asarray(im.resize((320,320),Image.BILINEAR),np.float32)/255.
    x=(x-[.485,.456,.406])/[.229,.224,.225];x=x.transpose(2,0,1)[None].astype(np.float32)
    m=S.run(None,{IN:x})[0][0,0];m=(m-m.min())/(m.max()-m.min()+1e-6)
    return m
if __name__=='__main__':
    for t in sys.argv[1:]:
        subprocess.run(['ffmpeg','-y','-loglevel','error','-ss',t,'-i','work/proxy.mp4','-frames:v','1','-vf','crop=1080:1560:0:360','prev/s.png'])
        im=Image.open('prev/s.png').convert('RGB');m=mask(im)
        a=Image.fromarray((m*255).astype(np.uint8)).resize(im.size,Image.BILINEAR).filter(ImageFilter.GaussianBlur(2))
        bg=Image.new('RGB',im.size,(0,82,92));bg.paste(im,(0,0),a);bg.resize((360,520)).save(f'prev/seg_{t}.png')
