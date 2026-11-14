import base64,subprocess
from playwright.sync_api import sync_playwright
D='/home/claude/reels/wallet';FPS=30;T=68.833;N=int(T*FPS)+1;LUT='/home/claude/reels/antv/work/srgb2hlg.cube'
fc=(f"[1:v]scale=1512:2688:flags=lanczos,format=rgb24,lut3d={LUT},format=yuv420p10le,fps=60[b];"
 "[0:v][b]overlay=0:0:enable='between(t,7.27,44.7)+between(t,49.3,64.4)'[v1];"
 f"[2:v]scale=1512:2688:flags=lanczos,format=rgba,split[c][a];[a]alphaextract,format=gray[al];[c]format=rgb24,lut3d={LUT},format=yuva420p10le[cy];[cy][al]alphamerge[ov];"
 "[v1][ov]overlay=0:0:format=auto,format=yuv420p10le[v];[0:a]loudnorm=I=-14:TP=-1.5[a]")
ff=subprocess.Popen(['ffmpeg','-nostdin','-y','-v','error','-i',f'{D}/src.mov','-i',f'{D}/broll_track.mp4','-f','image2pipe','-framerate',str(FPS),'-c:v','png','-i','-',
 '-filter_complex',fc,'-map','[v]','-map','[a]','-c:v','libx265','-crf','17','-preset','medium','-x265-params','colorprim=bt2020:transfer=arib-std-b67:colormatrix=bt2020nc:log-level=error',
 '-color_primaries','bt2020','-color_trc','arib-std-b67','-colorspace','bt2020nc','-tag:v','hvc1','-c:a','aac','-b:a','192k','-t',str(T),'-movflags','+faststart',f'{D}/ChatGPT_Wallet_Reel.mp4'],stdin=subprocess.PIPE)
with sync_playwright() as p:
    b=p.chromium.launch(args=['--allow-file-access-from-files']);pg=b.new_page(viewport={'width':1080,'height':1920})
    pg.goto(f'file://{D}/ov.html');pg.wait_for_timeout(1000)
    cdp=pg.context.new_cdp_session(pg);cdp.send('Emulation.setDefaultBackgroundColorOverride',{'color':{'r':0,'g':0,'b':0,'a':0}})
    bad=0
    for i in range(N):
        pg.evaluate(f'setT({i/FPS})')
        png=base64.b64decode(cdp.send('Page.captureScreenshot',{'format':'png'})['data'])
        if png[25]!=6: bad+=1
        ff.stdin.write(png)
    ff.stdin.close();ff.wait();print('done bad',bad)
