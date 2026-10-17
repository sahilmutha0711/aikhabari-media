from playwright.sync_api import sync_playwright
import re
F='file:///mnt/skills/examples/canvas-design/canvas-fonts/'
OUT='/home/claude/car/swe'
CSS=f"""
@font-face{{font-family:Disp;src:url('{F}BricolageGrotesque-Bold.ttf')}}
@font-face{{font-family:Ser;src:url('{F}InstrumentSerif-Italic.ttf')}}
@font-face{{font-family:Mono;font-weight:700;src:url('{F}JetBrainsMono-Bold.ttf')}}
@font-face{{font-family:Mono;src:url('{F}JetBrainsMono-Regular.ttf')}}
@font-face{{font-family:Sans;src:url('{F}InstrumentSans-Regular.ttf')}}
@font-face{{font-family:Sans;font-weight:700;src:url('{F}InstrumentSans-Bold.ttf')}}
:root{{--bg:#0B1020;--acc:#3D8BFF;--ink:#0B1020}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;overflow:hidden;color:#fff;font-family:Sans;position:relative;
background:radial-gradient(800px 700px at 100% 0%,rgba(61,139,255,.45),transparent 70%),radial-gradient(800px 700px at 0% 100%,rgba(0,90,255,.35),transparent 70%),var(--bg)}}
body:before{{content:'';position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.04) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.04) 1px,transparent 1px);background-size:54px 54px}}
.a{{position:absolute}}.d{{font-family:Disp;letter-spacing:-2px;line-height:1.0}}.s{{font-family:Ser}}.m{{font-family:Mono}}
.top{{position:absolute;left:64px;right:64px;top:52px;display:flex;justify-content:space-between;font-family:Mono;font-weight:700;font-size:22px;letter-spacing:3px}}
.bot{{position:absolute;left:64px;right:64px;bottom:44px;display:flex;justify-content:space-between;font-family:Mono;font-weight:700;font-size:22px}}
.win{{border-radius:26px;background:#11161F;border:2px solid #263042;box-shadow:0 40px 90px rgba(0,10,40,.6);overflow:hidden}}
.bar{{height:58px;display:flex;align-items:center;gap:12px;padding:0 24px;border-bottom:1px solid #263042;background:#0E131B}}
.dot{{width:15px;height:15px;border-radius:50%}}
.p{{font-family:Mono;font-size:38px;line-height:1.5;color:#E6EDF3}}
.p mark{{background:none;color:var(--acc);font-weight:700}}
.tag{{font-family:Mono;font-weight:700;font-size:20px;letter-spacing:2px;padding:6px 14px;border-radius:30px}}
.co{{display:inline-block;font-family:Disp;font-size:58px;letter-spacing:0;padding:8px 26px;border-radius:16px;background:#fff;color:#0B1020}}
"""
def page(n,N,body,blue=False):
    bg='style="background:radial-gradient(800px 700px at 100% 0%,#7AB0FF,transparent 70%),var(--acc)"' if blue else ''
    return f"""<html><head><meta charset=utf-8><style>{CSS}</style></head><body {bg}>{body}
<div class=top><span><span style="color:{'#0B1020' if blue else 'var(--acc)'}">&#9679;</span> THE AI KHABARI</span><span>{n} / {N}</span></div>
<div class=bot><span>@theaikhabari</span><span>{'SAVE THIS' if n==N else 'SWIPE &rarr;'}</span></div></body></html>"""
hl=lambda s:re.sub(r'\[\[(.+?)\]\]',r'<mark>\1</mark>',s)
def win(inner,label):
    return f'''<div class=win><div class=bar><div class=dot style="background:#FF5F57"></div><div class=dot style="background:#FEBC2E"></div><div class=dot style="background:#28C840"></div><span class=m style="margin-left:12px;font-size:20px;color:#7D8590">{label}</span><span class=m style="margin-left:auto;font-size:15px;letter-spacing:2px;color:#56606C">COPY &amp; PASTE</span></div><div style="padding:30px 34px">{inner}</div></div>'''
def P(i,co,title,prompt,why,ytop=930):
    return f'''<div class="a" style="left:64px;top:118px;display:flex;align-items:center;gap:22px"><div class=d style="font-size:130px;color:var(--acc)">{i}</div><div><div class=m style="font-size:22px;font-weight:700;letter-spacing:3px;color:var(--acc)">{co}</div><div class=d style="font-size:62px;letter-spacing:-1px">{title}</div></div></div>
<div class=a style="left:48px;right:48px;top:300px">{win('<div class=p>'+hl(prompt)+'</div>','prompt.txt')}<div style="margin:50px 16px 0;font-size:42px;line-height:1.32">{why}</div></div>'''
S=[]
cos=''.join(f'<span class=co style="margin:0 12px 14px 0">{c}</span>' for c in ['META','APPLE','AMAZON','NETFLIX','GOOGLE'])
S.append((f"""<div class="a m" style="left:64px;top:128px;font-size:26px;font-weight:700;letter-spacing:4px;color:var(--acc)">FOR SOFTWARE DEVELOPERS</div>
<div class="a d" style="left:64px;right:50px;top:180px;font-size:104px;letter-spacing:-4px">6 ChatGPT prompts to prep for <span style="background:var(--acc);padding:0 16px;border-radius:14px">MAANG</span> coding interviews</div>
<div class=a style="left:64px;right:30px;top:640px">{cos}</div>
<div class=a style="left:64px;right:64px;top:880px">{win('<div class=p style="font-size:32px"><span style="color:#7D8590">// stop typing</span><br><s style="color:#7D8590">give me leetcode questions</s><br><span style="color:#7D8590">// type this</span><br>run a <mark>45-min Meta-style</mark> mock and <mark>grade me hire / no hire</mark></div>','prompt.txt')}</div>""",False))
S.append((P(1,'ALL MAANG','Your 8-week battle plan','I have [[8 weeks]] before my [[Amazon SDE II]] loop and [[2 hrs/day]]. Build a week-by-week plan covering the most-asked coding patterns (sliding window, two pointers, BFS/DFS, heaps, DP...), system design basics and behavioral stories. Put a [[timed mock every Sunday]] and tell me what to cut if I fall behind.',
 'Most candidates grind random problems. <b style="color:var(--acc)">A plan by pattern</b> covers far more questions in less time.'),False))
