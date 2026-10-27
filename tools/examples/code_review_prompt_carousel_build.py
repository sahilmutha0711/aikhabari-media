from playwright.sync_api import sync_playwright
F='file:///mnt/skills/examples/canvas-design/canvas-fonts/'
OUT='/home/claude/car/review'
CSS=f"""
@font-face{{font-family:Disp;src:url('{F}BricolageGrotesque-Bold.ttf')}}
@font-face{{font-family:Ser;src:url('{F}InstrumentSerif-Italic.ttf')}}
@font-face{{font-family:Mono;font-weight:700;src:url('{F}JetBrainsMono-Bold.ttf')}}
@font-face{{font-family:Sans;src:url('{F}InstrumentSans-Regular.ttf')}}
@font-face{{font-family:Sans;font-weight:700;src:url('{F}InstrumentSans-Bold.ttf')}}
:root{{--bg:#FF8A00;--ink:#1C0B00}}
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
    st='style="background:#1C0B00;color:#fff"' if dark else ''
    return f"""<html><head><meta charset=utf-8><style>{CSS}</style></head><body {st}>{body}
<div class=top><span>&#9679; THE AI KHABARI</span><span>{n} / {N}</span></div>
<div class=bot><span>@theaikhabari</span><span>{'SAVE THIS' if n==N else 'SWIPE &rarr;'}</span></div></body></html>"""
def card(t,b):
    return f'<div class=card><div class=d style="font-size:66px;letter-spacing:-2px">{t}</div><div style="font-size:40px;line-height:1.32;margin-top:10px">{b}</div></div>'

def win(title,prompt):
    return f'<div style="background:#1C0B00;border-radius:24px;box-shadow:10px 10px 0 #fff;overflow:hidden"><div style="display:flex;gap:10px;align-items:center;padding:18px 24px;border-bottom:2px solid #4a2a10"><i style="width:18px;height:18px;border-radius:9px;background:#FF5F57;display:inline-block"></i><i style="width:18px;height:18px;border-radius:9px;background:#FEBC2E;display:inline-block"></i><i style="width:18px;height:18px;border-radius:9px;background:#28C840;display:inline-block"></i><span class=m style="color:#FFB866;font-size:22px;margin-left:12px">{title}</span></div><div class=m style="color:#FFF3E6;font-size:39px;line-height:1.4;padding:24px 30px 30px;font-weight:400">{prompt}</div></div>'
H=lambda s:f'<b style="color:#FFB866">{s}</b>'
def pslide(k,label,head,prompt,why):
    return f"""<div class="a m" style="left:64px;top:118px;font-size:26px;letter-spacing:3px">PROMPT {k} &middot; GOOGLE CHECKS: {label}</div>
<div class="a d" style="left:64px;right:64px;top:165px;font-size:80px">{head}</div>
<div class=a style="left:64px;right:64px;top:370px">{win('paste into ChatGPT / Claude + your diff',prompt)}</div>
<div class="a" style="left:64px;right:64px;top:1150px;font-size:32px;line-height:1.3"><b>Why it works:</b> {why}</div>"""
S=[]
S.append(("""<div class="a m" style="left:64px;top:130px;font-size:28px;letter-spacing:3px">SOFTWARE DEVELOPERS: SAVE THIS</div>
<div class="a" style="left:64px;top:190px"><span class=d style="font-size:210px;letter-spacing:-6px;background:#1C0B00;color:#fff;padding:0 30px;border-radius:24px">GOOGLE'S</span></div>
<div class="a d" style="left:64px;right:40px;top:440px;font-size:120px">code review checklist, turned into 3 AI prompts</div>
<div class="a s" style="left:64px;right:64px;top:900px;font-size:76px;line-height:1.05">Review your own PR like a Google reviewer. Before anyone else does.</div>""",False))
S.append((pslide(1,'DESIGN + COMPLEXITY','Catch the big problems first',
f"""Act as a senior reviewer using Google's code review guide. Review this diff for {H('DESIGN first')}: do the parts fit this codebase? Then flag code that {H("can't be understood quickly")} or is {H('over-engineered')} (features we don't need yet). For each issue: file:line, why, smallest fix. Prefix optional ones with {H('"Nit:"')}.""",
"Google calls design the most important thing to cover in a review, so the AI checks it first."),False))
S.append((pslide(2,'FUNCTIONALITY','Find the bug before your users do',
f"""This change is supposed to: {H('[what it should do]')}. Read the diff as the {H('end user')} AND the {H('next developer')}. List the edge cases, {H('race conditions / concurrency risks')} and user-visible behaviour changes it doesn't handle. Rank by severity. Ask me questions if the intent is unclear.""",
"You give the AI the intent, so it checks behaviour, not just syntax."),False))
S.append((pslide(3,'TESTS','Make sure your tests can actually fail',
f"""Write the tests this change is missing ({H('unit first')}, then integration if needed). For each, say {H('which bug it catches')}. Then audit my existing tests: would each one {H('FAIL if the code broke?')} Flag any test that can't fail or only repeats the code.""",
'"Tests do not test themselves." A test that can\'t fail only gives you false confidence.'),False))
S.append(("""<div class="a" style="left:64px;top:118px"><span class=tag style="background:#FF8A00;color:#1C0B00">SCREENSHOT THIS</span></div>
<div class="a d" style="left:64px;right:64px;top:180px;font-size:88px;color:#fff">Google's checklist in 8 lines</div>
<div class=a style="left:64px;right:64px;top:440px;display:grid;grid-template-columns:1fr 1fr;gap:18px 36px;font-size:38px;line-height:1.25;color:#fff">
 <div><b style="color:#FF8A00">Design</b> fits the codebase</div><div><b style="color:#FF8A00">Function</b> serves users</div>
 <div><b style="color:#FF8A00">Complexity</b> no higher than needed</div><div><b style="color:#FF8A00">Tests</b> that would fail</div>
 <div><b style="color:#FF8A00">Names</b> say the purpose</div><div><b style="color:#FF8A00">Comments</b> explain WHY</div>
 <div><b style="color:#FF8A00">Style</b> guide + "Nit:"</div><div><b style="color:#FF8A00">Docs</b> updated</div></div>
<div class="a d" style="left:64px;right:64px;top:870px;font-size:74px;color:#fff">Send this to the dev who opens 2,000-line PRs.</div>
<div class="a" style="left:64px;top:1070px"><span class=d style="font-size:60px;background:#FF8A00;color:#1C0B00;padding:6px 22px;border-radius:14px">Follow @theaikhabari</span></div>
<div class="a m" style="left:64px;right:64px;top:1180px;font-size:19px;color:#FFB866">Source: Google Engineering Practices, "What to look for in a code review" (google.github.io/eng-practices). Prompts are ours.</div>""",True))
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
