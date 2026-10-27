from playwright.sync_api import sync_playwright
F='file:///mnt/skills/examples/canvas-design/canvas-fonts/';A='file:///home/claude/reels/leak/a/'
CSS=f"""@font-face{{font-family:Disp;src:url('{F}BricolageGrotesque-Bold.ttf')}}@font-face{{font-family:Ser;src:url('{F}Gloock-Regular.ttf')}}@font-face{{font-family:Mono;src:url('{F}IBMPlexMono-Bold.ttf')}}
*{{margin:0;padding:0;box-sizing:border-box}}body{{width:1080px;height:1920px;overflow:hidden;position:relative;background:url(mesh.png) center/cover;color:#fff;font-family:Disp}}.a{{position:absolute}}
.n{{background:#fff;color:#16080C;border-radius:30px;padding:22px 28px;box-shadow:0 20px 60px rgba(0,0,0,.4);display:flex;gap:20px;align-items:center}}"""
body=f"""<div class=a style="left:0;right:0;top:280px;text-align:center"><span style="font-family:Mono;font-size:30px;letter-spacing:6px;background:#FF3B47;padding:10px 24px;border-radius:40px">⚠ SECURITY ALERT</span></div>
<div class=a style="left:60px;right:60px;top:380px;text-align:center;font-size:170px;line-height:.92;letter-spacing:-5px">Your email<br><span style="color:#FFB020">leaked?</span></div>
<div class=a style="left:90px;right:90px;top:820px;display:flex;flex-direction:column;gap:22px">
<div class=n style="transform:rotate(-2deg)"><div style="width:220px;height:46px;background:url('{A}capcom_logo.png') left/contain no-repeat;flex:none"></div><div style="font-size:52px;color:#FF3B47">11.7M</div><div style="font-size:30px">records exposed</div></div>
<div class=n style="transform:rotate(1.5deg)"><div style="width:70px;height:70px;background:url('{A}sbi_icon.png') center/contain no-repeat;flex:none"></div><div style="font-size:40px">SBI data on the dark web</div></div></div>
<div class=a style="left:60px;right:60px;top:1230px;text-align:center"><span style="font-size:76px;background:#FFB020;color:#16080C;padding:6px 30px;border-radius:22px">Do this tonight →</span></div>
<div class=a style="left:0;right:0;top:1400px;text-align:center;font-family:Ser;font-size:52px">The 5-minute fix</div>"""
with sync_playwright() as p:
    b=p.chromium.launch(args=['--allow-file-access-from-files'])
    open('cover.html','w').write(f'<html><head><meta charset=utf-8><style>{CSS}</style></head><body>{body}</body></html>')
    pg=b.new_page(viewport={'width':1080,'height':1920});pg.goto('file:///home/claude/reels/leak/cov/cover.html');pg.wait_for_timeout(800);pg.screenshot(path='cover.jpg',type='jpeg',quality=93)
