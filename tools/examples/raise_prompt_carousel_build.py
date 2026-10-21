from playwright.sync_api import sync_playwright
F='file:///mnt/skills/examples/canvas-design/canvas-fonts/'
OUT='/home/claude/car/raise'
Y='#FFC93C';K='#111111';W='#F7F3EA'
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
.dots{{position:absolute;inset:0;background-image:radial-gradient(rgba(255,255,255,.07) 2px,transparent 2.5px);background-size:38px 38px}}
"""
def page(n,N,body,light=False):
    st=f'style="background:{W};color:{K}"' if light else ''
    return f"""<html><head><meta charset=utf-8><style>{CSS}</style></head><body {st}><div class=dots></div>{body}
<div class=top><span>&#9679; THE AI KHABARI</span><span>{n} / {N}</span></div>
<div class=bot><span>@theaikhabari</span><span>{'SAVE THIS' if n==N else 'SWIPE &rarr;'}</span></div></body></html>"""
H=lambda s:f'<b style="color:{Y}">{s}</b>'
S=[]
# 1 hook
S.append((f"""<div class=a style="left:-120px;top:1010px;width:1400px;height:280px;background:{Y};transform:rotate(-6deg)"></div>
<div class="a m" style="left:64px;top:130px;font-size:22px;letter-spacing:2px;color:{Y}">NURSES &middot; TEACHERS &middot; SALES &middot; ENGINEERS &middot; ANYONE WITH A BOSS</div>
<div class="a d" style="left:64px;right:50px;top:190px;font-size:116px">Asking for a raise? Let an AI boss say <span class=hl>NO</span> first.</div>
<div class="a s" style="left:64px;right:64px;top:740px;font-size:58px;line-height:1.08">One prompt that turns ChatGPT into the toughest manager you'll ever face, then grades you.</div>
<div class="a d" style="left:90px;top:1065px;font-size:96px;color:{K};transform:rotate(-6deg)">Practice. Then ask.</div>""",False))
# 2 context / framework
S.append((f"""<div class="a m" style="left:64px;top:130px;font-size:26px;letter-spacing:3px;color:{Y}">WHY MOST RAISE TALKS FAIL</div>
<div class="a d" style="left:64px;right:64px;top:185px;font-size:84px">Most people walk in with a number. Negotiators walk in with a <span class=hl>BATNA</span>.</div>
<div class=a style="left:64px;right:64px;top:600px;background:{W};color:{K};border-radius:26px;padding:34px 38px;box-shadow:10px 10px 0 {Y}">
 <div class=m style="font-size:24px;letter-spacing:2px">BATNA = BEST ALTERNATIVE TO A NEGOTIATED AGREEMENT</div>
 <div style="font-size:42px;line-height:1.3;margin-top:12px">What you'll do if they say no: another offer, a new role, a date to ask again. From <i>Getting to Yes</i>, Harvard Negotiation Project.</div></div>
