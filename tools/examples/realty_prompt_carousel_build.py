from playwright.sync_api import sync_playwright
F='file:///mnt/skills/examples/canvas-design/canvas-fonts/'
OUT='/home/claude/car/realty'
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
S=[]
S.append((HOUSE(560,700,620,Y,Y)+HOUSE(150,860,380,K)+f"""
<div class="a m" style="left:64px;top:130px;font-size:22px;letter-spacing:2px;color:#9A3B1E">AGENTS &middot; BROKERS &middot; ANYONE SELLING A HOME</div>
<div class="a d" style="left:64px;right:60px;top:185px;font-size:122px">Real estate agents: steal these <span class=hl>3 AI moves</span>.</div>
<div class="a s" style="left:64px;right:540px;top:720px;font-size:54px;line-height:1.08">Not "write me a listing". The ones that actually win clients.</div>""",True))
P1=f"""Write an MLS description (max {H('[1,000]')} characters), an Instagram caption and a 3-line email for this home.<br>Use ONLY these facts: {H('[beds, baths, sq ft, year renovated, 3 standout features, parks/transit + distances]')}.<br>Describe the home, never the people who should live there.<br>Then list any phrase that could raise a Fair Housing issue and rewrite it."""
S.append((f"""<div class="a m" style="left:64px;top:118px;font-size:26px;letter-spacing:3px;color:{Y}">MOVE 1 &middot; THE LISTING</div>
<div class="a d" style="left:64px;right:64px;top:160px;font-size:76px">A listing that sells, <span class=hl>without the risk</span></div>
<div class="a win" style="left:64px;right:64px;top:370px">{win(P1)}</div>
<div class="a" style="left:64px;right:64px;top:1060px;font-size:30px;line-height:1.32"><b style="color:{Y}">Why it works:</b> AI invents details that sound true. Facts-only stops that. And lines like "ideal for families" can imply a preference: the prompt catches them before you post.</div>""",False))
P2=f"""I'm a real estate agent. My seller wants to list at {H('[$X]')}. Here are 4 recent sold comps from my MLS: {H('[address, sq ft, sold price, days on market]')}.<br>Explain my suggested price of {H('[$Y]')} in a calm 60-second talk a non-expert understands.<br>Then give the seller's 3 most likely objections and a short, respectful reply to each."""
S.append((f"""<div class="a m" style="left:64px;top:118px;font-size:26px;letter-spacing:3px;color:{Y}">MOVE 2 &middot; THE PRICE TALK</div>
<div class="a d" style="left:64px;right:64px;top:160px;font-size:76px">When the seller says "my house is worth more"</div>
<div class="a win" style="left:64px;right:64px;top:440px">{win(P2)}</div>
<div class="a" style="left:64px;right:64px;top:1070px;font-size:30px;line-height:1.32"><b style="color:{Y}">Why it works:</b> sellers trust numbers, not opinions. You walk in with the comps, the 60-second story and every pushback already answered.</div>""",False))
S.append((HOUSE(740,880,270,Y,Y)+f"""
<div class="a" style="left:64px;top:118px"><span class=m style="font-size:22px;letter-spacing:2px;background:{K};color:{Y};padding:8px 16px;border-radius:30px">MOVE 3 &middot; HIDDEN FEATURE</span></div>
<div class="a d" style="left:64px;right:64px;top:180px;font-size:84px">Zillow lives <span class=hl>inside ChatGPT</span> now.</div>
<div class="a" style="left:64px;right:64px;top:400px;font-size:38px;line-height:1.3">Start your message with <b>"Zillow,"</b> and you get live listings with photos, maps and prices, right in the chat.</div>
<div class="a" style="left:64px;right:64px;top:600px;background:#fff;border-radius:28px;padding:30px 34px;box-shadow:0 14px 0 {K};border:3px solid {K}">
 <div class=m style="font-size:20px;color:#9A3B1E;letter-spacing:2px">TRY IT</div>
 <div style="font-family:MonoR;font-size:34px;line-height:1.4;margin-top:10px">Zillow, show me 3-bed homes under $600,000 near good parks in Denver</div></div>
<div class="a" style="left:64px;right:420px;top:930px;font-size:30px;line-height:1.32"><b>Agents:</b> see your listing the way buyers now find it.<br><b>Buyers:</b> shortlist before you call an agent.</div>
<div class="a m" style="left:64px;right:64px;top:1220px;font-size:18px;color:#7A6A5E">US listings, signed-in ChatGPT users (Free, Plus, Pro).</div>""",True))
S.append((HOUSE(660,830,400,Y,Y)+f"""
<div class="a d" style="left:64px;right:64px;top:170px;font-size:104px">Send this to your <span class=hl>realtor friend</span>.</div>
<div class="a s" style="left:64px;right:64px;top:520px;font-size:58px;line-height:1.1">Or the friend selling their home this year.</div>
<div class="a" style="left:64px;top:720px"><span class=d style="font-size:54px;background:{Y};color:{K};padding:8px 22px;border-radius:14px;letter-spacing:-1px">Save this + follow @theaikhabari</span></div>
<div class="a m" style="left:64px;right:460px;top:1090px;font-size:18px;color:#A89A8E;line-height:1.5">Sources: Zillow app in ChatGPT (RISMedia, Oct 2025); listing best practices (Luxury Presence). Prompts are ours. Not legal advice: check your local Fair Housing and MLS rules.</div>""",False))
N=len(S)
with sync_playwright() as p:
    b=p.chromium.launch(args=['--allow-file-access-from-files'])
    for i,(body,light) in enumerate(S,1):
        open(f'{OUT}/s{i}.html','w').write(page(i,N,body,light))
        pg=b.new_page(viewport={'width':1080,'height':1350});pg.goto(f'file://{OUT}/s{i}.html');pg.wait_for_timeout(600)
        pg.screenshot(path=f'{OUT}/slide{i}.jpg',type='jpeg',quality=93)
print('ok',N)
