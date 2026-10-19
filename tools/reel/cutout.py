import sys,numpy as np,onnxruntime as ort
from PIL import Image,ImageFilter
src,dst=sys.argv[1],sys.argv[2]
im=Image.open(src).convert('RGB');s=ort.InferenceSession('/home/claude/models/u2net.onnx')
x=np.asarray(im.resize((320,320),Image.LANCZOS),np.float32)/255.
x=(x-[.485,.456,.406])/[.229,.224,.225];x=x.transpose(2,0,1)[None].astype(np.float32)
m=s.run(None,{s.get_inputs()[0].name:x})[0][0,0];m=(m-m.min())/(m.max()-m.min())
a=Image.fromarray((m*255).astype(np.uint8)).resize(im.size,Image.LANCZOS).filter(ImageFilter.GaussianBlur(1))
a=a.point(lambda v:0 if v<40 else min(255,int((v-40)*1.4)))
o=im.convert('RGBA');o.putalpha(a);o=o.crop(o.getbbox());o.save(dst)
