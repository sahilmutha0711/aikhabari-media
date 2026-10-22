import json,sys,subprocess,os
Z=open('/home/claude/reels/wa/work/zoom.txt').read()
from playwright.sync_api import sync_playwright
R='/home/claude/reels/wa';args=sys.argv[1:];FPS=30;TOTAL=68.0;n=int(TOTAL*FPS)
d=json.load(open(f'{R}/work/words.json'))
h=open(f'{R}/tpl.html').read().replace('__WORDS__',json.dumps(d['words'])).replace('__TOTAL__',str(TOTAL))
open(f'{R}/reel.html','w').write(h)
with sync_playwright() as p:
    b=p.chromium.launch(args=['--allow-file-access-from-files']);pg=b.new_page(viewport={'width':1080,'height':1920})
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)));pg.goto(f'file://{R}/reel.html');pg.wait_for_timeout(900)
    if args:
        from PIL import Image,ImageDraw
        ts=list(map(float,args));ims=[];os.makedirs(f'{R}/prev',exist_ok=True)
        for t in ts:
            subprocess.run(['ffmpeg','-y','-loglevel','error','-ss',str(t),'-i',f'{R}/work/proxy.mp4','-frames:v','1',f'{R}/prev/bg.png'])
            pg.evaluate(f'setT({t})');pg.screenshot(path=f'{R}/prev/f.png',omit_background=True)
            bg=Image.open(f'{R}/prev/bg.png').convert('RGBA');bg.alpha_composite(Image.open(f'{R}/prev/f.png').convert('RGBA'))
            ims.append(bg.convert('RGB').resize((270,480)))
        M=Image.new('RGB',(7*270,((len(ims)+6)//7)*500))
        for i,(im,t) in enumerate(zip(ims,ts)):M.paste(im,((i%7)*270,(i//7)*500));ImageDraw.Draw(M).text(((i%7)*270+5,(i//7)*500+482),str(t),fill=(255,255,0))
        M.save(f'{R}/prev/sheet.png');print('errors',errs);sys.exit()
    ff=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-i',f'{R}/work/proxy.mp4','-f','image2pipe','-framerate',str(FPS),'-c:v','png','-i','-','-i',f'{R}/final_in.mov',
      '-filter_complex',f"[0:v]scale=w='trunc(1080*{Z}/2)*2':h='trunc(1920*{Z}/2)*2':eval=frame:flags=bicubic,crop=1080:1920:(iw-1080)/2:(ih-1920)*0.38,eq=contrast=1.03:saturation=1.05[me];"+'[me][1:v]overlay=0:0:format=auto,setparams=color_primaries=bt709:color_trc=bt709:colorspace=bt709:range=tv,format=yuv420p[v];[2:a]loudnorm=I=-14:TP=-1.5:LRA=9[a]',
      '-map','[v]','-map','[a]','-c:v','libx264','-preset','medium','-crf','19','-profile:v','high','-color_primaries','bt709','-color_trc','bt709','-colorspace','bt709','-color_range','tv',
      '-c:a','aac','-b:a','192k','-ar','48000','-t',str(TOTAL),'-r','30','-movflags','+faststart',f'{R}/reel_wa.mp4'],stdin=subprocess.PIPE)
    for i in range(n):
        pg.evaluate(f'setT({i/FPS})');ff.stdin.write(pg.screenshot(type='png',omit_background=True))
    ff.stdin.close();ff.wait();print('done',TOTAL,'errors',errs)