<div class=a style="left:64px;right:64px;top:1000px;display:flex;gap:20px">
 <div style="flex:1;border:3px solid {Y};border-radius:22px;padding:22px"><div class=m style="color:{Y};font-size:22px">BRING 1</div><div class=d style="font-size:52px;letter-spacing:-1px">Your number</div></div>
 <div style="flex:1;border:3px solid {Y};border-radius:22px;padding:22px"><div class=m style="color:{Y};font-size:22px">BRING 2</div><div class=d style="font-size:52px;letter-spacing:-1px">3 wins, in numbers</div></div>
 <div style="flex:1;border:3px solid {Y};border-radius:22px;padding:22px"><div class=m style="color:{Y};font-size:22px">BRING 3</div><div class=d style="font-size:52px;letter-spacing:-1px">Your walk-away</div></div></div>""",False))
# 3 the prompt
P=f"""Play my manager at {H('[company / industry]')}. Be realistic and tough: the budget is tight, push back on my number, ask for proof, and try "not this cycle".<br><br>I'm asking for {H('[X% / $X]')} because {H('[3 results with numbers]')}. If you say no, my plan is {H('[my BATNA]')}.<br><br>One message at a time. After 6 turns, stop. Score me 1&ndash;10 on: {H('anchoring')}, {H('evidence')}, {H('staying calm')}, {H('getting a clear next step')}. Then rewrite my 3 weakest lines."""
S.append((f"""<div class="a m" style="left:64px;top:118px;font-size:26px;letter-spacing:3px;color:{Y}">THE PROMPT &middot; COPY IT</div>
<div class="a d" style="left:64px;right:64px;top:160px;font-size:72px">Rehearse the hardest version of the talk</div>
<div class=a style="left:64px;right:64px;top:350px;background:#1E1E1E;border:3px solid {Y};border-radius:24px;overflow:hidden">
 <div style="display:flex;gap:10px;align-items:center;padding:16px 24px;border-bottom:2px solid #333"><i style="width:18px;height:18px;border-radius:9px;background:#FF5F57;display:inline-block"></i><i style="width:18px;height:18px;border-radius:9px;background:#FEBC2E;display:inline-block"></i><i style="width:18px;height:18px;border-radius:9px;background:#28C840;display:inline-block"></i><span class=m style="color:{Y};font-size:22px;margin-left:12px">ChatGPT / Claude / Gemini</span></div>
 <div style="font-family:MonoR;font-size:32px;line-height:1.45;padding:26px 30px">{P}</div></div>
<div class="a" style="left:64px;right:64px;top:1150px;font-size:31px;line-height:1.3"><b style="color:{Y}">Pro move:</b> run it 3 times. Ask the AI to play a nicer boss, then a harsher one.</div>""",False))
# 4 cheat sheet + CTA
S.append((f"""<div class=a style="right:-220px;top:1020px;width:560px;height:560px;border-radius:50%;background:{Y}"></div>
<div class="a" style="left:64px;top:118px"><span class=m style="font-size:22px;letter-spacing:2px;background:{K};color:{Y};padding:8px 16px;border-radius:30px">SCREENSHOT THIS</span></div>
<div class="a d" style="left:64px;right:64px;top:180px;font-size:96px">Before you walk in</div>
<div class=a style="left:64px;right:64px;top:330px;display:flex;flex-direction:column;gap:20px;font-size:42px;line-height:1.25">
 <div><b>1. Anchor.</b> Say your number first, backed by your results.</div>
 <div><b>2. Prove.</b> 3 wins with numbers: money saved, made, or time cut.</div>
 <div><b>3. Know your walk-away</b> before they answer.</div>
 <div><b>4. If it's "no":</b> ask "What would it take, and by when?" Get it in writing.</div></div>
<div class="a d" style="left:64px;right:64px;top:900px;font-size:66px">Send this to the friend who's underpaid and knows it.</div>
<div class="a" style="left:64px;top:1080px"><span class=d style="font-size:56px;background:{K};color:{Y};padding:6px 22px;border-radius:14px;letter-spacing:-1px">Save this + follow @theaikhabari</span></div>
<div class="a m" style="left:64px;right:64px;top:1200px;font-size:18px;color:#555">BATNA: Fisher &amp; Ury, "Getting to Yes" (Harvard Negotiation Project). Prompt and tips are ours.</div>""",True))
N=len(S)
with sync_playwright() as p:
    b=p.chromium.launch(args=['--allow-file-access-from-files'])
    for i,(body,light) in enumerate(S,1):
        open(f'{OUT}/s{i}.html','w').write(page(i,N,body,light))
        pg=b.new_page(viewport={'width':1080,'height':1350});pg.goto(f'file://{OUT}/s{i}.html');pg.wait_for_timeout(600)
        pg.screenshot(path=f'{OUT}/slide{i}.jpg',type='jpeg',quality=93)
print('ok',N)
