from playwright.sync_api import sync_playwright
import re
F='file:///mnt/skills/examples/canvas-design/canvas-fonts/'
OUT='/home/claude/car/jobs'
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
cover_win=win("""<div class=ub style="margin-bottom:22px"><s style="color:#9A9A9A">write me a cover letter</s></div>
<div style="display:flex;gap:14px;align-items:center;color:#9A9A9A;font-size:30px"><div style="width:44px;height:44px;border-radius:50%;background:#fff"></div><span>Dear Hiring Manager, I am excited to apply...</span></div>""",'chat')
S.append((f"""<div class="a m" style="left:64px;top:130px;font-size:24px;font-weight:700;letter-spacing:4px;color:var(--lime)">JOB HUNTING? SAVE THIS</div>
<div class="a d" style="left:64px;right:40px;top:185px;font-size:140px;letter-spacing:-5px">6 ChatGPT prompts every <span style="background:var(--lime);color:#0B0D1A;padding:0 14px;border-radius:14px">job hunter</span> needs</div>
<div class=a style="left:110px;right:70px;top:760px;transform:rotate(2deg)">{cover_win}</div>
<div class="a s" style="left:64px;right:64px;top:1080px;font-size:70px;line-height:1.05">Number 4 is the question recruiters <span style="color:var(--lime)">won't answer</span> for you.</div>""",False))
S.append((swap(1,'Tailor your resume','Make my resume better.','Here is the job post and my resume. List the 5 skills they care about most, then rewrite my top 3 bullets to prove them [[with real numbers. Don\'t invent anything.]]',('Recruiters scan for <b style="color:var(--lime)">their own words</b>. This puts them in your resume, honestly.',985)),False))
S.append((swap(2,'A cover letter that\'s not generic','Write me a cover letter.','Write a 3-sentence opening that connects [[my one best achievement]] to [[a goal mentioned in this job post]]. No "I am excited to apply".',('Hiring managers stop reading at <b style="color:var(--lime)">"I am excited to apply"</b>. Lead with proof instead.',935)),False))
S.append((swap(3,'Interview practice','Give me interview tips.','Act as the hiring manager for this role. [[Ask me one tough question at a time]], wait for my answer, then score it out of 10 and tell me how to improve it.',('Tips are easy to forget. <b style="color:var(--lime)">Practising out loud</b> is what actually sticks.',935)),False))
S.append((swap(4,'The question recruiters won\'t answer','Is my resume good?','Compare my resume to this job post. [[What would make a recruiter reject me in 6 seconds?]] List the top 3 reasons and how to fix each.',('Most rejections come with no feedback. <b style="color:var(--lime)">Ask the brutal version</b> before you apply.',935)),False))
S.append((swap(5,'The follow-up','Write a thank-you email.','Write a 4-line follow-up email to [[name]] after today\'s interview. Mention [[one thing we discussed]] and end with one short question.',('A specific follow-up <b style="color:var(--lime)">reminds them who you are</b>. Generic ones get skimmed.',935)),False))
tmpl="""<div class=m style="font-size:32px;line-height:1.6;color:#F2F2F2">Here is the job post: <span style="color:var(--lime)">[paste]</span><br>Here is my resume: <span style="color:var(--lime)">[paste]</span><br>Act as the <span style="color:var(--lime)">[hiring manager]</span>.<br>Tell me <span style="color:var(--lime)">[what to fix]</span>,<br>then <span style="color:var(--lime)">[rewrite / quiz me / score me]</span>.<br>Never invent experience.</div>"""
S.append((f"""<div class="a" style="left:64px;top:118px"><span class=tag style="background:#0B0D1A;color:var(--lime)">SCREENSHOT THIS</span></div>
<div class="a d" style="left:64px;right:64px;top:175px;font-size:96px;letter-spacing:-3px">One template for every application</div>
<div class=a style="left:48px;right:48px;top:420px">{win(tmpl,'copy me')}</div>
<div class="a s" style="left:64px;right:64px;top:930px;font-size:58px">Save this. Send it to the friend who's job hunting <span style="background:#0B0D1A;color:var(--lime);padding:0 12px">right now</span>.</div>
<div class="a d" style="left:64px;top:1130px;font-size:56px;letter-spacing:-1px">Follow @theaikhabari for daily AI you can use</div>""",True))
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
s=Image.new('RGB',(540*4,675*2),'white')
for i,im in enumerate(ims): s.paste(im,((i%4)*540,(i//4)*675))
s.save('/tmp/claude-0/jobs_sheet.jpg',quality=85);print('ok',N)
