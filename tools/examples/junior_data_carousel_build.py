from playwright.sync_api import sync_playwright
import re
F='file:///mnt/skills/examples/canvas-design/canvas-fonts/'
OUT='/home/claude/car/junior'
CSS=f"""
@font-face{{font-family:Disp;src:url('{F}BricolageGrotesque-Bold.ttf')}}
@font-face{{font-family:Ser;src:url('{F}InstrumentSerif-Italic.ttf')}}
@font-face{{font-family:Mono;font-weight:700;src:url('{F}JetBrainsMono-Bold.ttf')}}
@font-face{{font-family:Mono;src:url('{F}JetBrainsMono-Regular.ttf')}}
@font-face{{font-family:Sans;src:url('{F}InstrumentSans-Regular.ttf')}}
@font-face{{font-family:Sans;font-weight:700;src:url('{F}InstrumentSans-Bold.ttf')}}
:root{{--bg:#1F5BFF;--acc:#9FD0FF;--ink:#0A1240}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;overflow:hidden;color:#fff;font-family:Sans;position:relative;
background:radial-gradient(900px 800px at 100% 0%,#4F86FF,transparent 70%),radial-gradient(900px 800px at 0% 100%,#1238D6,transparent 70%),var(--bg)}}
body:before{{content:'';position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.07) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.07) 1px,transparent 1px);background-size:54px 54px}}
.a{{position:absolute}}.d{{font-family:Disp;letter-spacing:-2px;line-height:1.0}}.s{{font-family:Ser}}.m{{font-family:Mono}}
.top{{position:absolute;left:64px;right:64px;top:52px;display:flex;justify-content:space-between;font-family:Mono;font-weight:700;font-size:22px;letter-spacing:3px}}
.bot{{position:absolute;left:64px;right:64px;bottom:44px;display:flex;justify-content:space-between;font-family:Mono;font-weight:700;font-size:22px}}
.win{{border-radius:26px;background:#0B1230;border:2px solid #2B3A7A;box-shadow:0 40px 90px rgba(0,10,60,.5);overflow:hidden}}
.bar{{height:58px;display:flex;align-items:center;gap:12px;padding:0 24px;border-bottom:1px solid #2B3A7A;background:#0E1740}}
.dot{{width:15px;height:15px;border-radius:50%}}
.p{{font-family:Mono;font-size:38px;line-height:1.5;color:#E6EDF3}}
.p mark{{background:none;color:#7CC4FF;font-weight:700}}
.tag{{font-family:Mono;font-weight:700;font-size:20px;letter-spacing:2px;padding:6px 14px;border-radius:30px}}
.co{{display:inline-block;font-family:Disp;font-size:74px;letter-spacing:-1px;padding:6px 28px;border-radius:18px;background:#0A1240;color:#fff}}
"""
def page(n,N,body,blue=False):
    bg='style="background:#FFFFFF;color:#0A1240"' if blue else ''
    return f"""<html><head><meta charset=utf-8><style>{CSS}</style></head><body {bg}>{body}
<div class=top style="color:{'#0A1240' if blue else '#fff'}"><span><span style="color:{'#1F5BFF' if blue else '#fff'}">&#9679;</span> THE AI KHABARI</span><span>{n} / {N}</span></div>
<div class=bot style="color:{'#0A1240' if blue else '#fff'}"><span>@theaikhabari</span><span>{'SAVE THIS' if n==N else 'SWIPE &rarr;'}</span></div></body></html>"""
hl=lambda s:re.sub(r'\[\[(.+?)\]\]',r'<mark>\1</mark>',s)
def win(inner,label):
    return f'''<div class=win><div class=bar><div class=dot style="background:#FF5F57"></div><div class=dot style="background:#FEBC2E"></div><div class=dot style="background:#28C840"></div><span class=m style="margin-left:12px;font-size:20px;color:#7D8590">{label}</span><span class=m style="margin-left:auto;font-size:15px;letter-spacing:2px;color:#56606C">COPY &amp; PASTE</span></div><div style="padding:30px 34px">{inner}</div></div>'''
