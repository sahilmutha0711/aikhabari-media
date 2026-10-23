from playwright.sync_api import sync_playwright
F='file:///mnt/skills/examples/canvas-design/canvas-fonts/';A='file:///home/claude/reels/hanuman/a/'
CSS=f"""@font-face{{font-family:Disp;src:url('{F}BricolageGrotesque-Bold.ttf')}}@font-face{{font-family:Ser;src:url('{F}Gloock-Regular.ttf')}}@font-face{{font-family:Ital;src:url('{F}InstrumentSerif-Italic.ttf')}}@font-face{{font-family:Mono;src:url('{F}IBMPlexMono-Bold.ttf')}}
*{{margin:0;padding:0;box-sizing:border-box}}body{{width:1080px;height:1920px;overflow:hidden;position:relative;background:url(mesh.png) center/cover;color:#fff;font-family:Disp}}
.a{{position:absolute}}.grain{{position:absolute;inset:0;opacity:.18;mix-blend-mode:overlay}}"""
G='<svg class=grain width=1080 height=1920><filter id=n><feTurbulence type=fractalNoise baseFrequency=.85 numOctaves=2/></filter><rect width=100% height=100% filter=url(#n)/></svg>'
c1=f"""{G}<div class=a style="left:0;right:0;top:250px;text-align:center"><span style="font-family:Mono;font-size:30px;letter-spacing:6px;background:#FFF8EC;color:#1A1033;padding:10px 24px;border-radius:40px">RAMAYANA &times; AI</span></div>
<div class=a style="left:150px;right:150px;top:360px;height:740px;border-radius:44px;overflow:hidden;border:4px solid rgba(255,214,120,.9);box-shadow:0 40px 100px rgba(10,4,30,.55);background:url({A}hanuman_mountain.jpg) 50% 25%/cover"></div>
<div class=a style="left:60px;right:60px;top:1160px;text-align:center;font-family:Ser;font-size:112px;line-height:1.02;text-shadow:0 8px 30px rgba(20,6,40,.6)">He forgot how<br>strong he was.</div>
<div class=a style="left:0;right:0;top:1420px;text-align:center"><span style="font-family:Disp;font-size:76px;background:#FFB020;color:#1A1033;padding:4px 30px;border-radius:20px">So have you.</span></div>"""
c2=f"""{G}<div class=a style="left:70px;top:260px;font-family:Mono;font-size:30px;letter-spacing:5px">THE AI KHABARI &middot; STORY</div>
<div class=a style="left:70px;right:70px;top:330px;font-family:Ser;font-size:150px;line-height:.98">The <span style="color:#FFB020">Hanuman</span> lesson every techie needs</div>
<div class=a style="left:70px;top:1000px;width:430px;height:600px;border-radius:36px;overflow:hidden;border:4px solid rgba(255,214,120,.9);transform:rotate(-4deg);box-shadow:0 30px 80px rgba(10,4,30,.5);background:url({A}bhakta.jpg) center/cover"></div>
<div class=a style="left:540px;top:1060px;width:470px;font-family:Disp;font-size:50px;line-height:1.15">
<div style="background:#FFF8EC;color:#1A1033;border-radius:24px;padding:18px 24px;transform:rotate(2deg)">💭 "I'm not good enough"</div>
<div style="margin-top:26px;background:#1A1033;border-radius:24px;padding:18px 24px;transform:rotate(-2deg)">😟 "AI will replace me"</div>
<div style="margin-top:26px;background:#FFB020;color:#1A1033;border-radius:24px;padding:18px 24px;transform:rotate(1deg)">You need a Jambavan 🙏</div></div>"""
with sync_playwright() as p:
    b=p.chromium.launch(args=['--allow-file-access-from-files'])
    for n,body in [('cover1',c1),('cover2',c2)]:
        open(f'{n}.html','w').write(f'<html><head><meta charset=utf-8><style>{CSS}</style></head><body>{body}</body></html>')
        pg=b.new_page(viewport={'width':1080,'height':1920});pg.goto(f'file:///home/claude/reels/hanuman/cov/{n}.html');pg.wait_for_timeout(800);pg.screenshot(path=f'{n}.jpg',type='jpeg',quality=93)
