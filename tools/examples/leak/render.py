import json,sys,subprocess,re
from playwright.sync_api import sync_playwright
R='/home/claude/reels/leak';MODE=sys.argv[1];args=sys.argv[2:];FPS=30;TOTAL=71.9;n=int(TOTAL*FPS)
d=json.load(open(f'{R}/a/words.json'))
h=open(f'{R}/tpl.html').read().replace('__WORDS__',json.dumps(d['words'])).replace('__TOTAL__',str(TOTAL)).replace('__MODE__',MODE)
if MODE=='glass':  # captions lower so they clear the under-chin glass cards; hide our duplicate stickers where an fx plays
    h=h.replace("cap.style.top=(cur[2]==='B'?1620:1480)+'px'","cap.style.top=(((t>=9.6&&t<13.0)||(t>=44.5&&t<60.8))?1800:1690)+'px'")
open(f'{R}/reel_{MODE}.html','w').write(h)
SC=[[0,'hook','A'],[6.0,'capcom','B'],[16.6,'sbi','B'],[24.5,'scam','B'],[32.3,'todo','A'],[36.0,'s1','A'],[42.2,'s2','A'],[48.5,'s3','A'],[53.6,'s4','A'],[61.2,'otp','A'],[64.9,'cta','A']]
TAG="setparams=color_primaries=bt709:color_trc=bt709:colorspace=bt709:range=tv,format=yuv420p"
if MODE=='normal':
    iv=[(s[0],(SC[i+1][0] if i+1<len(SC) else TOTAL),s[2]) for i,s in enumerate(SC)]
    B=[(a,b) for a,b,ty in iv if ty=='B'];Aseg=[(a,b) for a,b,ty in iv if ty=='A']
    Z='1'
    for a,b in reversed(Aseg): Z=f"if(between(t\\,{a}\\,{b})\\,1+0.05*min(1\\,(t-{a})/{b-a})\\,{Z})"
    benB='+'.join(f"between(t\\,{a}\\,{b})" for a,b in B)
    SRC=f'{R}/work/proxy.mp4'
    FC=(f"[0:v]scale=w='trunc(1080*{Z}/2)*2':h='trunc(1920*{Z}/2)*2':eval=frame:flags=bicubic,crop=1080:1920:(iw-1080)/2:(ih-1920)*0.3[own];"
        f"[own][2:v]overlay=0:0:enable='{benB}'[b1];[b1][1:v]overlay=0:0:format=auto,{TAG}[v]")
    EXTRA=['-i',f'{R}/work/meshbg.mp4']
else:
    SRC=f'{R}/work/fx_full.mp4';FC=f"[0:v][1:v]overlay=0:0:format=auto,{TAG}[v]";EXTRA=[]
with sync_playwright() as p:
    b=p.chromium.launch(args=['--allow-file-access-from-files']);pg=b.new_page(viewport={'width':1080,'height':1920})
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)));pg.goto(f'file://{R}/reel_{MODE}.html');pg.wait_for_timeout(1200)
    if args:
        from PIL import Image,ImageDraw
        ims=[]
        for k,t in enumerate(map(float,args)):
            pg.evaluate(f'setT({t})');pg.wait_for_timeout(120);pg.screenshot(path=f'{R}/work/o.png',omit_background=True)
            bg=f'{R}/work/meshbg.mp4' if MODE=='normal' and any(a<=t<b for a,b in B) else SRC
            subprocess.run(['ffmpeg','-y','-loglevel','error','-ss',str(t),'-i',bg,'-i',f'{R}/work/o.png','-filter_complex','[0:v]scale=1080:1920[x];[x][1:v]overlay','-frames:v','1',f'{R}/work/c.png'],check=True)
            ims.append(Image.open(f'{R}/work/c.png').convert('RGB').resize((216,384)))
        M=Image.new('RGB',(min(len(ims),8)*216,((len(ims)+7)//8)*400))
        for i,(im,t) in enumerate(zip(ims,args)):M.paste(im,((i%8)*216,(i//8)*400));ImageDraw.Draw(M).text(((i%8)*216+4,(i//8)*400+386),t,fill=(255,255,0))
        M.save(f'{R}/work/sheet_{MODE}.png');print(errs);sys.exit()
    ff=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-i',SRC,'-f','image2pipe','-framerate',str(FPS),'-c:v','png','-i','-',*EXTRA,
      '-filter_complex',FC,'-map','[v]','-an','-c:v','libx264','-preset','medium','-crf','19','-profile:v','high','-color_primaries','bt709','-color_trc','bt709','-colorspace','bt709','-color_range','tv','-t',str(TOTAL),'-r','30',f'{R}/work/vonly_{MODE}.mp4'],stdin=subprocess.PIPE)
    for i in range(n):
        pg.evaluate(f'setT({i/FPS})');ff.stdin.write(pg.screenshot(type='png',omit_background=True))
    ff.stdin.close();ff.wait()
    r=subprocess.run(['ffmpeg','-y','-loglevel','error','-i',f'{R}/work/vonly_{MODE}.mp4','-i',f'{R}/work/clean.wav','-map','0:v','-map','1:a','-c:v','copy','-c:a','aac','-b:a','256k','-shortest','-movflags','+faststart',f'{R}/leak_reel_{MODE}.mp4'],capture_output=True,text=True)
    print('done',errs,r.returncode,r.stderr[-300:])
