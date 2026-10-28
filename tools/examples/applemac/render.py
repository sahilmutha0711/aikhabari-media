import json,sys,subprocess
from playwright.sync_api import sync_playwright
R='/home/claude/reels/mac/work';PAL=sys.argv[1];args=sys.argv[2:];FPS=30;TOTAL=78.4;n=int(TOTAL*FPS)
G=json.load(open(f'{R}/groups.json'))
h=open(f'{R}/tpl.html').read().replace('__GROUPS__',json.dumps(G)).replace('__TOTAL__',str(TOTAL)).replace('__PAL__',PAL)
open(f'{R}/reel_{PAL}.html','w').write(h)
AS=[(0,10.45),(53.2,59.9),(72.9,78.5)]
Z='1'
for a,b in reversed(AS): Z=f"if(between(t\\,{a}\\,{b})\\,1+0.06*min(1\\,(t-{a})/{b-a})\\,{Z})"
benA='+'.join(f"between(t\\,{a}\\,{b})" for a,b in AS)
TAG="setparams=color_primaries=bt709:color_trc=bt709:colorspace=bt709:range=tv,format=yuv420p"
FC=(f"[0:v]scale=w='trunc(1080*{Z}/2)*2':h='trunc(1920*{Z}/2)*2':eval=frame:flags=bicubic,crop=1080:1920:(iw-1080)/2:(ih-1920)*0.3[own];"
    f"[2:v][own]overlay=0:0:enable='{benA}'[b1];[b1][1:v]overlay=0:0:format=auto,{TAG}[v]")
with sync_playwright() as p:
    b=p.chromium.launch(args=['--allow-file-access-from-files']);pg=b.new_page(viewport={'width':1080,'height':1920})
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)));pg.goto(f'file://{R}/reel_{PAL}.html');pg.wait_for_timeout(1500)
    if args:
        from PIL import Image,ImageDraw
        ims=[]
        for t in map(float,args):
            pg.evaluate(f'setT({t})');pg.wait_for_timeout(150);pg.screenshot(path=f'{R}/o.png',omit_background=True)
            bg='../proxy_tm.mp4' if any(a<=t<b for a,b in AS) else f'broll2_{PAL}.mp4'
            subprocess.run(['ffmpeg','-y','-loglevel','error','-ss',str(t),'-i',bg,'-i',f'{R}/o.png','-filter_complex','[0:v]scale=1080:1920[x];[x][1:v]overlay','-frames:v','1',f'{R}/c.png'],check=True)
            ims.append(Image.open(f'{R}/c.png').convert('RGB').resize((270,480)))
        M=Image.new('RGB',(min(len(ims),8)*270,((len(ims)+7)//8)*500))
        for i,(im,t) in enumerate(zip(ims,args)):M.paste(im,((i%8)*270,(i//8)*500));ImageDraw.Draw(M).text(((i%8)*270+4,(i//8)*500+484),t,fill=(255,255,0))
        M.save(f'/tmp/claude-0/-home-claude/acedb731-8581-5c7e-8ffe-4bf86f59215c/scratchpad/sheet_{PAL}.jpg');print(errs);sys.exit()
    ff=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-i','../proxy_tm.mp4','-f','image2pipe','-framerate',str(FPS),'-c:v','png','-i','-','-i',f'broll2_{PAL}.mp4',
      '-filter_complex',FC,'-map','[v]','-an','-c:v','libx264','-preset','medium','-crf','19','-profile:v','high','-color_primaries','bt709','-color_trc','bt709','-colorspace','bt709','-color_range','tv','-t',str(TOTAL),'-r','30',f'{R}/vonly_{PAL}.mp4'],stdin=subprocess.PIPE)
    for i in range(n):
        pg.evaluate(f'setT({i/FPS})');ff.stdin.write(pg.screenshot(type='png',omit_background=True))
    ff.stdin.close();ff.wait()
    r=subprocess.run(['ffmpeg','-y','-loglevel','error','-i',f'{R}/vonly_{PAL}.mp4','-i','../vclean.wav','-map','0:v','-map','1:a','-c:v','copy','-c:a','aac','-b:a','256k','-shortest','-movflags','+faststart',f'/home/claude/reels/mac/AppleTouchMac_{PAL}_v2.mp4'],capture_output=True,text=True)
    print('done',errs,r.returncode,r.stderr[-300:])
