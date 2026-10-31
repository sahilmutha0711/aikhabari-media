import json,sys,subprocess
from playwright.sync_api import sync_playwright
from PIL import Image,ImageDraw
R='/home/claude/reels/nylaw/work';ts=list(map(float,sys.argv[1:]));SRC='/mnt/user-data/uploads/1793476144811624.mov'
G=json.load(open(f'{R}/groups.json'))
h=open(f'{R}/tpl.html').read().replace('__GROUPS__',json.dumps(G)).replace('__TOTAL__','80.6')
open(f'{R}/reel.html','w').write(h)
def base(t):
    if 21.3<=t<28.7:
        return ['-ss',str(t-21.3),'-i',f'{R}/nyc.mp4'],'[0:v]scale=-2:1920,crop=1080:1920:(iw-1080)/2:0[x]'
    return ['-ss',str(t),'-i',SRC],'[0:v]scale=1080:1920[x]'
with sync_playwright() as p:
    b=p.chromium.launch(args=['--allow-file-access-from-files']);pg=b.new_page(viewport={'width':1080,'height':1920})
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)));pg.goto(f'file://{R}/reel.html');pg.wait_for_timeout(1500)
    ims=[]
    for t in ts:
        pg.evaluate(f'setT({t})');pg.wait_for_timeout(150);pg.screenshot(path=f'{R}/o.png',omit_background=True)
        inp,fc=base(t);extra=[];chain='[x]'
        for nm,a0,a1 in [('bd_illegal',12.6,14.05),('bd_redflag',66.6,68.75)]:
            if a0<=t<a1: extra=['-ss',str(t-a0),'-i',f'{R}/{nm}.mov'];fc+=';[x][2:v]overlay[x2]';chain='[x2]'
        cmd=['ffmpeg','-y','-loglevel','error',*inp,'-i',f'{R}/o.png',*extra,'-filter_complex',fc+f';{chain}[1:v]overlay','-frames:v','1',f'{R}/c.png']
        subprocess.run(cmd,check=True)
        ims.append(Image.open(f'{R}/c.png').convert('RGB').resize((270,480)))
M=Image.new('RGB',(min(len(ims),7)*270,((len(ims)+6)//7)*500))
for i,(im,t) in enumerate(zip(ims,ts)):M.paste(im,((i%7)*270,(i//7)*500));ImageDraw.Draw(M).text(((i%7)*270+4,(i//7)*500+484),str(t),fill=(255,255,0))
M.save('/home/claude/reels/nylaw/Template_NYlaw.jpg');print(errs)
