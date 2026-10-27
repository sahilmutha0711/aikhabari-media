from playwright.sync_api import sync_playwright
F='file:///mnt/skills/examples/canvas-design/canvas-fonts/'
OUT='/home/claude/car/realty2'
Y='#FF6A3D';K='#1B1612';W='#F4EEE3';D='#2A211B'
CSS=f"""
@font-face{{font-family:Disp;src:url('{F}BricolageGrotesque-Bold.ttf')}}
@font-face{{font-family:Ser;src:url('{F}InstrumentSerif-Italic.ttf')}}
@font-face{{font-family:Mono;font-weight:700;src:url('{F}JetBrainsMono-Bold.ttf')}}
@font-face{{font-family:MonoR;src:url('{F}JetBrainsMono-Regular.ttf')}}
@font-face{{font-family:Sans;src:url('{F}InstrumentSans-Regular.ttf')}}
@font-face{{font-family:Sans;font-weight:700;src:url('{F}InstrumentSans-Bold.ttf')}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;overflow:hidden;color:{W};font-family:Sans;position:relative;background:{K}}}
.a{{position:absolute}}.d{{font-family:Disp;letter-spacing:-3px;line-height:.98}}.s{{font-family:Ser}}.m{{font-family:Mono;font-weight:700}}
.top{{position:absolute;left:64px;right:64px;top:52px;display:flex;justify-content:space-between;font-family:Mono;font-weight:700;font-size:22px;letter-spacing:3px;z-index:5}}
.bot{{position:absolute;left:64px;right:64px;bottom:44px;display:flex;justify-content:space-between;font-family:Mono;font-weight:700;font-size:22px;z-index:5}}
.hl{{background:{Y};color:{K};padding:0 14px;border-radius:10px}}
.grid{{position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.045) 2px,transparent 2px),linear-gradient(90deg,rgba(255,255,255,.045) 2px,transparent 2px);background-size:54px 54px}}
.lt .grid{{background-image:linear-gradient(rgba(0,0,0,.05) 2px,transparent 2px),linear-gradient(90deg,rgba(0,0,0,.05) 2px,transparent 2px)}}
.win{{background:{D};border:3px solid {Y};border-radius:24px;overflow:hidden}}
.bar{{display:flex;gap:10px;align-items:center;padding:14px 24px;border-bottom:2px solid #4A3A30}}
.bar i{{width:18px;height:18px;border-radius:9px;display:inline-block}}
"""
HOUSE=lambda x,y,s,c,fill='none':f'<svg class=a style="left:{x}px;top:{y}px" width="{s}" height="{s}" viewBox="0 0 100 100"><path d="M10 48 L50 12 L90 48 V90 H62 V64 H38 V90 H10 Z" fill="{fill}" stroke="{c}" stroke-width="5" stroke-linejoin="round"/></svg>'
def page(n,N,body,light=False):
    st=f'class=lt style="background:{W};color:{K}"' if light else ''
    return f"""<html><head><meta charset=utf-8><style>{CSS}</style></head><body {st}><div class=grid></div>{body}
<div class=top><span>&#9679; THE AI KHABARI</span><span>{n} / {N}</span></div>
<div class=bot><span>@theaikhabari</span><span>{'SAVE THIS' if n==N else 'SWIPE &rarr;'}</span></div></body></html>"""
H=lambda s:f'<b style="color:{Y}">{s}</b>'
def win(txt,label='ChatGPT / Claude / Gemini',fs=31):
    return f"""<div class=bar><i style="background:#FF5F57"></i><i style="background:#FEBC2E"></i><i style="background:#28C840"></i><span class=m style="color:{Y};font-size:22px;margin-left:12px">{label}</span></div>
<div style="font-family:MonoR;font-size:{fs}px;line-height:1.42;padding:24px 30px;color:{W}">{txt}</div>"""

