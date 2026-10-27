from playwright.sync_api import sync_playwright
F='file:///mnt/skills/examples/canvas-design/canvas-fonts/'
OUT='/home/claude/car/creative'
K='#22102E';A='#C2187A';P='#FFB020'
CSS=f"""
@font-face{{font-family:Disp;src:url('{F}BricolageGrotesque-Bold.ttf')}}
@font-face{{font-family:Ser;src:url('{F}InstrumentSerif-Italic.ttf')}}
@font-face{{font-family:Mono;font-weight:700;src:url('{F}JetBrainsMono-Bold.ttf')}}
@font-face{{font-family:MonoR;src:url('{F}JetBrainsMono-Regular.ttf')}}
@font-face{{font-family:Sans;src:url('{F}InstrumentSans-Regular.ttf')}}
@font-face{{font-family:Sans;font-weight:700;src:url('{F}InstrumentSans-Bold.ttf')}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;overflow:hidden;color:{K};font-family:Sans;position:relative;background:#FFF4FA}}
.mesh{{position:absolute;inset:-10%;filter:blur(60px)}}
.grain{{position:absolute;inset:0;opacity:.10;mix-blend-mode:multiply}}
.a{{position:absolute}}.d{{font-family:Disp;letter-spacing:-3px;line-height:.98}}.s{{font-family:Ser}}.m{{font-family:Mono;font-weight:700}}
.top{{position:absolute;left:64px;right:64px;top:52px;display:flex;justify-content:space-between;font-family:Mono;font-weight:700;font-size:21px;letter-spacing:3px;z-index:5}}
.bot{{position:absolute;left:64px;right:64px;bottom:44px;display:flex;justify-content:space-between;font-family:Mono;font-weight:700;font-size:21px;z-index:5}}
.glass{{background:rgba(255,255,255,.62);backdrop-filter:blur(18px);border:1.5px solid rgba(255,255,255,.9);border-radius:36px;box-shadow:0 24px 60px rgba(15,40,50,.14)}}
.chip{{display:inline-block;font-family:Mono;font-weight:700;font-size:20px;letter-spacing:2px;background:{K};color:#fff;padding:8px 16px;border-radius:30px}}
.hl{{background:{K};color:#fff;padding:0 16px;border-radius:14px}}
.ic{{width:92px;height:92px;border-radius:26px;display:flex;align-items:center;justify-content:center;font-family:Disp;font-size:40px;color:#fff}}
.k{{font-family:Disp;font-size:60px;letter-spacing:-1.5px}}
.t{{font-size:36px;line-height:1.3;color:#3E2A48}}
.ex{{font-family:MonoR;font-size:28px;line-height:1.4;color:{A};margin-top:14px}}
"""
GRAIN='<svg class=grain width="1080" height="1350"><filter id=n><feTurbulence type=fractalNoise baseFrequency=.9 numOctaves=3 stitchTiles=stitch/><feColorMatrix values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 .55 0"/></filter><rect width=100% height=100% filter=url(#n)/></svg>'
MESHES=[
 [('#FF8CC6',8,12,48),('#A78BFF',92,18,50),('#8FD3FF',25,95,50),('#FFF4FA',70,60,45)],
 [('#A78BFF',10,8,48),('#FF9EC9',95,45,48),('#FFD7A0',15,92,50),('#FFF4FA',55,50,40)],
 [('#8FD3FF',90,8,45),('#FF8CC6',5,55,48),('#B9A2FF',85,95,55),('#FFF4FA',50,40,40)],
]
def mesh(i):
    g=','.join(f'radial-gradient(circle at {x}% {y}%, {c} 0, transparent {r}%)' for c,x,y,r in MESHES[i%3])
    return f'<div class=mesh style="background:{g}"></div>'
def page(n,N,body):
    return f"""<html><head><meta charset=utf-8><style>{CSS}</style></head><body>{mesh(n)}{GRAIN}{body}
<div class=top><span>&#9679; THE AI KHABARI</span><span>{n} / {N}</span></div>
<div class=bot><span>@theaikhabari</span><span>{'SAVE THIS' if n==N else 'SWIPE &rarr;'}</span></div></body></html>"""
def tool(letter,col,name,what,ex):
    return f"""<div class="glass" style="padding:34px 38px;display:flex;gap:30px">
<div class=ic style="background:{col};flex:none">{letter}</div>
<div><div class=k>{name}</div><div class=t>{what}</div><div class=ex>{ex}</div></div></div>"""
S=[]
S.append(f"""<div class=a style="left:64px;top:130px"><span class=chip>FOR DESIGNERS &middot; CREATORS &middot; EDITORS</span></div>
<div class="a d" style="left:64px;right:64px;top:200px;font-size:112px">Designer or creator? Claude can now <span class=hl>drive your apps</span>.</div>
<div class="a glass" style="left:64px;right:64px;top:860px;padding:30px 36px">
 <div class=m style="font-size:20px;letter-spacing:2px;color:{A}">REAL CONNECTORS, NOT JUST PROMPTS</div>
 <div style="display:flex;gap:14px;margin-top:18px;flex-wrap:wrap">
 {''.join(f'<span style="font-family:Disp;font-size:40px;background:#fff;border-radius:18px;padding:10px 22px">{x}</span>' for x in ['Adobe','Canva','Figma','Descript'])}</div>
 <div class=s style="font-size:44px;margin-top:22px">You type. Your creative apps do the work.</div></div>""")
