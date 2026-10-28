import numpy as np,subprocess,math,sys
V=sys.argv[1];W,H,FPS,T=270,480,30,78.5;n=int(T*FPS)
y,x=np.mgrid[0:H,0:W].astype(np.float32)
if V=='noir':
    base=np.array([6,6,8],np.float32);blobs=[((70,58,40),.75),((40,40,48),.9),((150,118,70),.45),((28,28,34),.8)]
else:
    base=np.array([2,17,14],np.float32);blobs=[((10,130,96),.7),((8,82,92),.85),((40,190,140),.35),((5,50,40),.9)]
p=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','-','-vf','scale=1080:1920:flags=bicubic,noise=alls=6:allf=t,format=yuv420p','-c:v','libx264','-crf','18','-preset','fast',f'mesh_{V}.mp4'],stdin=subprocess.PIPE)
for i in range(n):
    t=i/FPS;img=np.tile(base,(H,W,1))
    pos=[(0.15+0.12*math.sin(t*.35),0.10+0.08*math.cos(t*.3)),(0.85+0.1*math.cos(t*.28),0.45+0.1*math.sin(t*.33)),(0.25+0.12*math.sin(t*.25+1),0.85+0.06*math.cos(t*.4)),(0.7+0.1*math.sin(t*.3+2),0.2+0.05*math.sin(t*.2))]
    for (c,a),(px,py) in zip(blobs,pos):
        d=((x-px*W)**2+(y-py*H)**2)/(2*(0.30*W)**2)
        g=(np.exp(-d)*a)[...,None];img=img*(1-g)+np.array(c,np.float32)*g
    p.stdin.write(np.clip(img,0,255).astype(np.uint8).tobytes())
p.stdin.close();p.wait()
