import json,sys,subprocess,os
from playwright.sync_api import sync_playwright
R='/home/claude/reels/agi_owner';mode=sys.argv[1];args=sys.argv[2:];FPS=30
d=json.load(open(f'{R}/work/words_full.json'));Wd=d['words'];TOTAL=87.6;n=int(TOTAL*FPS)
h=open(f'{R}/tpl2.html').read()
for k,v in {'__WORDS__':json.dumps(Wd),'__TOTAL__':str(TOTAL),'__DIR__':'file://'+R,'__MODE__':mode}.items():h=h.replace(k,v)
open(f'{R}/reel2_{mode}.html','w').write(h)
BOX=(50,180) if mode=='split' else (50,300)
WIN=[(9.8,12.45),(24.0,31.75),(54.4,63.75),(65.4,71.35)]
EN='+'.join(f'between(t,{a},{b})' for a,b in WIN)
def compose_cmd(out):
    if mode=='split':
        fc=(f"color=c=black:s=1080x1920:r=30:d={TOTAL}[bg];[0:v]crop=1080:805:0:430,scale=980:730,eq=contrast=1.04:saturation=1.06[me];[bg][me]overlay=50:1120[b1];"
            f"[b1][1:v]overlay={BOX[0]}:{BOX[1]}:enable='{EN}'[b2];[b2][2:v]overlay=0:0:format=auto,format=yuv420p[v]")
    else:
        fc=(f"[0:v]eq=contrast=1.04:saturation=1.06[me];[me][1:v]overlay={BOX[0]}:{BOX[1]}:enable='{EN}'[b2];[b2][2:v]overlay=0:0:format=auto,format=yuv420p[v]")
    return ['ffmpeg','-y','-loglevel','error','-i',f'{R}/work/proxy.mp4','-i',f'{R}/work/cliptrack.mp4','-f','image2pipe','-framerate',str(FPS),'-c:v','png','-i','-',
            '-filter_complex',fc,'-map','[v]','-c:v','libx264','-preset','medium','-crf','19','-t',str(TOTAL),'-r','30',out]
with sync_playwright() as p:
    b=p.chromium.launch(args=['--allow-file-access-from-files']);pg=b.new_page(viewport={'width':1080,'height':1920})
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)));pg.goto(f'file://{R}/reel2_{mode}.html');pg.wait_for_timeout(900)
    if args:
        from PIL import Image,ImageDraw
        ts=list(map(float,args));ims=[];os.makedirs(f'{R}/prev',exist_ok=True)
        for t in ts:
            subprocess.run(['ffmpeg','-y','-loglevel','error','-ss',str(t),'-i',f'{R}/work/proxy.mp4','-frames:v','1',f'{R}/prev/me.png'])
            subprocess.run(['ffmpeg','-y','-loglevel','error','-ss',str(t),'-i',f'{R}/work/cliptrack.mp4','-frames:v','1',f'{R}/prev/cl.png'])
            pg.evaluate(f'setT({t})');pg.screenshot(path=f'{R}/prev/f.png',omit_background=True)
            me=Image.open(f'{R}/prev/me.png').convert('RGBA')
            if mode=='split':
                bg=Image.new('RGBA',(1080,1920),'black');bg.paste(me.crop((0,430,1080,1235)).resize((980,730)),(50,1120))
            else: bg=me
            if any(a<=t<=b for a,b in WIN): bg.paste(Image.open(f'{R}/prev/cl.png').convert('RGBA'),BOX)
            bg.alpha_composite(Image.open(f'{R}/prev/f.png').convert('RGBA'))
            ims.append(bg.convert('RGB').resize((270,480)))
        M=Image.new('RGB',(7*270,((len(ims)+6)//7)*500))
        for i,(im,t) in enumerate(zip(ims,ts)):M.paste(im,((i%7)*270,(i//7)*500));ImageDraw.Draw(M).text(((i%7)*270+5,(i//7)*500+482),str(t),fill=(255,255,0))
        M.save(f'{R}/prev/sheet2_{mode}.png');print('errors',errs);sys.exit()
    ff=subprocess.Popen(compose_cmd(f'{R}/work/video2_{mode}.mp4'),stdin=subprocess.PIPE)
    for i in range(n):
        pg.evaluate(f'setT({i/FPS})');ff.stdin.write(pg.screenshot(type='png',omit_background=True))
    ff.stdin.close();ff.wait();print('done',TOTAL,'errors',errs)
