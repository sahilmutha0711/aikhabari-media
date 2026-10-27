from playwright.sync_api import sync_playwright
import re
F='file:///mnt/skills/examples/canvas-design/canvas-fonts/'
OUT='/home/claude/car/maang'
CSS=f"""
@font-face{{font-family:Disp;src:url('{F}BricolageGrotesque-Bold.ttf')}}
@font-face{{font-family:Ser;src:url('{F}InstrumentSerif-Italic.ttf')}}
@font-face{{font-family:Mono;font-weight:700;src:url('{F}JetBrainsMono-Bold.ttf')}}
@font-face{{font-family:Mono;src:url('{F}JetBrainsMono-Regular.ttf')}}
@font-face{{font-family:Sans;src:url('{F}InstrumentSans-Regular.ttf')}}
@font-face{{font-family:Sans;font-weight:700;src:url('{F}InstrumentSans-Bold.ttf')}}
:root{{--bg:#5B21D6;--lime:#D4FF3F;--ink:#0B0D1A}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;overflow:hidden;color:#fff;font-family:Sans;position:relative;
background:radial-gradient(700px 600px at 85% 10%,#7B47F0,transparent 70%),radial-gradient(800px 700px at 0% 100%,#3D0FA8,transparent 70%),var(--bg)}}
.a{{position:absolute}}.d{{font-family:Disp;letter-spacing:-2px;line-height:1.0}}.s{{font-family:Ser}}.m{{font-family:Mono}}
.ghost{{position:absolute;border-radius:30px;background:rgba(255,255,255,.07)}}
.top{{position:absolute;left:64px;right:64px;top:52px;display:flex;justify-content:space-between;font-family:Mono;font-weight:700;font-size:22px;letter-spacing:3px}}
.bot{{position:absolute;left:64px;right:64px;bottom:44px;display:flex;justify-content:space-between;font-family:Mono;font-weight:700;font-size:22px}}
.win{{border-radius:30px;background:#171717;box-shadow:0 40px 90px rgba(5,10,60,.55);overflow:hidden}}
.bar{{height:62px;display:flex;align-items:center;gap:12px;padding:0 26px;border-bottom:1px solid #2A2A2A}}
.dot{{width:16px;height:16px;border-radius:50%}}
.ub{{margin-left:auto;max-width:860px;background:#2F2F2F;border-radius:30px 30px 8px 30px;padding:24px 30px;font-size:40px;line-height:1.38;color:#F2F2F2}}
.card{{}}
.ub mark{{background:none;color:var(--lime);font-weight:700}}
.inp{{border-radius:40px;background:#2A2A2A;padding:22px 28px;font-size:38px;color:#9A9A9A;display:flex;align-items:center;gap:16px}}
.tag{{font-family:Mono;font-weight:700;font-size:20px;letter-spacing:2px;padding:6px 14px;border-radius:30px}}
"""
GH='''<div class=ghost style="left:-60px;top:250px;width:420px;height:110px"></div><div class=ghost style="right:-80px;top:420px;width:520px;height:110px"></div><div class=ghost style="left:-40px;top:1040px;width:380px;height:100px"></div><div class=ghost style="right:-60px;top:1160px;width:460px;height:100px"></div>'''
def page(n,N,body,light=False):
    c='#0B0D1A' if light else '#fff'
    bg='style="background:radial-gradient(700px 600px at 85% 10%,#E6FF85,transparent 70%),var(--lime);color:#0B0D1A"' if light else ''
    return f"""<html><head><meta charset=utf-8><style>{CSS}</style></head><body {bg}>{'' if light else GH}{body}
<div class=top style="color:{c}"><span><span style="color:{'#5B21D6' if light else 'var(--lime)'}">&#9679;</span> THE AI KHABARI</span><span>{n} / {N}</span></div>
<div class=bot style="color:{c}"><span>@theaikhabari</span><span>{'SAVE THIS' if n==N else 'SWIPE &rarr;'}</span></div></body></html>"""
hl=lambda s:re.sub(r'\[\[(.+?)\]\]',r'<mark>\1</mark>',s)
def win(inner,label='chat'):
    return f'''<div class=win><div class=bar><div class=dot style="background:#FF5F57"></div><div class=dot style="background:#FEBC2E"></div><div class=dot style="background:#28C840"></div><span class=m style="margin-left:14px;font-size:20px;color:#8A8A8A">{label}</span><span class=m style="margin-left:auto;font-size:16px;letter-spacing:2px;color:#6A6A6A">ILLUSTRATION</span></div><div style="padding:28px 30px 30px">{inner}</div></div>'''
