from playwright.sync_api import sync_playwright
import os
F='file:///mnt/skills/examples/canvas-design/canvas-fonts/'
OUT='/home/claude/car/prompts1'
# Palette: Paper & Cobalt (light) — bg #F2F0EB, text #101418, accent #2448D8
CSS=f"""
@font-face{{font-family:Disp;src:url('{F}BricolageGrotesque-Bold.ttf')}}
@font-face{{font-family:Ser;src:url('{F}CrimsonPro-Italic.ttf')}}
@font-face{{font-family:Mono;src:url('{F}GeistMono-Regular.ttf')}}
@font-face{{font-family:Mono;font-weight:700;src:url('{F}GeistMono-Bold.ttf')}}
@font-face{{font-family:Sans;src:url('{F}InstrumentSans-Regular.ttf')}}
@font-face{{font-family:Sans;font-weight:700;src:url('{F}InstrumentSans-Bold.ttf')}}
:root{{--bg:#F2F0EB;--tx:#101418;--ac:#2448D8;--dim:#5F6168;--card:#FFFFFF;--line:#DEDAD0;--bad:#9A9A93}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;overflow:hidden;background:var(--bg);color:var(--tx);font-family:Sans;position:relative}}
.a{{position:absolute}}.d{{font-family:Disp;letter-spacing:-2px;line-height:1.02}}.s{{font-family:Ser;font-style:italic}}.m{{font-family:Mono}}
.top{{position:absolute;left:72px;right:72px;top:58px;display:flex;justify-content:space-between;font-family:Mono;font-size:24px;letter-spacing:3px;font-weight:700}}
.bot{{position:absolute;left:72px;right:72px;bottom:46px;display:flex;justify-content:space-between;font-family:Mono;font-size:21px;color:var(--dim)}}
.bad{{border-radius:24px;border:2px dashed var(--line);padding:26px 30px;color:var(--bad);font-size:44px}}
.bad b{{font-family:Mono;font-size:22px;letter-spacing:3px;color:#B0453A;display:block;margin-bottom:8px}}
.good{{border-radius:24px;background:var(--card);border:2px solid var(--tx);box-shadow:10px 10px 0 var(--ac);padding:28px 32px}}
.good b{{font-family:Mono;font-size:22px;letter-spacing:3px;color:var(--ac);display:block;margin-bottom:12px}}
.good .m{{font-size:37px;line-height:1.45}}
.why{{font-size:38px;line-height:1.35;color:var(--dim)}}
.why span{{color:var(--tx);font-weight:700}}
.num{{font-family:Disp;font-size:150px;line-height:1;color:var(--ac);letter-spacing:-4px}}
"""
def page(n,N,body,credit='',dark=False):
    st='background:#101418;color:#F2F0EB' if dark else ''
    tc='#F2F0EB' if dark else 'var(--tx)'
    return f"""<html><head><meta charset=utf-8><style>{CSS}</style></head><body style="{st}">{body}
<div class=top style="color:{tc}"><span><span style="color:{'#7C95FF' if dark else 'var(--ac)'}">&#9679;</span> THE AI KHABARI</span><span>{n} / {N}</span></div>
<div class=bot><span style="color:{tc};font-weight:700">@theaikhabari</span><span>{credit}</span></div></body></html>"""
def swap(i,label,bad,good,why):
    return f"""<div class="a" style="left:72px;top:150px;display:flex;align-items:flex-end;gap:24px"><div class=num>{i}</div><div class="m" style="font-size:26px;letter-spacing:4px;font-weight:700;color:var(--dim);padding-bottom:26px">{label}</div></div>
<div class=a style="left:72px;right:72px;top:330px"><div class=bad><b>STOP TYPING</b><s>{bad}</s></div></div>
<div class=a style="left:72px;right:82px;top:530px"><div class=good><b>TYPE THIS INSTEAD</b><div class=m>{good}</div></div></div>
<div class="a why" style="left:72px;right:72px;top:930px">{why}</div>"""
S=[]
S.append(("""<div class="a m" style="left:72px;top:190px;font-size:28px;letter-spacing:5px;font-weight:700;color:var(--ac)">PROMPT PACK &middot; SAVE THIS</div>
<div class="a d" style="left:72px;right:72px;top:250px;font-size:132px">5 things to stop typing into ChatGPT</div>
<div class="a s" style="left:72px;right:72px;top:720px;font-size:66px;line-height:1.1">Number 5 is the one <span style="color:var(--ac)">everyone</span> does.</div>
<div class=a style="left:72px;right:72px;top:900px;display:flex;gap:18px">
 <div class="bad" style="flex:1;font-size:34px"><s>"make it better"</s></div>
 <div class="good" style="flex:1;padding:22px 26px"><div class=m style="font-size:27px">"rewrite it for a busy manager, keep the numbers"</div></div></div>
<div class="a m" style="left:72px;top:1150px;font-size:26px;color:var(--dim)">Works on ChatGPT, Claude and Gemini. Swipe &rarr;</div>""",''))
S.append((swap(1,'VAGUE TASKS','"Write an email to my boss."','Write a 5-line email to my boss asking to move Friday\'s review to Monday. Tone: polite and direct. End with one suggested time.','AI fills gaps with guesses. Give it the <span>goal, length and tone</span> and the first draft is usually usable.'),''))
S.append((swap(2,'"MAKE IT BETTER"','"Make it better."','Rewrite this to be shorter and clearer for a busy manager. Keep every number. Then list what you changed in 3 bullets.','"Better" means nothing to a model. Say <span>better for whom</span>, and ask it to show its edits so you can check them.'),''))
S.append((swap(3,'NO CONTEXT','"Explain AI agents."','Explain AI agents to a shop owner with no tech background. Use one real-life example. Keep it under 100 words.','Tell it <span>who the answer is for</span> and set a limit. You get your level, not a textbook.'),''))
S.append((swap(4,'ASKING FOR A YES','"Is this a good idea?"','Argue against this idea like a tough investor. Give me the 3 biggest risks, then one way to fix each.','Chatbots tend to agree with you. <span>Ask it to push back</span> and you get the problems before your customers find them.'),''))
S.append((swap(5,'THE ONE EVERYONE DOES','"Give me some ideas."','Give me 10 ideas for this. Rank the top 3 by cost and speed, then tell me which one you\'d pick and why.','A list is easy, a decision is useful. <span>Make it rank and choose</span>, then ask "why not number 2?"'),''))
S.append(("""<div class="a m" style="left:72px;top:170px;font-size:28px;letter-spacing:5px;font-weight:700;color:#7C95FF">WHAT YOU CAN TAKE FROM THIS</div>
<div class="a d" style="left:72px;right:72px;top:225px;font-size:92px;color:#F2F0EB">One template for every prompt</div>
<div class=a style="left:72px;right:72px;top:470px;border-radius:24px;border:2px dashed #7C95FF;padding:34px 36px"><div class=m style="font-size:34px;line-height:1.6;color:#F2F0EB">You are a <span style="color:#7C95FF">[role]</span>.<br>Help me <span style="color:#7C95FF">[task]</span> for <span style="color:#7C95FF">[who it's for]</span>.<br>Give it as <span style="color:#7C95FF">[format]</span>, under <span style="color:#7C95FF">[length]</span>.<br>Then <span style="color:#7C95FF">[check / rank / push back]</span>.</div></div>
<div class="a s" style="left:72px;right:72px;top:910px;font-size:58px;color:#F2F0EB">Save this. Send it to the friend who types <span style="color:#7C95FF">"make it better"</span>.</div>
<div class=a style="left:72px;top:1130px;display:flex;gap:16px"><div class=m style="background:#2448D8;color:#fff;border-radius:40px;padding:14px 30px;font-size:26px;font-weight:700;letter-spacing:2px">SAVE + SEND</div><div class=m style="border:2px solid #F2F0EB;color:#F2F0EB;border-radius:40px;padding:12px 28px;font-size:26px;font-weight:700;letter-spacing:2px">FOLLOW @THEAIKHABARI</div></div>""",'',True))
N=len(S)
with sync_playwright() as p:
    b=p.chromium.launch(args=['--allow-file-access-from-files'])
    for i,item in enumerate(S,1):
        body,cred=item[0],item[1];dark=len(item)>2 and item[2]
        open(f'{OUT}/s{i}.html','w').write(page(i,N,body,cred,dark))
        pg=b.new_page(viewport={'width':1080,'height':1350});pg.goto(f'file://{OUT}/s{i}.html');pg.wait_for_timeout(600)
        pg.screenshot(path=f'{OUT}/slide{i}.jpg',type='jpeg',quality=92);pg.close()
    b.close()
from PIL import Image
ims=[Image.open(f'{OUT}/slide{i}.jpg').resize((540,675)) for i in range(1,N+1)]
s=Image.new('RGB',(540*4,675*2),'white')
for i,im in enumerate(ims): s.paste(im,((i%4)*540,(i//4)*675))
s.save('/tmp/claude-0/prompts_sheet.jpg',quality=85);print('ok',N)
