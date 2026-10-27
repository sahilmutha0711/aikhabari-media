import numpy as np,subprocess,math
W,H,FPS,T=270,480,30,28.0;n=int(T*FPS)
y,x=np.mgrid[0:H,0:W].astype(np.float32)
base=np.array([6,8,24],np.float32)
blobs=[((40,40,120),.7),((20,60,110),.6),((70,30,110),.6),((30,30,90),.6)]
p=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','-','-vf','scale=1080:1920:flags=bicubic,noise=alls=7:allf=t,format=yuv420p','-c:v','libx264','-crf','20','-preset','fast','meshbg2.mp4'],stdin=subprocess.PIPE)
for i in range(n):
    t=i/FPS;img=np.tile(base,(H,W,1))
    pos=[(0.15+0.12*math.sin(t*.35),0.12+0.08*math.cos(t*.3)),(0.85+0.1*math.cos(t*.28),0.42+0.1*math.sin(t*.33)),(0.2+0.12*math.sin(t*.25+1),0.88+0.06*math.cos(t*.4)),(0.75+0.1*math.sin(t*.3+2),0.95+0.05*math.sin(t*.2))]
    for (c,a),(px,py) in zip(blobs,pos):
        d=((x-px*W)**2+(y-py*H)**2)/(2*(0.32*W)**2)
        g=(np.exp(-d)*a)[...,None]
        img=img*(1-g)+np.array(c,np.float32)*g
    p.stdin.write(np.clip(img,0,255).astype(np.uint8).tobytes())
p.stdin.close();p.wait()