S.append((P(2,'GOOGLE','Learn patterns, not answers','Give me one medium problem that uses [[sliding window]]. [[Don\'t show the solution.]] After I explain my approach, ask the clarifying questions a Google interviewer would, push me on time and space complexity, then reveal the optimal pattern and [[2 similar problems to lock it in]].',
 'Interviewers rarely repeat questions. <b style="color:var(--acc)">If you know the pattern</b>, you can solve the version you\'ve never seen.'),False))
S.append((P(3,'META','The real mock interview','Run a [[45-minute Meta-style coding round: 2 problems]]. Interrupt me if I start coding before clarifying inputs and edge cases. At the end, score me on [[communication, problem solving, code quality and testing]], and give a verdict: [[hire, lean hire or no hire]], with the one thing to fix.',
 'Meta rounds are known for <b style="color:var(--acc)">2 problems in one round</b>. Practise the pace, not just the solutions.'),False))
S.append((P(4,'GOOGLE · SENIOR ROLES','System design like an L5','Interview me on [[designing a news feed]] like a Google system design round. Make me start with requirements and [[scale estimates]], then let me drive. Challenge my choices on [[bottlenecks, caching, sharding and trade-offs]]. End with what a senior engineer would have done differently.',
 'Design rounds reward <b style="color:var(--acc)">trade-offs, not buzzwords</b>. This prompt makes you defend every box you draw.'),False))
S.append((P(5,'AMAZON','Survive the Bar Raiser','Turn my project [[(describe it)]] into STAR stories for Amazon\'s [[Ownership and Dive Deep]] principles. Include the technical decision, the option I rejected and why, and [[a metric: latency, cost or users]]. Then ask me [[3 follow-ups a Bar Raiser would ask]].',
 'Amazon\'s own guide says every round checks its Leadership Principles, with <b style="color:var(--acc)">"I" statements and data</b>.'),False))
S.append((P(6,'GOOGLE · APPLE · NETFLIX','A resume that gets the call','Rewrite my project bullets with Google\'s X-Y-Z formula, impact first. Example: [["Cut API p95 latency 40% by adding Redis caching"]]. Flag any bullet a recruiter would skip in 6 seconds. [[Never invent numbers: ask me.]]',
 'Laszlo Bock, Google\'s former HR chief, recommends <b style="color:var(--acc)">"Accomplished X, measured by Y, by doing Z"</b>.'),False))
rows=[('META','2 coding problems per round · speed + communication'),('AMAZON','Leadership Principles in every round · Bar Raiser'),('GOOGLE','Algorithms + "Googleyness & Leadership"'),('APPLE','Team-specific · deep domain knowledge'),('NETFLIX','Senior-heavy · culture of judgment')]
r=''.join(f'<div style="display:flex;gap:24px;align-items:center;background:#11161F;border:2px solid #263042;border-radius:20px;padding:22px 28px"><b class=m style="font-size:30px;width:200px;color:var(--acc)">{a}</b><span style="font-size:34px">{b}</span></div>' for a,b in rows)
S.append((f"""<div class="a" style="left:64px;top:118px"><span class=tag style="background:var(--acc);color:#fff">SCREENSHOT THIS</span></div>
<div class="a d" style="left:64px;right:64px;top:180px;font-size:100px;letter-spacing:-3px">What MAANG tests developers on</div>
<div class=a style="left:64px;right:64px;top:440px;display:flex;flex-direction:column;gap:18px">{r}</div>
<div class="a m" style="left:64px;right:64px;top:1180px;font-size:20px;color:#9BA8B8">Based on company career guides and widely reported candidate experiences. Loops vary by team and level.</div>""",False))
S.append(("""<div class="a d" style="left:64px;right:64px;top:170px;font-size:130px;letter-spacing:-5px;color:#fff">Save this before your next interview</div>
<div class="a s" style="left:64px;right:64px;top:600px;font-size:66px;color:#0B1020">Send it to your dev friend who's still grinding LeetCode at 2am.</div>
<div class="a" style="left:64px;right:64px;top:880px;font-size:38px;line-height:1.4;color:#0B1020">Swap the (brackets) for your role, level and projects. Use AI to practise, never to invent experience.</div>
<div class="a d" style="left:64px;top:1110px;font-size:66px;letter-spacing:-1px;color:#fff">Follow @theaikhabari</div>""",True))
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
s=Image.new('RGB',(540*5,675*2),'white')
for i,im in enumerate(ims): s.paste(im,((i%5)*540,(i//5)*675))
s.save('/tmp/claude-0/swe_sheet.jpg',quality=85);print('ok',N)
