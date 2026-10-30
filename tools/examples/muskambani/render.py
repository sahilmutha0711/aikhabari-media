import json,sys,subprocess
from playwright.sync_api import sync_playwright
R='/home/claude/reels/ambani/work';PAL=sys.argv[1];args=sys.argv[2:];FPS=30;TOTAL=83.6;n=int(TOTAL*FPS)
SRC='/mnt/user-data/uploads/1793321170217489.mov'
G=json.load(open(f'{R}/groups.json'))
h=open(f'{R}/tpl.html').read().replace('__GROUPS__',json.dumps(G)).replace('__TOTAL__',str(TOTAL)).replace('__PAL__',PAL)
open(f'{R}/reel_{PAL}.html','w').write(h)
Z="zscale=tin=iec61966-2-1:pin=709:min=gbr:rin=full:t=linear:p=2020:m=gbr:npl=203,zscale=t=arib-std-b67:m=2020_ncl:r=limited:npl=203"
with sync_playwright() as p:
    b=p.chromium.launch(args=['--allow-file-access-from-files']);pg=b.new_page(viewport={'width':1080,'height':1920})
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)));pg.goto(f'file://{R}/reel_{PAL}.html');pg.wait_for_timeout(1500)
    if args:
        from PIL import Image,ImageDraw
        ims=[]
        for t in map(float,args):
            pg.evaluate(f'setT({t})');pg.wait_for_timeout(150);pg.screenshot(path=f'{R}/o.png',omit_background=True)
            subprocess.run(['ffmpeg','-y','-loglevel','error','-ss',str(t),'-i','../proxy.mp4','-i',f'{R}/o.png','-filter_complex','[0:v]scale=1080:1920[x];[x][1:v]overlay','-frames:v','1',f'{R}/c.png'],check=True)
            ims.append(Image.open(f'{R}/c.png').convert('RGB').resize((270,480)))
        M=Image.new('RGB',(min(len(ims),8)*270,((len(ims)+7)//8)*500))
        for i,(im,t) in enumerate(zip(ims,args)):M.paste(im,((i%8)*270,(i//8)*500));ImageDraw.Draw(M).text(((i%8)*270+4,(i//8)*500+484),t,fill=(255,255,0))
        M.save(f'/tmp/claude-0/-home-claude/acedb731-8581-5c7e-8ffe-4bf86f59215c/scratchpad/amb_{PAL}.jpg');print(errs);sys.exit()
    FC=(f"[0:v]scale=1080:1920:flags=bicubic,fps=30,format=yuv420p10le[own];[1:v]format=rgba,split[c][a];[a]alphaextract,format=gray[al];"
        f"[c]format=gbrpf32le,{Z},format=yuv420p10le[col];[col][al]alphamerge,format=yuva420p10le[ov];[own][ov]overlay=0:0:format=yuv420p10[v]")
    ff=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-i',SRC,'-f','image2pipe','-framerate',str(FPS),'-c:v','png','-i','-','-i','../clean.wav',
      '-filter_complex',FC,'-map','[v]','-map','2:a','-c:v','libx265','-preset','medium','-crf','20','-pix_fmt','yuv420p10le','-tag:v','hvc1',
      '-x265-params','log-level=error:colorprim=bt2020:transfer=arib-std-b67:colormatrix=bt2020nc:range=limited',
      '-color_primaries','bt2020','-color_trc','arib-std-b67','-colorspace','bt2020nc','-color_range','tv','-c:a','aac','-b:a','256k','-t',str(TOTAL),'-movflags','+faststart',f'/home/claude/reels/ambani/MuskAmbani_{PAL}.mp4'],stdin=subprocess.PIPE)
    for i in range(n):
        pg.evaluate(f'setT({i/FPS})');ff.stdin.write(pg.screenshot(type='png',omit_background=True))
    ff.stdin.close();ff.wait();print('done',errs,ff.returncode)
