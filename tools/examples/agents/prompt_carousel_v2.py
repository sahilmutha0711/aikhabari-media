from playwright.sync_api import sync_playwright
import re
F='file:///mnt/skills/examples/canvas-design/canvas-fonts/'
OUT='/home/claude/car/prompts2'
CSS=f"""
@font-face{{font-family:Disp;src:url('{F}BricolageGrotesque-Bold.ttf')}}
@font-face{{font-family:Ser;src:url('{F}InstrumentSerif-Italic.ttf')}}
@font-face{{font-family:Mono;font-weight:700;src:url('{F}JetBrainsMono-Bold.ttf')}}
@font-face{{font-family:Mono;src:url('{F}JetBrainsMono-Regular.ttf')}}
@font-face{{font-family:Sans;src:url('{F}InstrumentSans-Regular.ttf')}}
@font-face{{font-family:Sans;font-weight:700;src:url('{F}InstrumentSans-Bold.ttf')}}
:root{{--bg:#2340F5;--lime:#D4FF3F;--ink:#0B0D1A}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;overflow:hidden;color:#fff;font-family:Sans;position:relative;
background:radial-gradient(700px 600px at 85% 10%,#4D6BFF,transparent 70%),radial-gradient(800px 700px at 0% 100%,#1426B8,transparent 70%),var(--bg)}}
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
<div class=top style="color:{c}"><span><span style="color:{'#2340F5' if light else 'var(--lime)'}">&#9679;</span> THE AI KHABARI</span><span>{n} / {N}</span></div>
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
cover_win=win('''<div class=ub style="margin-bottom:22px"><s style="color:#9A9A9A">make it better</s></div>
<div style="display:flex;gap:14px;align-items:center;color:#9A9A9A;font-size:30px"><div style="width:44px;height:44px;border-radius:50%;background:#fff"></div><span>Sure! Here's a better version...</span></div>''','chat')
S.append((f'''<div class="a m" style="left:64px;top:130px;font-size:24px;font-weight:700;letter-spacing:4px;color:var(--lime)">PROMPT PACK &middot; WORKS ON CHATGPT, CLAUDE, GEMINI</div>
<div class="a d" style="left:64px;right:40px;top:185px;font-size:150px;letter-spacing:-5px">Stop typing these into <span style="background:var(--lime);color:#0B0D1A;padding:0 14px;border-radius:14px">ChatGPT</span></div>
<div class=a style="left:110px;right:70px;top:720px;transform:rotate(2deg)">{cover_win}</div>
<div class="a s" style="left:64px;right:64px;top:1060px;font-size:72px;line-height:1.05">5 swaps. Number 5 is the one <span style="color:var(--lime)">everyone</span> does.</div>''',False))
S.append((swap(1,'Vague tasks','Write an email to my boss.','Write a [[5-line]] email to my boss asking to move Friday\'s review to Monday. [[Tone: polite and direct.]] End with one suggested time.',('AI fills gaps with guesses. Give it the <b style="color:var(--lime)">goal, length and tone</b> and the first draft is usually usable.',985)),False))
S.append((swap(2,'"Make it better"','Make it better.','Rewrite this to be shorter and clearer [[for a busy manager]]. Keep every number. Then [[list what you changed]] in 3 bullets.',('"Better" means nothing to a model. Say <b style="color:var(--lime)">better for whom</b>, and make it show its edits.',985)),False))
S.append((swap(3,'No context','Explain AI agents.','Explain AI agents [[to a shop owner with no tech background.]] Use one real-life example. [[Under 100 words.]]',('Tell it <b style="color:var(--lime)">who the answer is for</b> and set a limit. You get your level, not a textbook.',935)),False))
S.append((swap(4,'Asking for a yes','Is this a good idea?','[[Argue against this idea]] like a tough investor. Give me the 3 biggest risks, then [[one way to fix each.]]',('Chatbots tend to agree with you. <b style="color:var(--lime)">Ask it to push back</b> and find the problems before your customers do.',935)),False))
S.append((swap(5,'The one everyone does','Give me some ideas.','Give me 10 ideas for this. [[Rank the top 3 by cost and speed,]] then [[tell me which one you\'d pick]] and why.',('A list is easy, a decision is useful. <b style="color:var(--lime)">Make it rank and choose</b>, then ask "why not number 2?"',935)),False))
tmpl='''<div class=m style="font-size:34px;line-height:1.65;color:#F2F2F2">You are a <span style="color:var(--lime)">[role]</span>.<br>Help me <span style="color:var(--lime)">[task]</span><br>for <span style="color:var(--lime)">[who it's for]</span>.<br>Give it as <span style="color:var(--lime)">[format]</span>,<br>under <span style="color:var(--lime)">[length]</span>.<br>Then <span style="color:var(--lime)">[check / rank / push back]</span>.</div>'''
S.append((f'''<div class="a m" style="left:64px;top:130px;font-size:24px;font-weight:700;letter-spacing:4px;color:#2340F5">WHAT YOU CAN TAKE FROM THIS</div>
<div class="a d" style="left:64px;right:64px;top:180px;font-size:96px;letter-spacing:-3px">One prompt template for everything</div>
<div class=a style="left:48px;right:48px;top:420px">{win(tmpl,'copy me')}</div>
<div class="a s" style="left:64px;right:64px;top:1020px;font-size:62px">Save this. Send it to the friend who still types <span style="background:#0B0D1A;color:var(--lime);padding:0 12px">"make it better"</span>.</div>''',True))
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
s.save('/tmp/claude-0/prompts2_sheet.jpg',quality=85);print('ok',N)
