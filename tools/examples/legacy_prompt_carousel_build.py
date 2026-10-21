from playwright.sync_api import sync_playwright
F='file:///mnt/skills/examples/canvas-design/canvas-fonts/'
OUT='/home/claude/car/legacy'
CSS=f"""
@font-face{{font-family:Disp;src:url('{F}BricolageGrotesque-Bold.ttf')}}
@font-face{{font-family:Ser;src:url('{F}InstrumentSerif-Italic.ttf')}}
@font-face{{font-family:Mono;font-weight:700;src:url('{F}JetBrainsMono-Bold.ttf')}}
@font-face{{font-family:Sans;src:url('{F}InstrumentSans-Regular.ttf')}}
@font-face{{font-family:Sans;font-weight:700;src:url('{F}InstrumentSans-Bold.ttf')}}
:root{{--bg:#F4EFE6;--ink:#14161A}}
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
    st='style="background:#14161A;color:#F4EFE6"' if dark else ''
    return f"""<html><head><meta charset=utf-8><style>{CSS}</style></head><body {st}>{body}
<div class=top><span>&#9679; THE AI KHABARI</span><span>{n} / {N}</span></div>
<div class=bot><span>@theaikhabari</span><span>{'SAVE THIS' if n==N else 'SWIPE &rarr;'}</span></div></body></html>"""
def card(t,b):
    return f'<div class=card><div class=d style="font-size:66px;letter-spacing:-2px">{t}</div><div style="font-size:40px;line-height:1.32;margin-top:10px">{b}</div></div>'

def win(title,prompt):
    return f'<div style="background:#14161A;border-radius:24px;box-shadow:10px 10px 0 #12B76A;overflow:hidden"><div style="display:flex;gap:10px;align-items:center;padding:18px 24px;border-bottom:2px solid #2a2d33"><i style="width:18px;height:18px;border-radius:9px;background:#FF5F57;display:inline-block"></i><i style="width:18px;height:18px;border-radius:9px;background:#FEBC2E;display:inline-block"></i><i style="width:18px;height:18px;border-radius:9px;background:#28C840;display:inline-block"></i><span class=m style="color:#5EE6A0;font-size:22px;margin-left:12px">{title}</span></div><div class=m style="color:#FFF3E6;font-size:39px;line-height:1.4;padding:24px 30px 30px;font-weight:400">{prompt}</div></div>'
H=lambda s:f'<b style="color:#5EE6A0">{s}</b>'
def pslide(k,label,head,prompt,why):
    return f"""<div class=a style="inset:0;background-image:linear-gradient(rgba(20,22,26,.06) 2px,transparent 2px);background-size:100% 60px"></div><div class=a style="left:0;top:0;bottom:0;width:18px;background:#12B76A"></div><div class="a m" style="left:64px;top:118px;font-size:26px;letter-spacing:3px">STEP {k} &middot; {label}</div>
<div class="a d" style="left:64px;right:64px;top:165px;font-size:80px">{head}</div>
<div class=a style="left:64px;right:64px;top:370px">{win('paste into ChatGPT / Claude + the code',prompt)}</div>
<div class="a" style="left:64px;right:64px;top:1150px;font-size:32px;line-height:1.3"><b>Why it works:</b> {why}</div>"""
S=[]
S.append(("""<div class=a style="inset:0;background-image:linear-gradient(rgba(20,22,26,.06) 2px,transparent 2px);background-size:100% 60px"></div>
<div class=a style="right:-220px;top:1000px;width:600px;height:600px;border-radius:50%;background:#12B76A"></div>
<div class="a m" style="left:64px;top:130px;font-size:28px;letter-spacing:3px">SOFTWARE DEVELOPERS: SAVE THIS</div>
<div class="a d" style="left:64px;right:50px;top:185px;font-size:100px">Inherited code nobody understands?</div>
<div class="a s" style="left:64px;right:64px;top:560px;font-size:66px;line-height:1.05">3 AI prompts built on the two legacy-code classics:</div>
<div class=a style="left:64px;right:64px;top:760px;display:flex;flex-direction:column;gap:18px">
 <span class=d style="align-self:flex-start;font-size:46px;background:#14161A;color:#F4EFE6;padding:6px 22px;border-radius:12px">FEATHERS &middot; CHARACTERIZATION TESTS</span>
 <span class=d style="align-self:flex-start;font-size:46px;background:#12B76A;color:#14161A;padding:6px 22px;border-radius:12px">FOWLER &middot; STRANGLER FIG</span></div>""",False))
S.append((pslide(1,'MAP IT','Understand it before you touch it',
f"""You're a staff engineer onboarding me onto this code. Give me: {H('1)')} what it does in 5 lines, {H('2)')} entry points and data flow, {H('3)')} the 3 riskiest functions (most callers, side effects, no tests), {H('4)')} questions for the original authors. Mark anything unclear as {H('UNKNOWN')}. Don't guess.""",
"Writing UNKNOWN instead of guessing stops the AI from inventing how your system works."),False))
S.append((pslide(2,'PIN IT','Lock in what it does today',
f"""Before I change {H('[function]')}, write {H('characterization tests')} that record what it does TODAY, weird cases included. {H("Don't fix bugs")}: assert current behaviour and flag suspected bugs in comments. Cover empty, null, huge and boundary inputs.""",
"Michael Feathers' idea: first pin down current behaviour, then refactor with a safety net."),False))
S.append((pslide(3,'STRANGLE IT','Replace it without a big-bang rewrite',
f"""I want to replace {H('[module]')} gradually using the {H('Strangler Fig')} pattern. Propose: the seam to put a {H('facade')} on, the first small slice to route to new code, how to run old and new {H('side by side and compare outputs')}, and the rollback plan.""",
"Martin Fowler's pattern: grow the new system around the old one until the old one can be switched off."),False))
S.append(("""<div class="a" style="left:64px;top:118px"><span class=tag style="background:#12B76A;color:#14161A">SCREENSHOT THIS</span></div>
<div class="a d" style="left:64px;right:64px;top:180px;font-size:120px;color:#F4EFE6">Map it. Pin it. Strangle it.</div>
<div class="a s" style="left:64px;right:64px;top:520px;font-size:66px;line-height:1.1;color:#5EE6A0">&ldquo;To me, legacy code is simply code without tests.&rdquo;</div>
<div class="a m" style="left:64px;top:700px;font-size:26px;color:#C9CCD3">MICHAEL FEATHERS, WORKING EFFECTIVELY WITH LEGACY CODE</div>
<div class="a d" style="left:64px;right:64px;top:820px;font-size:70px;color:#F4EFE6">Send this to the dev who just got handed the 2009 codebase.</div>
<div class="a" style="left:64px;top:1060px"><span class=d style="font-size:56px;background:#12B76A;color:#14161A;padding:6px 22px;border-radius:14px">Save this + follow @theaikhabari</span></div>
<div class="a m" style="left:64px;right:64px;top:1185px;font-size:18px;color:#8C9099">Sources: M. Feathers (2004); M. Fowler, "Strangler Fig" (martinfowler.com). Prompts are ours. Don't paste secrets or code your company hasn't approved for AI tools.</div>""",True))
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
