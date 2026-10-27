import json,sys,subprocess,os
from playwright.sync_api import sync_playwright
R='/home/claude/reels/court';args=sys.argv[1:];FPS=30
d=json.load(open(f'{R}/audio/words.json'));Wd=d['words'];TOTAL=round(d['duration']+0.5,2);n=int(TOTAL*FPS)
h=open(f'{R}/tpl.html').read()
for k,v in {'__WORDS__':json.dumps(Wd),'__TOTAL__':str(TOTAL),'__DIR__':'file://'+R}.items():h=h.replace(k,v)
open(f'{R}/reel.html','w').write(h)
with sync_playwright() as p:
    b=p.chromium.launch(args=['--allow-file-access-from-files']);pg=b.new_page(viewport={'width':1080,'height':1920})
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)));pg.goto(f'file://{R}/reel.html');pg.wait_for_timeout(900)
    if args:
        from PIL import Image,ImageDraw
        ts=list(map(float,args));ims=[];os.makedirs(f'{R}/prev',exist_ok=True)
        for t in ts:
            subprocess.run(['ffmpeg','-y','-loglevel','error','-ss',str(t),'-i',f'{R}/work/base.mp4','-frames:v','1',f'{R}/prev/bg.png'])
            pg.evaluate(f'setT({t})');pg.screenshot(path=f'{R}/prev/f.png',omit_background=True)
            bg=Image.open(f'{R}/prev/bg.png').convert('RGBA');fg=Image.open(f'{R}/prev/f.png').convert('RGBA');bg.alpha_composite(fg)
            ims.append(bg.convert('RGB').resize((270,480)))
        M=Image.new('RGB',(7*270,((len(ims)+6)//7)*500))
        for i,(im,t) in enumerate(zip(ims,ts)):M.paste(im,((i%7)*270,(i//7)*500));ImageDraw.Draw(M).text(((i%7)*270+5,(i//7)*500+482),str(t),fill=(255,255,0))
        M.save(f'{R}/prev/sheet.png');print('errors',errs);sys.exit()
    ff=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-i',f'{R}/work/base.mp4','-f','image2pipe','-framerate',str(FPS),'-c:v','png','-i','-','-i',f'{R}/audio/voice.wav','-i',f'{R}/work/logo48.wav',
      '-filter_complex','[0:v][1:v]overlay=0:0:format=auto,format=yuv420p[v];[3:a]volume=0.7[l];[2:a][l]amix=inputs=2:duration=first:normalize=0,apad[a]',
      '-map','[v]','-map','[a]','-c:v','libx264','-preset','medium','-crf','19','-c:a','aac','-b:a','192k','-t',str(TOTAL),'-movflags','+faststart',f'{R}/reel.mp4'],stdin=subprocess.PIPE)
    for i in range(n):
        pg.evaluate(f'setT({i/FPS})');ff.stdin.write(pg.screenshot(type='png',omit_background=True))
    ff.stdin.close();ff.wait();print('done',TOTAL,'errors',errs)