def swap(i,label,bad,good,why):
    inner=f'''<div class=inp style="margin-bottom:26px"><span class=tag style="background:#FF5A5A;color:#fff">STOP</span><s style="color:#B5B5B5">{bad}</s></div>
<div style="display:flex;justify-content:flex-end;margin-bottom:12px"><span class=tag style="background:var(--lime);color:#0B0D1A">TYPE THIS INSTEAD</span></div>
<div class=ub>{hl(good)}</div>
<div style="display:flex;gap:16px;align-items:center;margin-top:26px;color:#9A9A9A;font-size:32px"><div style="width:46px;height:46px;border-radius:50%;background:#fff;flex:none"></div><span style="letter-spacing:6px;font-size:40px">&bull;&bull;&bull;</span></div>'''
    return f'''<div class="a" style="left:64px;top:120px;display:flex;align-items:center;gap:22px"><div class=d style="font-size:120px;color:var(--lime)">{i}</div><div class=d style="font-size:64px;letter-spacing:-1px">{label}</div></div>
<div class=a style="left:48px;right:48px;top:290px"><div style="transform:rotate(-1deg)">{win(inner)}</div><div style="margin:56px 16px 0;font-size:44px;line-height:1.3">{why[0]}</div></div>'''
S=[]
cover_win=win("""<div class=ub style="margin-bottom:22px"><s style="color:#9A9A9A">help me get a job at google</s></div>
<div style="display:flex;gap:14px;align-items:center;color:#9A9A9A;font-size:30px"><div style="width:44px;height:44px;border-radius:50%;background:#fff"></div><span>Sure! Here are some general tips...</span></div>""",'chat')
S.append((f"""<div class="a m" style="left:64px;top:130px;font-size:24px;font-weight:700;letter-spacing:4px;color:var(--lime)">GOOGLE · AMAZON · META · APPLE · NETFLIX</div>
<div class="a d" style="left:64px;right:40px;top:185px;font-size:130px;letter-spacing:-5px">Applying to big tech?</div>
<div class="a d" style="left:64px;right:40px;top:470px;font-size:96px;letter-spacing:-4px"><span style="background:var(--lime);color:#0B0D1A;padding:0 16px;border-radius:14px">Type these 6 prompts</span></div>
<div class=a style="left:110px;right:70px;top:760px;transform:rotate(2deg)">{cover_win}</div>
<div class="a s" style="left:64px;right:64px;top:1080px;font-size:70px;line-height:1.05">Prompt 3 is built on how <span style="color:var(--lime)">Amazon says it grades you</span>.</div>""",False))
S.append((swap(1,"Google's X-Y-Z resume formula",'Improve my resume bullets.','Rewrite each bullet in my resume as [[\"Accomplished X, as measured by Y, by doing Z\"]]. Put the number first. If a bullet has no number, [[ask me for one. Never invent it.]]',('This is the format Google\'s former HR chief Laszlo Bock recommends. <b style="color:var(--lime)">Results first, proof second.</b>',985)),False))
S.append((swap(2,'Speak the job post\'s language','Tailor my resume to this job.','Here is the [[job post for (role) at (company)]]. Pull out its exact tech names, scale and ownership words. Reorder my bullets so [[the best match comes first]], and list anything I\'m missing.',('Big-tech recruiters skim fast. <b style="color:var(--lime)">Mirror their exact words</b> and lead with your strongest match.',985)),False))
S.append((swap(3,'Amazon\'s story bank','Help me prep for Amazon.','From my resume, write one STAR story (Situation, Task, Action, Result) for each of the [[6 Amazon Leadership Principles most relevant to (role)]]. Use "I", not "we". [[End every story with a number.]]',('Amazon\'s own guide says interviews are judged on its Leadership Principles, with STAR answers, <b style="color:var(--lime)">"I" statements and data</b>.',935)),False))
S.append((swap(4,'A mock interview that grades you','Give me interview tips.','Act as a [[(company) interviewer for (role)]]. Ask one behavioral question, wait for my answer, then grade it on: my own actions, a measurable result, what I learned. [[Then ask a tough follow-up.]]',('Real interviewers dig deeper on follow-ups. <b style="color:var(--lime)">Practise the second question</b>, not just the first.',935)),False))
S.append((swap(5,'Find your gaps before they do','Is my resume good enough?','What does [[(company) value that others don\'t]]? Compare that to my resume: give me my 3 strongest proofs and [[my 3 weakest gaps, with a fix for each]].',('Each company screens for different things. <b style="color:var(--lime)">Know your gaps</b> before the recruiter spots them.',935)),False))
S.append((swap(6,'The message that gets replies','Write a referral request.','Write a 5-line LinkedIn message to an engineer at [[(company)]] I don\'t know. Mention [[one specific thing they built or wrote]], one line on my best result, and ask for 15 minutes of advice, not a referral.',('Asking for advice, not a favour, makes it <b style="color:var(--lime)">easy to say yes</b>. Referrals follow conversations.',935)),False))
S.append(("""<div class="a" style="left:64px;top:118px"><span class=tag style="background:var(--lime);color:#0B0D1A">SCREENSHOT THIS</span></div>
<div class="a d" style="left:64px;right:64px;top:180px;font-size:104px;letter-spacing:-3px">What each company looks for</div>
<div class=a style="left:64px;right:64px;top:440px;display:flex;flex-direction:column;gap:20px">
 <div class=card style="background:rgba(255,255,255,.1);border-radius:22px;padding:24px 30px;display:flex;gap:24px;align-items:center"><b class=d style="font-size:54px;width:250px;color:var(--lime)">Google</b><span style="font-size:38px">Scale and systems thinking</span></div>
 <div class=card style="background:rgba(255,255,255,.1);border-radius:22px;padding:24px 30px;display:flex;gap:24px;align-items:center"><b class=d style="font-size:54px;width:250px;color:var(--lime)">Amazon</b><span style="font-size:38px">Ownership and data (Leadership Principles)</span></div>
 <div class=card style="background:rgba(255,255,255,.1);border-radius:22px;padding:24px 30px;display:flex;gap:24px;align-items:center"><b class=d style="font-size:54px;width:250px;color:var(--lime)">Meta</b><span style="font-size:38px">Product impact and speed</span></div>
 <div class=card style="background:rgba(255,255,255,.1);border-radius:22px;padding:24px 30px;display:flex;gap:24px;align-items:center"><b class=d style="font-size:54px;width:250px;color:var(--lime)">Apple</b><span style="font-size:38px">Craft and technical depth</span></div>
 <div class=card style="background:rgba(255,255,255,.1);border-radius:22px;padding:24px 30px;display:flex;gap:24px;align-items:center"><b class=d style="font-size:54px;width:250px;color:var(--lime)">Netflix</b><span style="font-size:38px">Independent judgment</span></div></div>
<div class="a m" style="left:64px;right:64px;top:1180px;font-size:22px;opacity:.8">Per Enhancv's FAANG resume guide; Amazon interview guide (aboutamazon.com).</div>""",False))
S.append(("""<div class="a d" style="left:64px;right:64px;top:170px;font-size:120px;letter-spacing:-4px">Save this before you apply</div>
<div class="a s" style="left:64px;right:64px;top:600px;font-size:66px">Send it to the friend applying to Google, Amazon or Meta <span style="background:#0B0D1A;color:var(--lime);padding:0 12px">this month</span>.</div>
<div class="a" style="left:64px;right:64px;top:860px;font-size:40px;line-height:1.4">Swap the (brackets) for your details. Never let AI invent experience: recruiters check.</div>
<div class="a d" style="left:64px;top:1120px;font-size:64px;letter-spacing:-1px">Follow @theaikhabari</div>""",True))
N=len(S)
with sync_playwright() as p:
    b=p.chromium.launch(args=['--allow-file-access-from-files'])
    for i,(body,light) in enumerate(S,1):
        open(f'{OUT}/s{i}.html','w').write(page(i,N,body,light))
        pg=b.new_page(viewport={'width':1080,'height':1350});pg.goto(f'file://{OUT}/s{i}.html');pg.wait_for_timeout(600)
        pg.screenshot(path=f'{OUT}/slide{i}.jpg',type='jpeg',quality=92);pg.close()
    b.close()
from PIL import Image
ims=[Image.open(f'{OUT}/slide{i}.jpg').resize((540,675)) for i in range(1,N+1)]
s=Image.new('RGB',(540*5,675*2),'white')
for i,im in enumerate(ims): s.paste(im,((i%5)*540,(i//5)*675))
s.save('/tmp/claude-0/maang_sheet.jpg',quality=85);print('ok',N)
