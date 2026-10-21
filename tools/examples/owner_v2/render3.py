import json,sys,subprocess,os
from playwright.sync_api import sync_playwright
R='/home/claude/reels/agi_owner';var=sys.argv[1];args=sys.argv[2:];FPS=30;TOTAL=87.6;n=int(TOTAL*FPS)
d=json.load(open(f'{R}/work/words_full.json'));Wd=d['words']
h=open(f'{R}/tpl3.html').read()
for k,v in {'__WORDS__':json.dumps(Wd),'__TOTAL__':str(TOTAL),'__DIR__':'file://'+R,'__MODE__':'split'}.items():h=h.replace(k,v)
open(f'{R}/reel3_{var}.html','w').write(h)
WIN=[(9.8,12.45),(24.0,31.75),(54.4,63.75),(65.4,71.35)];EN='+'.join(f'between(t,{a},{b})' for a,b in WIN)
PW,PH=637,920;PX=50+(980-PW)//2;PY=965
def fc():
    head=f"color=c=black:s=1080x1920:r=30:d={TOTAL}[bg];[0:v]crop=1080:1560:0:360,split=2[c1][c2];"
    if var=='blur':
        panel=(f"[c1]scale=980:1415,crop=980:920:0:200,boxblur=28:2,eq=brightness=-0.12:saturation=0.9[pb];[c2]scale={PW}:{PH},eq=contrast=1.04:saturation=1.06[pf];"
               f"[bg][pb]overlay=50:{PY}[b0];[b0][pf]overlay={PX}:{PY}[b1];")
    else:
        panel=(f"[c1]scale={PW}:{PH},eq=contrast=1.05:saturation=1.07:brightness=0.02[pf];[3:v]scale={PW}:{PH},format=gray,geq=lum='lum(X,Y)*min(1,min(X,W-1-X)/26)'[pm];[pf][pm]alphamerge[pa];[c2]nullsink;"
               f"[bg][4:v]overlay=50:{PY}[b0];[b0][pa]overlay={PX}:{PY}[b1];")
    return head+panel+f"[b1][1:v]overlay=50:160:enable='{EN}'[b2];[b2][2:v]overlay=0:0:format=auto,format=yuv420p[v]"
def cmd(out):
    c=['ffmpeg','-y','-loglevel','error','-i',f'{R}/work/proxy.mp4','-i',f'{R}/work/cliptrack680.mp4','-f','image2pipe','-framerate',str(FPS),'-c:v','png','-i','-']
    if var=='studio': c+=['-i',f'{R}/work/mask.mp4','-loop','1','-framerate','30','-i',f'{R}/bg/studio.png']
    return c+['-filter_complex',fc(),'-map','[v]','-c:v','libx264','-preset','medium','-crf','19','-t',str(TOTAL),'-r','30',out]
with sync_playwright() as p:
    b=p.chromium.launch(args=['--allow-file-access-from-files']);pg=b.new_page(viewport={'width':1080,'height':1920})
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)));pg.goto(f'file://{R}/reel3_{var}.html');pg.wait_for_timeout(900)
    if args:
        from PIL import Image,ImageDraw,ImageFilter
        ts=list(map(float,args));ims=[]
        for t in ts:
            subprocess.run(['ffmpeg','-y','-loglevel','error','-ss',str(t),'-i',f'{R}/work/proxy.mp4','-frames:v','1','-vf','crop=1080:1560:0:360',f'{R}/prev/me.png'])
            subprocess.run(['ffmpeg','-y','-loglevel','error','-ss',str(t),'-i',f'{R}/work/cliptrack680.mp4','-frames:v','1',f'{R}/prev/cl.png'])
            pg.evaluate(f'setT({t})');pg.screenshot(path=f'{R}/prev/f.png',omit_background=True)
            me=Image.open(f'{R}/prev/me.png').convert('RGB');bg=Image.new('RGBA',(1080,1920),'black')
            pb=me.resize((980,1415)).crop((0,200,980,1120)).filter(ImageFilter.GaussianBlur(14));bg.paste(pb,(50,PY))
            bg.paste(me.resize((PW,PH)),(PX,PY))
            if any(a<=t<=b2 for a,b2 in WIN): bg.paste(Image.open(f'{R}/prev/cl.png').convert('RGBA'),(50,160))
            bg.alpha_composite(Image.open(f'{R}/prev/f.png').convert('RGBA'))
            ims.append(bg.convert('RGB').resize((270,480)))
        M=Image.new('RGB',(7*270,((len(ims)+6)//7)*500))
        for i,(im,t) in enumerate(zip(ims,ts)):M.paste(im,((i%7)*270,(i//7)*500));ImageDraw.Draw(M).text(((i%7)*270+5,(i//7)*500+482),str(t),fill=(255,255,0))
        M.save(f'{R}/prev/sheet3.png');print('errors',errs);sys.exit()
    ff=subprocess.Popen(cmd(f'{R}/work/video3_{var}.mp4'),stdin=subprocess.PIPE)
    for i in range(n):
        pg.evaluate(f'setT({i/FPS})');ff.stdin.write(pg.screenshot(type='png',omit_background=True))
    ff.stdin.close();ff.wait();print('done',TOTAL,'errors',errs)
