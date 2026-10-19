from playwright.sync_api import sync_playwright
F='file:///mnt/skills/examples/canvas-design/canvas-fonts/'
OUT='/home/claude/car/junior2'
CSS=f"""
@font-face{{font-family:Disp;src:url('{F}BricolageGrotesque-Bold.ttf')}}
@font-face{{font-family:Ser;src:url('{F}InstrumentSerif-Italic.ttf')}}
@font-face{{font-family:Mono;font-weight:700;src:url('{F}JetBrainsMono-Bold.ttf')}}
@font-face{{font-family:Sans;src:url('{F}InstrumentSans-Regular.ttf')}}
@font-face{{font-family:Sans;font-weight:700;src:url('{F}InstrumentSans-Bold.ttf')}}
:root{{--bg:#1BE3A6;--ink:#06231A}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;overflow:hidden;color:var(--ink);font-family:Sans;position:relative;background:var(--bg)}}
.a{{position:absolute}}.d{{font-family:Disp;letter-spacing:-3px;line-height:.98}}.s{{font-family:Ser}}.m{{font-family:Mono;font-weight:700}}
.top{{position:absolute;left:64px;right:64px;top:52px;display:flex;justify-content:space-between;font-family:Mono;font-weight:700;font-size:22px;letter-spacing:3px}}
.bot{{position:absolute;left:64px;right:64px;bottom:44px;display:flex;justify-content:space-between;font-family:Mono;font-weight:700;font-size:22px}}
.box{{background:var(--ink);color:#fff;padding:0 16px;border-radius:12px}}
.card{{background:#fff;border-radius:26px;padding:28px 32px;box-shadow:8px 8px 0 var(--ink)}}
.tag{{font-family:Mono;font-weight:700;font-size:22px;letter-spacing:2px;padding:8px 16px;border-radius:30px;background:var(--ink);color:#fff}}
"""
def page(n,N,body,dark=False):
    st='style="background:#06231A;color:#fff"' if dark else ''
    return f"""<html><head><meta charset=utf-8><style>{CSS}</style></head><body {st}>{body}
<div class=top><span>&#9679; THE AI KHABARI</span><span>{n} / {N}</span></div>
<div class=bot><span>@theaikhabari</span><span>{'SAVE THIS' if n==N else 'SWIPE &rarr;'}</span></div></body></html>"""
def card(t,b):
    return f'<div class=card><div class=d style="font-size:66px;letter-spacing:-2px">{t}</div><div style="font-size:40px;line-height:1.32;margin-top:10px">{b}</div></div>'
