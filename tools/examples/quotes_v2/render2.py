import sys,subprocess
from playwright.sync_api import sync_playwright
R='/home/claude/reels/quotes';FPS=30;T=28.0;n=int(T*FPS);args=sys.argv[1:]
with sync_playwright() as p:
    b=p.chromium.launch(args=['--allow-file-access-from-files']);pg=b.new_page(viewport={'width':1080,'height':1920})
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)));pg.goto(f'file://{R}/tpl2.html');pg.wait_for_timeout(1200)
    if args:
        from PIL import Image,ImageDraw
        ims=[]
        for k,t in enumerate(map(float,args)):
            pg.evaluate(f'setT({t})');pg.wait_for_timeout(150);pg.screenshot(path=f'{R}/o.png',omit_background=True)
            subprocess.run(['ffmpeg','-y','-loglevel','error','-ss',str(t),'-i',f'{R}/meshbg2.mp4','-i',f'{R}/o.png','-filter_complex','[0:v][1:v]overlay','-frames:v','1',f'{R}/c.png'],check=True)
            ims.append(Image.open(f'{R}/c.png').convert('RGB').resize((270,480)))
        M=Image.new('RGB',(len(ims)*270,500));[M.paste(im,(i*270,0)) for i,im in enumerate(ims)];M.save(f'{R}/sheet.png');print(errs);sys.exit()
    ff=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-i',f'{R}/meshbg2.mp4','-f','image2pipe','-framerate',str(FPS),'-c:v','png','-i','-',
      '-filter_complex','[0:v][1:v]overlay=0:0:format=auto,setparams=color_primaries=bt709:color_trc=bt709:colorspace=bt709:range=tv,format=yuv420p[v]',
      '-map','[v]','-c:v','libx264','-crf','20','-preset','medium','-color_primaries','bt709','-color_trc','bt709','-colorspace','bt709','-color_range','tv','-t',str(T),'-movflags','+faststart',f'{R}/quotes_reel_v2.mp4'],stdin=subprocess.PIPE)
    for i in range(n):
        pg.evaluate(f'setT({i/FPS})');ff.stdin.write(pg.screenshot(type='png',omit_background=True))
    ff.stdin.close();ff.wait();print('done',errs)