def P(i,co,title,prompt,why,ytop=930):
    return f'''<div class="a" style="left:64px;top:118px;display:flex;align-items:center;gap:22px"><div class=d style="font-size:120px;background:#fff;color:#1F5BFF;border-radius:24px;padding:0 26px">{i}</div><div><div class=m style="font-size:24px;font-weight:700;letter-spacing:3px;color:#DCEBFF">{co}</div><div class=d style="font-size:62px;letter-spacing:-1px">{title}</div></div></div>
<div class=a style="left:48px;right:48px;top:300px">{win('<div class=p>'+hl(prompt)+'</div>','prompt.txt')}<div style="margin:50px 16px 0;font-size:42px;line-height:1.32">{why}</div></div>'''
S=[]
def big(n,label,y,sz=230):
    return f'<div class=a style="left:64px;right:64px;top:{y}px"><div class=d style="font-size:{sz}px;letter-spacing:-8px">{n}</div><div style="font-size:40px;margin-top:6px;color:#DCEBFF">{label}</div></div>'
def card(t,b):
    return f'<div style="background:#0B1230;border:2px solid #2B3A7A;border-radius:22px;padding:26px 30px"><div class=d style="font-size:52px;color:#7CC4FF">{t}</div><div style="font-size:36px;line-height:1.35;margin-top:8px">{b}</div></div>'
