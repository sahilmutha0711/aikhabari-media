import json,sys,subprocess
from playwright.sync_api import sync_playwright
R='/home/claude/reels/nylaw/work';FPS=30;TOTAL=80.6;n=int(TOTAL*FPS)
SRC='/mnt/user-data/uploads/1793476144811624.mov'
G=json.load(open(f'{R}/groups.json'))
h=open(f'{R}/tpl.html').read().replace('__GROUPS__',json.dumps(G)).replace('__TOTAL__',str(TOTAL))
open(f'{R}/reel_final.html','w').write(h)
L="format=rgb48le,lut3d=file=srgb2hlg.cube:interp=tetrahedral,scale=in_range=full:out_range=tv:out_color_matrix=bt2020,format=yuv420p10le"
def alpha_layer(idx,name):
    return (f"[{idx}:v]format=rgba,scale=2160:3840:flags=lanczos,format=rgba,split[{name}c][{name}a];[{name}a]alphaextract,format=gray[{name}al];"
            f"[{name}c]{L}[{name}col];[{name}col][{name}al]alphamerge,format=yuva420p10le[{name}]")
FC=("[0:v]fps=30,format=yuv420p10le[own];"
    f"[2:v]fps=30,scale=-2:3840:flags=lanczos,crop=2160:3840:(iw-2160)/2:0,{L}[nyc];[own][nyc]overlay=0:0:eof_action=pass:enable='between(t,21.3,28.7)':format=yuv420p10[b0];"
    +alpha_layer(3,'bi')+";[b0][bi]overlay=0:0:eof_action=pass:enable='between(t,12.6,14.05)':format=yuv420p10[b1];"
    +alpha_layer(4,'br')+";[b1][br]overlay=0:0:eof_action=pass:enable='between(t,66.6,68.75)':format=yuv420p10[b2];"
    +alpha_layer(1,'ht')+";[b2][ht]overlay=0:0:format=yuv420p10[v]")
with sync_playwright() as p:
    b=p.chromium.launch(args=['--allow-file-access-from-files']);pg=b.new_page(viewport={'width':1080,'height':1920})
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)));pg.goto(f'file://{R}/reel_final.html');pg.wait_for_timeout(1500)
    ff=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-i',SRC,'-f','image2pipe','-framerate',str(FPS),'-c:v','png','-i','-',
      '-itsoffset','21.3','-i',f'{R}/nyc.mp4','-itsoffset','12.6','-i',f'{R}/bd_illegal.mov','-itsoffset','66.6','-i',f'{R}/bd_redflag.mov','-i','../clean.wav',
      '-filter_complex',FC,'-map','[v]','-map','5:a','-c:v','libx265','-preset','veryfast','-crf','16','-pix_fmt','yuv420p10le','-tag:v','hvc1',
      '-x265-params','log-level=error:colorprim=bt2020:transfer=arib-std-b67:colormatrix=bt2020nc:range=limited',
      '-color_primaries','bt2020','-color_trc','arib-std-b67','-colorspace','bt2020nc','-color_range','tv','-c:a','aac','-b:a','256k','-t',str(TOTAL),'-movflags','+faststart','/home/claude/reels/nylaw/NYLaw_Reel.mp4'],stdin=subprocess.PIPE)
    for i in range(n):
        pg.evaluate(f'setT({i/FPS})');ff.stdin.write(pg.screenshot(type='png',omit_background=True))
    ff.stdin.close();ff.wait();print('done',errs,ff.returncode)
