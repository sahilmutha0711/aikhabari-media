# usage: python3 gen_build.py REELDIR [t1 t2 ...]   (REELDIR has script.json, spec.json, photos)
import json,wave,sys,subprocess,numpy as np,os
from playwright.sync_api import sync_playwright
R=os.path.abspath(sys.argv[1]);args=sys.argv[2:];FPS=30;K=os.path.dirname(os.path.abspath(__file__))
if not os.path.exists(f'{R}/audio/words.json'): subprocess.run(['python3','/home/claude/tools/tts.py',f'{R}/script.json',f'{R}/audio'],check=True)
d=json.load(open(f'{R}/audio/words.json'));Wd=d['words']
w=wave.open(f'{R}/audio/voice.wav');a=np.frombuffer(w.readframes(w.getnframes()),np.int16)/32767.;sr=w.getframerate()
TOTAL=round(d['duration']+0.8,2);n=int(TOTAL*FPS);hop=sr//FPS
env=[float(np.sqrt((a[i*hop:(i+1)*hop]**2).mean())) if i*hop<len(a) else 0 for i in range(n)];m=max(env);env=[round(min(1,e/m*1.4),3) for e in env]
h=open(os.environ.get('TPL',f'{K}/gen.html.tpl')).read()
for k,v in {'__WORDS__':json.dumps(Wd),'__ENV__':json.dumps(env),'__TOTAL__':str(TOTAL),'__FPS__':str(FPS),'__DIR__':'file://'+R,'__OWLDIR__':'file:///home/claude/kit2'}.items():h=h.replace(k,v)
open(f'{R}/reel.html','w').write(h)
with sync_playwright() as p:
    b=p.chromium.launch(args=['--allow-file-access-from-files']);pg=b.new_page(viewport={'width':1080,'height':1920})
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)));pg.goto(f'file://{R}/reel.html');pg.wait_for_timeout(800)
    if args:
        from PIL import Image,ImageDraw
        ts=list(map(float,args));ims=[];os.makedirs(f'{R}/prev',exist_ok=True)
        for t in ts: pg.evaluate(f'setT({t})');pg.screenshot(path=f'{R}/prev/f.png');ims.append(Image.open(f'{R}/prev/f.png').convert('RGB').resize((270,480)))
        M=Image.new('RGB',(7*270,((len(ims)+6)//7)*500))
        for i,(im,t) in enumerate(zip(ims,ts)):M.paste(im,((i%7)*270,(i//7)*500));ImageDraw.Draw(M).text(((i%7)*270+5,(i//7)*500+482),str(t),fill=(255,255,0))
        M.save(f'{R}/prev/sheet.png');print('dur',TOTAL,'errors',errs);sys.exit()
    ff=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','image2pipe','-framerate',str(FPS),'-c:v','mjpeg','-i','-','-i',f'{R}/audio/voice.wav','-af','apad','-c:v','libx264','-preset','medium','-crf','21','-pix_fmt','yuv420p','-c:a','aac','-b:a','160k','-t',str(TOTAL),'-movflags','+faststart',f'{R}/reel.mp4'],stdin=subprocess.PIPE)
    for i in range(n):
        pg.evaluate(f'setT({i/FPS})');ff.stdin.write(pg.screenshot(type='jpeg',quality=90))
    ff.stdin.close();ff.wait();print('done',TOTAL,'errors',errs)
