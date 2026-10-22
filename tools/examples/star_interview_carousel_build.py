from playwright.sync_api import sync_playwright
F='file:///mnt/skills/examples/canvas-design/canvas-fonts/'
OUT='/home/claude/car/star'
Y='#3DF5B0';K='#24104F';W='#F6F2FF'
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
S.append((f"""<div class=a style="right:-180px;top:880px;width:640px;height:640px;border-radius:50%;background:{Y}"></div>
<div class=a style="right:120px;top:1010px;width:260px;height:260px;border-radius:50%;border:22px solid {K}"></div>
<div class="a m" style="left:64px;top:130px;font-size:22px;letter-spacing:2px;color:{Y}">FRESHERS &middot; CAREER SWITCHERS &middot; ANY JOB, ANY INDUSTRY</div>
<div class="a d" style="left:64px;right:50px;top:185px;font-size:118px">Interview tomorrow? Let AI <span class=hl>grill you</span> tonight.</div>
<div class="a s" style="left:64px;right:420px;top:760px;font-size:58px;line-height:1.08">The answer method Amazon tells every candidate to use, as one prompt.</div>""",False))
S.append((f"""<div class="a m" style="left:64px;top:130px;font-size:26px;letter-spacing:3px;color:{Y}">WHY GOOD PEOPLE FAIL INTERVIEWS</div>
<div class="a d" style="left:64px;right:64px;top:185px;font-size:84px">They tell a story with no <span class=hl>result</span>.</div>
<div class=a style="left:64px;right:64px;top:470px;display:grid;grid-template-columns:1fr 1fr;gap:20px">
 <div style="background:{W};color:{K};border-radius:24px;padding:24px 28px"><div class=d style="font-size:110px;color:{K}">S</div><div style="font-size:36px"><b>Situation</b><br>where, when</div></div>
 <div style="background:{W};color:{K};border-radius:24px;padding:24px 28px"><div class=d style="font-size:110px">T</div><div style="font-size:36px"><b>Task</b><br>your goal</div></div>
 <div style="background:{W};color:{K};border-radius:24px;padding:24px 28px"><div class=d style="font-size:110px">A</div><div style="font-size:36px"><b>Action</b><br>what <u>you</u> did</div></div>
 <div style="background:{Y};color:{K};border-radius:24px;padding:24px 28px"><div class=d style="font-size:110px">R</div><div style="font-size:36px"><b>Result</b><br>in numbers</div></div></div>
<div class="a" style="left:64px;right:64px;top:1150px;font-size:30px;line-height:1.3;color:#CFC4F2">Amazon: "Always answer the interview questions using the STAR method." Say "I", not "we", and use numbers.</div>""",False))
P=f"""Act as a tough interviewer for a {H('[job title]')} role at {H('[company / industry]')}.<br><br>Ask me 5 behavioural questions, one at a time. After each answer, score it 1&ndash;10 for each STAR part and tell me: {H('what was missing')}, where I said "we" instead of "I", and {H('which number would make it stronger')}.<br><br>Then rewrite my weakest answer in under 90 seconds of speaking."""
S.append((f"""<div class="a m" style="left:64px;top:118px;font-size:26px;letter-spacing:3px;color:{Y}">THE PROMPT &middot; COPY IT</div>
<div class="a d" style="left:64px;right:64px;top:160px;font-size:72px">Practice until it sounds easy</div>
<div class=a style="left:64px;right:64px;top:350px;background:#170A36;border:3px solid {Y};border-radius:24px;overflow:hidden">
 <div style="display:flex;gap:10px;align-items:center;padding:16px 24px;border-bottom:2px solid #3B2A70"><i style="width:18px;height:18px;border-radius:9px;background:#FF5F57;display:inline-block"></i><i style="width:18px;height:18px;border-radius:9px;background:#FEBC2E;display:inline-block"></i><i style="width:18px;height:18px;border-radius:9px;background:#28C840;display:inline-block"></i><span class=m style="color:{Y};font-size:22px;margin-left:12px">ChatGPT / Claude / Gemini</span></div>
 <div style="font-family:MonoR;font-size:34px;line-height:1.45;padding:26px 30px">{P}</div></div>
<div class="a" style="left:64px;right:64px;top:1150px;font-size:31px;line-height:1.3"><b style="color:{Y}">Pro move:</b> use voice mode and answer out loud. Interviews are spoken, not typed.</div>""",False))
S.append((f"""<div class=a style="right:-220px;top:1020px;width:560px;height:560px;border-radius:50%;background:{Y}"></div>
<div class="a" style="left:64px;top:118px"><span class=m style="font-size:22px;letter-spacing:2px;background:{K};color:{Y};padding:8px 16px;border-radius:30px">SCREENSHOT THIS</span></div>
<div class="a d" style="left:64px;right:64px;top:180px;font-size:88px">Every answer, every time</div>
<div class=a style="left:64px;right:64px;top:400px;display:flex;flex-direction:column;gap:20px;font-size:42px;line-height:1.25">
 <div><b>S</b> &middot; 1 line of context. No life story.</div>
 <div><b>T</b> &middot; What you had to fix or win.</div>
 <div><b>A</b> &middot; 2&ndash;3 things <u>you</u> did. Say "I".</div>
 <div><b>R</b> &middot; A number: %, &#8377;/$, hours, users.</div>
 <div><b>+</b> &middot; What you'd do better next time.</div></div>
<div class="a d" style="left:64px;right:64px;top:900px;font-size:66px">Send this to the friend with an interview this week.</div>
<div class="a" style="left:64px;top:1080px"><span class=d style="font-size:56px;background:{K};color:{Y};padding:6px 22px;border-radius:14px;letter-spacing:-1px">Save this + follow @theaikhabari</span></div>
<div class="a m" style="left:64px;right:64px;top:1200px;font-size:18px;color:#5A4E80">Quote: Amazon, "Interview tips" (aboutamazon.com). Prompt and tips are ours.</div>""",True))
N=len(S)
with sync_playwright() as p:
    b=p.chromium.launch(args=['--allow-file-access-from-files'])
    for i,(body,light) in enumerate(S,1):
        open(f'{OUT}/s{i}.html','w').write(page(i,N,body,light))
        pg=b.new_page(viewport={'width':1080,'height':1350});pg.goto(f'file://{OUT}/s{i}.html');pg.wait_for_timeout(600)
        pg.screenshot(path=f'{OUT}/slide{i}.jpg',type='jpeg',quality=93)
print('ok',N)
