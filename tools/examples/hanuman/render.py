import json,sys,subprocess,re
from playwright.sync_api import sync_playwright
R='/home/claude/reels/hanuman';MODE=sys.argv[1];args=sys.argv[2:];FPS=30;TOTAL=84.7;n=int(TOTAL*FPS)
d=json.load(open(f'{R}/work/words.json'))
h=open(f'{R}/tpl.html').read().replace('__WORDS__',json.dumps(d['words'])).replace('__TOTAL__',str(TOTAL)).replace('__MODE__',MODE)
open(f'{R}/reel_{MODE}.html','w').write(h)
SC=[[float(a),k,ty] for a,k,ty in re.findall(r"\[([\d.]+),'(\w+)','([AB])'\]",h)]
iv=[(s[0],(SC[i+1][0] if i+1<len(SC) else TOTAL),s[2]) for i,s in enumerate(SC)]
B=[(a,b) for a,b,ty in iv if ty=='B'];Aseg=[(a,b) for a,b,ty in iv if ty=='A']
Z='1'
for a,b in reversed(Aseg): Z=f"if(between(t\\,{a}\\,{b})\\,1+0.06*min(1\\,(t-{a})/{b-a})\\,{Z})"
benB='+'.join(f"between(t\\,{a}\\,{b})" for a,b in B)
TAG="setparams=color_primaries=bt709:color_trc=bt709:colorspace=bt709:range=tv,format=yuv420p"
if MODE=='full':
    FC=(f"[0:v]scale=w='trunc(1080*{Z}/2)*2':h='trunc(1920*{Z}/2)*2':eval=frame:flags=bicubic,crop=1080:1920:(iw-1080)/2:(ih-1920)*0.3[own];"
        f"[own][2:v]overlay=0:0:enable='{benB}'[b1];"
        "[3:v]scale=-2:1000,crop=960:1000,format=rgba[oc];[oc][4:v]alphamerge[ocm];"
        "[b1][ocm]overlay=60:270:enable='between(t,13.3,18.0)'[b2];"
        f"[b2][1:v]overlay=0:0:format=auto,{TAG}[v]")
    MASKS=['-loop','1','-i',f'{R}/work/m_full.png']
else:
    FC=("[0:v]crop=1080:1560:0:360,split=2[pa][pb];[pa]scale=602:870[ps];[pb]scale=980:-2,crop=980:870,gblur=sigma=30[pbl];[pbl][ps]overlay=189:0,format=rgba[pan];[pan][5:v]alphamerge[panm];"
        "[2:v][panm]overlay=50:1010[b1];"
        "[3:v]scale=-2:760,crop=980:760,format=rgba[oc];[oc][4:v]alphamerge[ocm];"
        "[b1][ocm]overlay=50:150:enable='between(t,13.3,18.0)'[b2];"
        f"[b2][1:v]overlay=0:0:format=auto,{TAG}[v]")
    MASKS=['-loop','1','-i',f'{R}/work/m_split.png','-loop','1','-i',f'{R}/work/m_own.png']
with sync_playwright() as p:
    b=p.chromium.launch(args=['--allow-file-access-from-files']);pg=b.new_page(viewport={'width':1080,'height':1920})
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)));pg.goto(f'file://{R}/reel_{MODE}.html');pg.wait_for_timeout(1500)
    if args:  # preview: render exact frames through the same graph
        ts=list(map(float,args));import os
        os.makedirs(f'{R}/prev',exist_ok=True)
        for k,t in enumerate(ts):
            pg.evaluate(f'setT({t})');pg.wait_for_timeout(120);pg.screenshot(path=f'{R}/prev/o{k}.png',omit_background=True)
        from PIL import Image,ImageDraw
        ims=[]
        for k,t in enumerate(ts):
            fc=FC.replace('[1:v]','[1:v]')
            subprocess.run(['ffmpeg','-y','-loglevel','error','-ss',str(t),'-i',f'{R}/work/proxy.mp4','-loop','1','-i',f'{R}/prev/o{k}.png','-ss',str(t),'-i',f'{R}/work/meshbg.mp4','-stream_loop','-1','-ss',str(t),'-i',f'{R}/a/ocean.webm',*MASKS,
              '-filter_complex',FC.replace("between(t","between(t+"+str(t)).replace("min(1\\,(t-","min(1\\,(t+"+str(t)+"-").replace("between(t\\,","between(t+"+str(t)+"\\,"),'-map','[v]','-frames:v','1',f'{R}/prev/c{k}.png'],check=True)
            ims.append(Image.open(f'{R}/prev/c{k}.png').convert('RGB').resize((270,480)))
        M=Image.new('RGB',(7*270,((len(ims)+6)//7)*500))
        for i,(im,t) in enumerate(zip(ims,ts)):M.paste(im,((i%7)*270,(i//7)*500));ImageDraw.Draw(M).text(((i%7)*270+5,(i//7)*500+482),str(t),fill=(255,255,0))
        M.save(f'{R}/prev/sheet_{MODE}.png');print('errors',errs);sys.exit()
    ff=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-i',f'{R}/work/proxy.mp4','-f','image2pipe','-framerate',str(FPS),'-c:v','png','-i','-','-i',f'{R}/work/meshbg.mp4','-stream_loop','-1','-i',f'{R}/a/ocean.webm',*MASKS,
      '-filter_complex',FC,'-map','[v]','-an','-c:v','libx264','-preset','medium','-crf','18','-profile:v','high','-color_primaries','bt709','-color_trc','bt709','-colorspace','bt709','-color_range','tv','-t',str(TOTAL),'-r','30',f'{R}/work/video_only_{MODE}.mp4'],stdin=subprocess.PIPE)
    for i in range(n):
        pg.evaluate(f'setT({i/FPS})');ff.stdin.write(pg.screenshot(type='png',omit_background=True))
    ff.stdin.close();ff.wait()
    r=subprocess.run(['ffmpeg','-y','-loglevel','error','-i',f'{R}/work/video_only_{MODE}.mp4','-i',f'{R}/final_in.mov','-map','0:v','-map','1:a','-c','copy','-shortest','-movflags','+faststart',f'{R}/reel_hanuman_{MODE}.mp4'],capture_output=True,text=True)
    print('done',errs,r.returncode,r.stderr[-300:])