S=[]
S.append(("""<div class="a m" style="left:64px;top:130px;font-size:28px;letter-spacing:3px">JUNIOR DEVELOPERS, READ THIS</div>
<div class="a d" style="left:64px;right:50px;top:185px;font-size:88px">The company behind Claude just shared its hiring data</div>
<div class="a" style="left:64px;right:64px;top:560px;font-family:Mono;font-weight:700;font-size:28px;letter-spacing:3px">JUNIOR SHARE OF ANTHROPIC'S TECH HIRES</div>
<div class=a style="left:64px;right:64px;top:610px;display:flex;align-items:center;gap:24px"><span class=d style="font-size:200px;letter-spacing:-8px;opacity:.45"><s>27%</s></span><span class=d style="font-size:100px">&rarr;</span><span class=d style="font-size:200px;letter-spacing:-8px;background:#06231A;color:#fff;border-radius:28px;padding:0 24px">9%</span></div>
<div class="a s" style="left:64px;right:64px;top:1040px;font-size:70px;line-height:1.05">And what they look for now has changed.</div>""",False))
S.append(("""<div class="a m" style="left:64px;top:130px;font-size:26px;letter-spacing:3px">WHAT ANTHROPIC REPORTED (OCT 16)</div>
<div class=a style="left:64px;right:64px;top:190px;display:flex;flex-direction:column;gap:26px">"""+
card('21% &rarr; 14%','junior share of technical staff since early 2025, while the company roughly tripled')+
card('6&times; the hours','AI agents ran 6x the hours of the people directing them by August')+
card('5&times; commits','code commits per engineer vs six months earlier')+"""</div>""",False))
S.append(("""<div class="a m" style="left:64px;top:130px;font-size:26px;letter-spacing:3px">WHAT INTERVIEWERS NOTICE NOW</div>
<div class="a d" style="left:64px;right:64px;top:185px;font-size:96px">Skills <span class=box>up</span> vs skills <span class=box style="background:#fff;color:#06231A">down</span></div>
<div class=a style="left:64px;right:64px;top:420px;display:flex;flex-direction:column;gap:26px">"""+
card('&uarr; Autonomy &amp; judgment','rose the most in interviewer comments for tech candidates')+
card('&uarr; Creative use of AI tools','comments on it tripled for tech roles since 2024')+
card('&darr; Domain expertise alone','a shrinking share of what interviewers wrote about')+"""</div>""",False))
S.append(("""<div class="a" style="left:64px;top:118px"><span class=tag style="background:#1BE3A6;color:#06231A">SCREENSHOT THIS</span></div>
<div class="a d" style="left:64px;right:64px;top:185px;font-size:92px;color:#fff">If you're a junior dev, do this</div>
<div class=a style="left:64px;right:64px;top:420px;display:flex;flex-direction:column;gap:30px;font-size:46px;line-height:1.3;color:#fff">
 <div style="display:flex;gap:26px"><b class=d style="font-size:72px;color:#1BE3A6">1</b><span><b>Ship a project with AI agents</b> and write up how you reviewed and tested their code.</span></div>
 <div style="display:flex;gap:26px"><b class=d style="font-size:72px;color:#1BE3A6">2</b><span><b>Show judgment:</b> bring a story of when you did NOT trust the AI output.</span></div>
 <div style="display:flex;gap:26px"><b class=d style="font-size:72px;color:#1BE3A6">3</b><span><b>Learn the meta-work:</b> tests, evals, code review, agent tooling.</span></div></div>
<div class="a" style="left:64px;right:64px;top:1120px;font-size:30px;line-height:1.35;color:#9FE9D0">The catch: one AI company, and its own report says AI isn't the only cause. The bar moved, it didn't close.</div>""",True))
S.append(("""<div class="a d" style="left:64px;right:64px;top:190px;font-size:130px">Save this. The bar just moved.</div>
<div class="a s" style="left:64px;right:64px;top:720px;font-size:72px;line-height:1.05">Send it to your friend graduating in CS this year.</div>
<div class="a" style="left:64px;right:64px;top:960px"><span class=d style="font-size:76px;background:#06231A;color:#fff;padding:6px 24px;border-radius:16px">Follow @theaikhabari</span></div>
<div class="a m" style="left:64px;right:64px;top:1150px;font-size:20px">Source: "How employment is changing at Anthropic", Anthropic research, Oct 16, 2026.</div>""",False))
N=len(S)
with sync_playwright() as p:
    b=p.chromium.launch(args=['--allow-file-access-from-files'])
    for i,(body,dark) in enumerate(S,1):
        open(f'{OUT}/s{i}.html','w').write(page(i,N,body,dark))
        pg=b.new_page(viewport={'width':1080,'height':1350});pg.goto(f'file://{OUT}/s{i}.html');pg.wait_for_timeout(600)
        pg.screenshot(path=f'{OUT}/slide{i}.jpg',type='jpeg',quality=92);pg.close()
    b.close()
from PIL import Image
ims=[Image.open(f'{OUT}/slide{i}.jpg').resize((432,540)) for i in range(1,N+1)]
s=Image.new('RGB',(432*N,540),'white')
for i,im in enumerate(ims): s.paste(im,(i*432,0))
s.save('/tmp/claude-0/junior2_sheet.jpg',quality=85);print('ok',N)