S.append(f"""<div class=a style="left:64px;top:130px"><span class=chip>CONNECTORS &middot; PHOTOS + DESIGN</span></div>
<div class="a d" style="left:64px;right:64px;top:200px;font-size:84px">Photoshop and Canva, from the chat</div>
<div class=a style="left:64px;right:64px;top:430px;display:flex;flex-direction:column;gap:40px">
{tool('Ps','#2F6BFF','Adobe for Creativity','50+ tools across Photoshop, Lightroom, Illustrator, Firefly, Premiere and Express.','"Remove the background from these 20 product shots and resize for Instagram"')}
{tool('C','#7D2AE8','Canva','Makes editable Canva designs, using your Brand Kit and templates.','"A launch post in our brand kit, in 3 sizes"')}
</div><div class="a s" style="left:64px;right:64px;top:1185px;font-size:46px;line-height:1.1">The boring 80% of the job, done in one message.</div>""")
S.append(f"""<div class=a style="left:64px;top:130px"><span class=chip>CONNECTORS &middot; UI + VIDEO</span></div>
<div class="a d" style="left:64px;right:64px;top:200px;font-size:84px">Figma files and video edits</div>
<div class=a style="left:64px;right:64px;top:430px;display:flex;flex-direction:column;gap:40px">
{tool('F','#F24E1E','Figma','Reads your real file: components, tokens, layout. Turns a frame into code, or a live website into editable layers.','"Build this frame as a React component using our tokens"')}
{tool('D','#22102E','Descript','Edit video by text: remove filler words and retakes, Studio Sound, captions, clips.','"Remove the ums, add captions, cut a 30-second clip"')}
</div><div class="a s" style="left:64px;right:64px;top:1222px;font-size:44px;line-height:1.1">From design file to shipped, without the copy-paste.</div>""")
S.append(f"""<div class=a style="left:64px;top:130px"><span class=chip>TRY IT &middot; TWO CONNECTORS</span></div>
<div class="a d" style="left:64px;right:64px;top:200px;font-size:84px">A week of content, one prompt</div>
<div class="a glass" style="left:64px;right:64px;top:440px;overflow:hidden;background:rgba(34,16,46,.93);border-color:rgba(255,255,255,.2)">
 <div style="display:flex;gap:10px;align-items:center;padding:18px 28px;border-bottom:1.5px solid rgba(255,255,255,.15)"><i style="width:18px;height:18px;border-radius:9px;background:#FF5F57"></i><i style="width:18px;height:18px;border-radius:9px;background:#FEBC2E"></i><i style="width:18px;height:18px;border-radius:9px;background:#28C840"></i><span class=m style="color:#FF9EC9;font-size:21px;margin-left:12px">Claude</span></div>
 <div style="font-family:MonoR;font-size:33px;line-height:1.45;padding:30px 34px;color:#fff">With Descript: clean up my episode <b style="color:#FFD7A0">[name]</b>, remove filler words and retakes, add captions, and cut 3 clips under 45 seconds.<br><br>With Canva: make a thumbnail for each clip in my brand kit.</div></div>
<div class="a s" style="left:64px;right:64px;top:1120px;font-size:44px;line-height:1.1">Review before you publish. Your taste still wins.</div>""")
S.append(f"""<div class=a style="left:64px;top:130px"><span class=chip>SWITCH IT ON</span></div>
<div class="a glass" style="left:64px;right:64px;top:210px;padding:36px 40px;font-size:36px;line-height:1.6">
<b>1.</b> Claude &rarr; Settings &rarr; <b>Connectors</b><br><b>2.</b> Add Adobe, Canva, Figma or Descript<br><b>3.</b> Sign in with your own account</div>
<div class="a t" style="left:64px;right:64px;top:520px;font-size:28px">Uses your existing accounts and AI credits. Some features need paid plans.</div>
<div class="a d" style="left:64px;right:64px;top:640px;font-size:68px">Know a <span class=hl>designer or creator</span>? Send this to them.</div>
<div class="a glass" style="left:64px;right:64px;top:830px;padding:26px 34px">
 <div class="s" style="font-size:42px;line-height:1.1">Creating yourself?</div>
 <div style="font-family:Disp;font-size:44px;letter-spacing:-1px;margin-top:10px"><span style="background:#22102E;color:#fff;padding:2px 14px;border-radius:12px">Save this</span> + follow <span style="color:#C2187A">@theaikhabari</span></div>
 <div class=t style="font-size:28px;margin-top:8px">New AI tools for your field, every week.</div></div>
<div class="a m" style="left:64px;right:64px;top:1180px;font-size:17px;line-height:1.5;color:#5A4466">Sources: Adobe blog (Apr 2026); canva.com; descript.com/mcp; Figma MCP docs via toools.design. Example prompts are ours. Not sponsored.</div>""")
N=len(S)
with sync_playwright() as p:
    b=p.chromium.launch(args=['--allow-file-access-from-files'])
    for i,body in enumerate(S,1):
        open(f'{OUT}/s{i}.html','w').write(page(i,N,body))
        pg=b.new_page(viewport={'width':1080,'height':1350});pg.goto(f'file://{OUT}/s{i}.html');pg.wait_for_timeout(700)
        pg.screenshot(path=f'{OUT}/slide{i}.jpg',type='jpeg',quality=93)
print('ok',N)
