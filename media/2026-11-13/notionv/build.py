import json,sys,subprocess,os
from playwright.sync_api import sync_playwright
D='/home/claude/reels/notionv';FPS=30;TOTAL=46.6;n=int(TOTAL*FPS)
SC=[0,3.0,8.2,11.0,18.1,21.0,28.9,34.8,38.4,42.2]
h=open(f'{D}/tpl.html').read().replace('__WORDS__',open(f'{D}/words.json').read()).replace('__SCENES__',json.dumps(SC)).replace('__TOTAL__',str(TOTAL))
open(f'{D}/reel.html','w').write(h)
args=sys.argv[1:]
with sync_playwright() as p:
    b=p.chromium.launch(args=['--allow-file-access-from-files']);pg=b.new_page(viewport={'width':1080,'height':1920})
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)));pg.goto(f'file://{D}/reel.html');pg.wait_for_timeout(800)
    if args:
        from PIL import Image
        ims=[]
        for t in map(float,args):
            pg.evaluate(f'setT({t})');pg.screenshot(path=f'{D}/f.png');ims.append(Image.open(f'{D}/f.png').convert('RGB').resize((270,480)))
        M=Image.new('RGB',(270*min(6,len(ims)),480*((len(ims)+5)//6)))
        for i,im in enumerate(ims):M.paste(im,((i%6)*270,(i//6)*480))
        M.save(f'{D}/sheet.jpg');print('errs',errs);sys.exit()
    ff=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','image2pipe','-framerate',str(FPS),'-c:v','mjpeg','-i','-','-i',f'{D}/voice.mp3','-af','loudnorm=I=-14,apad','-c:v','libx264','-preset','medium','-crf','20','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k','-t',str(TOTAL),'-movflags','+faststart',f'{D}/notion_reel.mp4'],stdin=subprocess.PIPE)
    for i in range(n):
        pg.evaluate(f'setT({i/FPS})');ff.stdin.write(pg.screenshot(type='jpeg',quality=90))
    ff.stdin.close();ff.wait();print('done',errs)