S.append(("""<div class="a m" style="left:64px;top:128px;font-size:28px;font-weight:700;letter-spacing:3px;color:#DCEBFF">JUNIOR DEVELOPERS, READ THIS</div>
<div class="a d" style="left:64px;right:40px;top:185px;font-size:100px;letter-spacing:-4px">The company behind Claude just shared its own hiring data</div>
<div class=a style="left:64px;right:64px;top:560px;background:#0B1230;border-radius:30px;padding:40px 44px;border:2px solid #2B3A7A">
 <div class=m style="font-size:26px;font-weight:700;letter-spacing:3px;color:#7CC4FF">JUNIOR SHARE OF ANTHROPIC'S TECH HIRES</div>
 <div style="display:flex;align-items:center;gap:30px;margin-top:10px"><span class=d style="font-size:190px;letter-spacing:-8px;color:#8A97C8"><s>27%</s></span><span class=d style="font-size:100px">&rarr;</span><span class=d style="font-size:190px;letter-spacing:-8px;background:#fff;color:#1F5BFF;border-radius:24px;padding:0 20px">9%</span></div></div>
<div class="a s" style="left:64px;right:64px;top:1080px;font-size:64px;line-height:1.05">And what they look for now has changed. Swipe.</div>""",False))
S.append((f"""<div class="a m" style="left:64px;top:128px;font-size:26px;font-weight:700;letter-spacing:3px;color:#DCEBFF">THE NUMBERS (SINCE EARLY 2025)</div>
{big('27% &rarr; 9%','junior share of new technical hires',190,190)}
{big('21% &rarr; 14%','junior share of technical staff',520,190)}
{big('~3&times;','company headcount grew, but juniors did not keep up',850,190)}""",False))
S.append((f"""<div class="a m" style="left:64px;top:128px;font-size:26px;font-weight:700;letter-spacing:3px;color:#DCEBFF">WHY: THE AGENTS</div>
{big('6&times;','agents ran 6x the hours of the humans directing them (by August)',190,260)}
{big('5&times;','code commits per engineer vs six months earlier',640,260)}
<div class="a" style="left:64px;right:64px;top:1080px;font-size:34px;line-height:1.35;color:#DCEBFF">Agent hours = runtime of AI agents in employee-directed sessions. Human hours = headcount &times; 40 h/week. (Anthropic's definitions)</div>""",False))
S.append((f"""<div class="a m" style="left:64px;top:128px;font-size:26px;font-weight:700;letter-spacing:3px;color:#DCEBFF">WHAT INTERVIEWERS NOW NOTICE</div>
<div class="a d" style="left:64px;right:64px;top:180px;font-size:96px;letter-spacing:-3px">The skills that went <span style="background:#fff;color:#1F5BFF;padding:0 14px;border-radius:12px">up</span></div>
<div class=a style="left:64px;right:64px;top:470px;display:flex;flex-direction:column;gap:22px">
{card('Autonomy &amp; judgment','Rose the most in interviewer comments for technical candidates.')}
{card('Creative use of AI tools','Comments on it tripled for technical roles (from ~5% in 2024).')}
{card('Domain expertise alone','Shrank as a share of what interviewers wrote about.')}</div>""",False))
S.append((f"""<div class="a m" style="left:64px;top:128px;font-size:26px;font-weight:700;letter-spacing:3px;color:#DCEBFF">THE NEW JOB</div>
<div class="a d" style="left:64px;right:64px;top:180px;font-size:92px;letter-spacing:-3px">Engineers are becoming <span style="background:#fff;color:#1F5BFF;padding:0 14px;border-radius:12px">managers of agents</span></div>
{big('10% &rarr; 22%','of Claude sessions were "meta-work": building agent tools and supervising pipelines (fall 2025 to spring 2026)',700,190)}""",False))
S.append((f"""<div class="a" style="left:64px;top:128px"><span class=tag style="background:#FF5A5F;color:#fff">THE CATCH</span></div>
<div class="a d" style="left:64px;right:64px;top:190px;font-size:110px;letter-spacing:-4px">Don't panic yet</div>
<div class=a style="left:64px;right:64px;top:420px;display:flex;flex-direction:column;gap:22px">
{card('One company','Anthropic builds AI, so it adopts agents faster than most. Its own authors say results may not generalise.')}
{card('Cause is unclear','The company also tripled in size. The report says AI is a big factor, not the only one.')}
{card('Still hiring','Juniors are a smaller share, not zero. The bar moved, it did not close.')}</div>""",False))
S.append((f"""<div class="a" style="left:64px;top:118px"><span class=tag style="background:#fff;color:#1F5BFF">SCREENSHOT THIS</span></div>
<div class="a d" style="left:64px;right:64px;top:170px;font-size:84px;letter-spacing:-3px">If you're a junior dev, do this</div>
<div class=a style="left:64px;right:64px;top:380px;display:flex;flex-direction:column;gap:16px">
{card('1 · Ship with agents','Build a project with AI agents and write up how you reviewed and tested their code.')}
{card('2 · Show judgment','In interviews, explain a time you did NOT trust the AI output, and why.')}
{card('3 · Learn the meta-work','Tests, evals, code review, agent tooling: the work that is growing.')}
{card('4 · Own it end to end','Bring stories where you took a problem from vague to shipped, alone.')}</div>""",False))
S.append(("""<div class="a d" style="left:64px;right:64px;top:170px;font-size:120px;letter-spacing:-4px;color:#1F5BFF">Save this. The bar just moved.</div>
<div class="a s" style="left:64px;right:64px;top:460px;font-size:66px;color:#0B1020">Send it to your friend graduating in CS this year.</div>
<div class="a" style="left:64px;right:64px;top:720px;font-size:38px;line-height:1.4;color:#0B1020">Source: "How employment is changing at Anthropic", Anthropic research, Oct 16, 2026. Figures are Anthropic's internal data.</div>
<div class="a d" style="left:64px;top:1080px;font-size:66px;letter-spacing:-1px;color:#1F5BFF">Follow @theaikhabari</div>""",True))
N=len(S)
with sync_playwright() as p:
    b=p.chromium.launch(args=['--allow-file-access-from-files'])
    for i,(body,blue) in enumerate(S,1):
        open(f'{OUT}/s{i}.html','w').write(page(i,N,body,blue))
        pg=b.new_page(viewport={'width':1080,'height':1350});pg.goto(f'file://{OUT}/s{i}.html');pg.wait_for_timeout(600)
        pg.screenshot(path=f'{OUT}/slide{i}.jpg',type='jpeg',quality=92);pg.close()
    b.close()
from PIL import Image
ims=[Image.open(f'{OUT}/slide{i}.jpg').resize((540,675)) for i in range(1,N+1)]
s=Image.new('RGB',(540*4,675*2),'white')
for i,im in enumerate(ims): s.paste(im,((i%4)*540,(i//4)*675))
s.save('/tmp/claude-0/junior_sheet.jpg',quality=85);print('ok',N)