def chat(app,rest,note=''):
    return f"""<div style="background:{D};border:3px solid #4A3A30;border-radius:28px;padding:26px 30px">
<div class=m style="font-size:20px;color:#A89A8E;letter-spacing:2px">TYPE IN CHATGPT</div>
<div style="font-family:MonoR;font-size:36px;line-height:1.4;margin-top:12px;color:{W}"><span style="background:{Y};color:{K};padding:0 10px;border-radius:8px;font-family:Mono;font-weight:700">{app}</span> {rest}</div>{note}</div>"""
def chatL(app,rest):
    return f"""<div style="background:#fff;border:3px solid {K};box-shadow:0 14px 0 {K};border-radius:28px;padding:26px 30px">
<div class=m style="font-size:20px;color:#9A3B1E;letter-spacing:2px">TYPE IN CHATGPT</div>
<div style="font-family:MonoR;font-size:36px;line-height:1.4;margin-top:12px;color:{K}"><span style="background:{Y};color:{K};padding:0 10px;border-radius:8px;font-family:Mono;font-weight:700">{app}</span> {rest}</div></div>"""
S=[]
S.append((HOUSE(560,700,620,Y,Y)+HOUSE(150,880,360,K)+f"""
<div class="a m" style="left:64px;top:130px;font-size:22px;letter-spacing:2px;color:#9A3B1E">REALTORS &middot; BROKERS &middot; HOME SELLERS</div>
<div class="a d" style="left:64px;right:60px;top:185px;font-size:112px">ChatGPT has <span class=hl>apps inside it</span> now. Most agents haven't noticed.</div>
<div class="a s" style="left:64px;right:540px;top:760px;font-size:50px;line-height:1.08">4 free ChatGPT add-ons + 1 Claude trick for real listing work.</div>""",True))
S.append((f"""<div class="a m" style="left:64px;top:118px;font-size:26px;letter-spacing:3px;color:{Y}">APP 1 &middot; ZILLOW</div>
<div class="a d" style="left:64px;right:64px;top:160px;font-size:80px">Check your competition <span class=hl>before</span> you price</div>
<div class="a" style="left:64px;right:64px;top:440px">{chat('Zillow,','show me 3-bed homes for sale under $650,000 in 78704')}</div>
<div class="a" style="left:64px;right:64px;top:800px;font-size:34px;line-height:1.35">Live listings with photos, maps and prices, inside the chat. See exactly what your listing is up against, then hand the buyer the same view.</div>
<div class="a m" style="left:64px;right:64px;top:1190px;font-size:20px;color:#A89A8E">US listings &middot; signed-in ChatGPT users</div>""",False))
S.append((f"""<div class="a" style="left:64px;top:118px"><span class=m style="font-size:22px;letter-spacing:2px;background:{K};color:{Y};padding:8px 16px;border-radius:30px">APP 2 &middot; ADOBE PHOTOSHOP</span></div>
<div class="a d" style="left:64px;right:64px;top:185px;font-size:80px">Fix dark listing photos in <span class=hl>10 seconds</span></div>
<div class="a" style="left:64px;right:64px;top:470px">{chatL('Photoshop,','brighten this living room photo and fix the exposure')}</div>
<div class="a" style="left:64px;right:64px;top:830px;font-size:34px;line-height:1.35">Drag the photo into the chat first. Free, with sliders to fine-tune.<br><b>Rule:</b> fix light and colour only. Never edit out a real flaw.</div>""",True))
S.append((f"""<div class="a m" style="left:64px;top:118px;font-size:26px;letter-spacing:3px;color:{Y}">APPS 3 + 4 &middot; CANVA &amp; ACROBAT</div>
<div class="a d" style="left:64px;right:64px;top:160px;font-size:76px">The "Just Listed" post and the paperwork</div>
<div class="a" style="left:64px;right:64px;top:400px">{chat('Canva,','make an Instagram "Just Listed" post for a 3-bed home in Austin, warm colours')}</div>
<div class="a" style="left:64px;right:64px;top:770px">{chat('Acrobat,','merge these disclosure PDFs into one file and compress it')}</div>
<div class="a" style="left:64px;right:64px;top:1130px;font-size:30px;line-height:1.3">One chat: post designed, documents ready to email.</div>""",False))
S.append((f"""<div class="a" style="left:64px;top:118px"><span class=m style="font-size:22px;letter-spacing:2px;background:{K};color:{Y};padding:8px 16px;border-radius:30px">CLAUDE USERS &middot; SKILLS</span></div>
<div class="a d" style="left:64px;right:64px;top:185px;font-size:78px">Teach Claude your listing style <span class=hl>once</span></div>
<div class="a" style="left:64px;right:64px;top:440px;font-size:34px;line-height:1.35">A Skill is a folder with a SKILL.md file: your tone, your MLS character limit, your Fair Housing word list, 3 of your best listings.</div>
<div class="a" style="left:64px;right:64px;top:680px;background:#fff;border:3px solid {K};box-shadow:0 14px 0 {K};border-radius:28px;padding:26px 30px;font-size:34px;line-height:1.5">
<b>1.</b> Zip the folder<br><b>2.</b> Settings &rarr; Capabilities &rarr; Skills &rarr; <b>Upload skill</b><br><b>3.</b> Say: <span style="font-family:MonoR;background:{Y};padding:0 8px;border-radius:6px">"Use my listing skill for 12 Oak St"</span></div>
<div class="a m" style="left:64px;right:64px;top:1150px;font-size:20px;color:#7A6A5E;line-height:1.5">Claude Pro, Max, Team, Enterprise &middot; code execution on</div>""",True))
S.append((HOUSE(660,830,400,Y,Y)+f"""
<div class="a" style="left:64px;top:118px"><span class=m style="font-size:22px;letter-spacing:2px;background:{Y};color:{K};padding:8px 16px;border-radius:30px">SCREENSHOT THIS</span></div>
<div class=a style="left:64px;right:64px;top:190px;display:flex;flex-direction:column;gap:22px;font-size:40px;line-height:1.2">
 <div><b style="color:{Y}">Zillow,</b> &rarr; check competing listings</div>
 <div><b style="color:{Y}">Photoshop,</b> &rarr; fix dark photos</div>
 <div><b style="color:{Y}">Canva,</b> &rarr; "Just Listed" posts</div>
 <div><b style="color:{Y}">Acrobat,</b> &rarr; merge + shrink PDFs</div>
 <div><b style="color:{Y}">Claude Skill</b> &rarr; your listing style, forever</div></div>
<div class="a d" style="left:64px;right:64px;top:640px;font-size:64px">Send this to your <span class=hl>realtor friend</span>.</div>
<div class="a" style="left:64px;top:840px"><span class=d style="font-size:46px;background:{W};color:{K};padding:8px 20px;border-radius:14px;letter-spacing:-1px">Save + follow @theaikhabari</span></div>
<div class="a m" style="left:64px;right:460px;top:1000px;font-size:18px;color:#A89A8E;line-height:1.5">Sources: OpenAI "Apps in ChatGPT" (Oct 2025); Adobe apps in ChatGPT (TechRadar, BetaNews, Dec 2025); Claude Help Center "Using Skills in Claude". Not sponsored.</div>""",False))
N=len(S)
with sync_playwright() as p:
    b=p.chromium.launch(args=['--allow-file-access-from-files'])
    for i,(body,light) in enumerate(S,1):
        open(f'{OUT}/s{i}.html','w').write(page(i,N,body,light))
        pg=b.new_page(viewport={'width':1080,'height':1350});pg.goto(f'file://{OUT}/s{i}.html');pg.wait_for_timeout(600)
        pg.screenshot(path=f'{OUT}/slide{i}.jpg',type='jpeg',quality=93)
print('ok',N)
