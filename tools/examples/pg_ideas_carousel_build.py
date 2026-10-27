from playwright.sync_api import sync_playwright
F='file:///mnt/skills/examples/canvas-design/canvas-fonts/'
OUT='/home/claude/car/pg'
CSS=f"""
@font-face{{font-family:Disp;src:url('{F}BricolageGrotesque-Bold.ttf')}}
@font-face{{font-family:Ser;src:url('{F}InstrumentSerif-Italic.ttf')}}
@font-face{{font-family:Mono;font-weight:700;src:url('{F}JetBrainsMono-Bold.ttf')}}
@font-face{{font-family:Sans;src:url('{F}InstrumentSans-Regular.ttf')}}
@font-face{{font-family:Sans;font-weight:700;src:url('{F}InstrumentSans-Bold.ttf')}}
:root{{--bg:#16171B;--ink:#F4EFE6}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;overflow:hidden;color:var(--ink);font-family:Sans;position:relative;background:var(--bg)}}
.a{{position:absolute}}.d{{font-family:Disp;letter-spacing:-3px;line-height:.98}}.s{{font-family:Ser}}.m{{font-family:Mono;font-weight:700}}
.top{{position:absolute;left:64px;right:64px;top:52px;display:flex;justify-content:space-between;font-family:Mono;font-weight:700;font-size:22px;letter-spacing:3px}}
.bot{{position:absolute;left:64px;right:64px;bottom:44px;display:flex;justify-content:space-between;font-family:Mono;font-weight:700;font-size:22px}}
.box{{background:var(--ink);color:#fff;padding:0 16px;border-radius:12px}}
.card{{background:#F4EFE6;color:#16171B;border-radius:26px;padding:28px 32px;box-shadow:8px 8px 0 #E9B949}}
.tag{{font-family:Mono;font-weight:700;font-size:22px;letter-spacing:2px;padding:8px 16px;border-radius:30px;background:#E9B949;color:#16171B}}
"""
def page(n,N,body,dark=False):
    st='style="background:#16171B;color:#fff"' if dark else ''
    return f"""<html><head><meta charset=utf-8><style>{CSS}</style></head><body {st}>{body}
<div class=top><span>&#9679; THE AI KHABARI</span><span>{n} / {N}</span></div>
<div class=bot><span>@theaikhabari</span><span>{'SAVE THIS' if n==N else 'SWIPE &rarr;'}</span></div></body></html>"""
def card(t,b):
    return f'<div class=card><div class=d style="font-size:66px;letter-spacing:-2px">{t}</div><div style="font-size:40px;line-height:1.32;margin-top:10px">{b}</div></div>'
Q=lambda s:f'<div class=s style="font-size:80px;line-height:1.06">&ldquo;{s}&rdquo;</div>'
def rule(k,quote,do,ai):
    return f"""<div class="a d" style="right:40px;top:960px;font-size:420px;color:#E9B949;opacity:.16;letter-spacing:-10px">0{k}</div><div class="a m" style="left:64px;top:120px;font-size:28px;letter-spacing:3px;color:#E9B949">RULE {k} &middot; PAUL GRAHAM</div>
<div class=a style="left:64px;right:64px;top:180px" >{'<div class=card>'+Q(quote)+'</div>'}</div>
<div class=a style="left:64px;right:64px;top:640px;display:flex;flex-direction:column;gap:26px">
 <div class=card style="background:#E9B949;color:#16171B;box-shadow:8px 8px 0 #F4EFE6"><div class=m style="font-size:24px;color:#16171B;letter-spacing:2px">DO THIS TONIGHT</div><div style="font-size:42px;line-height:1.3;margin-top:8px">{do}</div></div>
 <div class=card><div class=m style="font-size:24px;letter-spacing:2px">IN THE AI ERA</div><div style="font-size:40px;line-height:1.3;margin-top:8px">{ai}</div></div></div>"""
S=[]
S.append(("""<div class=a style="right:-200px;top:980px;width:620px;height:620px;border-radius:50%;border:44px solid #E9B949;opacity:.9"></div><div class="a m" style="left:64px;top:130px;font-size:28px;letter-spacing:3px;color:#E9B949">FOUNDERS + DEVS WITH SIDE PROJECTS</div>
<div class="a d" style="left:64px;right:40px;top:190px;font-size:92px">How to find a startup idea, from the guy whose Y&nbsp;Combinator backed</div>
<div class="a" style="left:64px;right:64px;top:610px;display:flex;flex-wrap:wrap;gap:16px">
 <span class=d style="font-size:84px;background:#E9B949;color:#16171B;padding:4px 22px;border-radius:14px">AIRBNB</span>
 <span class=d style="font-size:84px;background:#F4EFE6;color:#16171B;padding:4px 22px;border-radius:14px">STRIPE</span>
 <span class=d style="font-size:84px;background:#E9B949;color:#16171B;padding:4px 22px;border-radius:14px">DROPBOX</span>
 <span class=d style="font-size:84px;background:#F4EFE6;color:#16171B;padding:4px 22px;border-radius:14px">REDDIT</span></div>
<div class="a s" style="left:64px;right:64px;top:900px;font-size:76px;line-height:1.05;color:#E9B949">Paul Graham's 4 rules. Written in 2012. Truer now.</div>""",False))
S.append((rule(1,"The way to get startup ideas is not to try to think of startup ideas.",
 "Write down 10 things that annoyed you at work this week. That list beats any brainstorm.",
 "AI made building cheap. Knowing the real problem is now the rare part."),False))
S.append((rule(2,"Live in the future, then build what's missing.",
 "List the AI tools you use daily. Where do you still copy-paste, wait or fix things by hand?",
 "If you use AI every day, you already live in the future most people haven't reached."),False))
S.append((rule(3,"You can either dig a hole that's broad but shallow, or one that's narrow and deep, like a well.",
 "Find 10 people who need it so badly they'd use a broken first version.",
 "A tiny group that urgently needs it beats a million people who think it's 'cool'."),False))
S.append(("""<div class="a" style="left:64px;top:118px"><span class=tag style="background:#E9B949;color:#16171B">SCREENSHOT THIS</span></div>
<div class="a d" style="left:64px;right:64px;top:180px;font-size:84px;color:#fff">The 4 rules</div>
<div class=a style="left:64px;right:64px;top:320px;display:flex;flex-direction:column;gap:22px;font-size:42px;line-height:1.25;color:#fff">
 <div><b style="color:#E9B949">1.</b> Don't brainstorm. Notice problems, ideally your own.</div>
 <div><b style="color:#E9B949">2.</b> Live in the future, then build what's missing.</div>
 <div><b style="color:#E9B949">3.</b> Dig a well: a few people who need it badly.</div>
 <div><b style="color:#E9B949">4.</b> Avoid "sitcom" ideas that only sound good.</div></div>
<div class="a d" style="left:64px;right:64px;top:860px;font-size:66px;color:#fff">Send this to the friend who says "I'd start a company if I had an idea."</div>
<div class="a" style="left:64px;top:1085px"><span class=d style="font-size:56px;background:#E9B949;color:#16171B;padding:6px 22px;border-radius:14px">Save this + follow @theaikhabari</span></div>
<div class="a m" style="left:64px;right:64px;top:1195px;font-size:18px;color:#C9B98F">Source: Paul Graham, "How to Get Startup Ideas", paulgraham.com, Nov 2012. Quotes verbatim; tips are ours.</div>""",True))
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
