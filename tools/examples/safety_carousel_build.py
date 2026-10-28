from playwright.sync_api import sync_playwright
F='file:///mnt/skills/examples/canvas-design/canvas-fonts/'
OUT='/home/claude/car/safety'
K='#2A0E10';A='#D6322B';P='#FFB020'
CSS=f"""
@font-face{{font-family:Disp;src:url('{F}BricolageGrotesque-Bold.ttf')}}
@font-face{{font-family:Ser;src:url('{F}InstrumentSerif-Italic.ttf')}}
@font-face{{font-family:Mono;font-weight:700;src:url('{F}JetBrainsMono-Bold.ttf')}}
@font-face{{font-family:MonoR;src:url('{F}JetBrainsMono-Regular.ttf')}}
@font-face{{font-family:Sans;src:url('{F}InstrumentSans-Regular.ttf')}}
@font-face{{font-family:Sans;font-weight:700;src:url('{F}InstrumentSans-Bold.ttf')}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;overflow:hidden;color:{K};font-family:Sans;position:relative;background:#FFF6F0}}
.mesh{{position:absolute;inset:-10%;filter:blur(60px)}}
.grain{{position:absolute;inset:0;opacity:.10;mix-blend-mode:multiply}}
.a{{position:absolute}}.d{{font-family:Disp;letter-spacing:-3px;line-height:.98}}.s{{font-family:Ser}}.m{{font-family:Mono;font-weight:700}}
.top{{position:absolute;left:64px;right:64px;top:52px;display:flex;justify-content:space-between;font-family:Mono;font-weight:700;font-size:21px;letter-spacing:3px;z-index:5}}
.bot{{position:absolute;left:64px;right:64px;bottom:44px;display:flex;justify-content:space-between;font-family:Mono;font-weight:700;font-size:21px;z-index:5}}
.glass{{background:rgba(255,255,255,.62);backdrop-filter:blur(18px);border:1.5px solid rgba(255,255,255,.9);border-radius:36px;box-shadow:0 24px 60px rgba(15,40,50,.14)}}
.chip{{display:inline-block;font-family:Mono;font-weight:700;font-size:20px;letter-spacing:2px;background:{K};color:#fff;padding:8px 16px;border-radius:30px}}
.hl{{background:{K};color:#fff;padding:0 16px;border-radius:14px}}
.ic{{width:92px;height:92px;border-radius:26px;display:flex;align-items:center;justify-content:center;font-family:Disp;font-size:40px;color:#fff}}
.k{{font-family:Disp;font-size:60px;letter-spacing:-1.5px}}
.t{{font-size:36px;line-height:1.3;color:#4A2A2A}}
.ex{{font-family:MonoR;font-size:28px;line-height:1.4;color:{A};margin-top:14px}}
"""
GRAIN='<svg class=grain width="1080" height="1350"><filter id=n><feTurbulence type=fractalNoise baseFrequency=.9 numOctaves=3 stitchTiles=stitch/><feColorMatrix values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 .55 0"/></filter><rect width=100% height=100% filter=url(#n)/></svg>'
MESHES=[
 [('#FF8A73',8,12,48),('#FFC46B',92,18,50),('#FFB3A1',25,95,50),('#FFF6F0',70,60,45)],
 [('#FFC46B',10,8,48),('#FF9C86',95,45,48),('#FFE3A8',15,92,50),('#FFF6F0',55,50,40)],
 [('#FFB3A1',90,8,45),('#FF8A73',5,55,48),('#FFD58A',85,95,55),('#FFF6F0',50,40,40)],
]
def mesh(i):
    g=','.join(f'radial-gradient(circle at {x}% {y}%, {c} 0, transparent {r}%)' for c,x,y,r in MESHES[i%3])
    return f'<div class=mesh style="background:{g}"></div>'
def page(n,N,body):
    return f"""<html><head><meta charset=utf-8><style>{CSS}</style></head><body>{mesh(n)}{GRAIN}{body}
<div class=top><span>&#9679; THE AI KHABARI</span><span>{n} / {N}</span></div>
<div class=bot><span>@theaikhabari</span><span>{'SAVE THIS' if n==N else 'SWIPE &rarr;'}</span></div></body></html>"""
def tool(letter,col,name,what,ex):
    return f"""<div class="glass" style="padding:34px 38px;display:flex;gap:30px">
<div class=ic style="background:{col};flex:none">{letter}</div>
<div><div class=k>{name}</div><div class=t>{what}</div><div class=ex>{ex}</div></div></div>"""
S=[]
def step(n,t,d,ex,col):
    return f"""<div class="glass" style="padding:34px 38px;display:flex;gap:30px"><div class=ic style="background:{col};flex:none">{n}</div><div><div class=k>{t}</div><div class=t>{d}</div><div class=ex>{ex}</div></div></div>"""
S.append(f"""<div class=a style="left:64px;top:130px"><span class=chip>SEND THIS TO YOUR FAMILY GROUP</span></div>
<div class="a d" style="left:64px;right:64px;top:200px;font-size:120px">Your email has <span class=hl>probably leaked.</span></div>
<div class="a s" style="left:64px;right:64px;top:640px;font-size:56px;line-height:1.08">Here's the 5-minute fix most people never do.</div>
<div class="a glass" style="left:64px;right:64px;top:880px;padding:30px 36px">
 <div class=m style="font-size:20px;letter-spacing:2px;color:{A}">IN THE LAST 10 DAYS</div>
 <div style="font-family:Disp;font-size:46px;line-height:1.2;margin-top:12px">Capcom: 11.7M account records exposed<br>SBI: customer records found on the dark web</div></div>""")
S.append(f"""<div class=a style="left:64px;top:130px"><span class=chip>STEP 1 + 2</span></div>
<div class="a d" style="left:64px;right:64px;top:200px;font-size:84px">Find out, then lock the door</div>
<div class=a style="left:64px;right:64px;top:430px;display:flex;flex-direction:column;gap:40px">
{step('1','Check your email','Go to haveibeenpwned.com and type your email. It shows which leaks it was in.','Free. Takes 10 seconds.','#D6322B')}
{step('2','Kill reused passwords','If one password is used on 2+ sites, change it everywhere. One leak can unlock all of them.','Let a password manager make and remember them.','#2A0E10')}
</div>""")
S.append(f"""<div class=a style="left:64px;top:130px"><span class=chip>STEP 3 + 4</span></div>
<div class="a d" style="left:64px;right:64px;top:200px;font-size:84px">Make stolen passwords useless</div>
<div class=a style="left:64px;right:64px;top:430px;display:flex;flex-direction:column;gap:40px">
{step('3','Turn on passkeys','Google, Apple, Microsoft and many banks support them. Your fingerprint or face unlocks the account.','Or at least an authenticator app, not just SMS codes.','#E08A00')}
{step('4','Never click "breach" messages','Leaked emails are used to send scams that look 100% real. Open the app or site yourself.','Typed by you > tapped from a message.','#D6322B')}
</div>""")
S.append(f"""<div class=a style="left:64px;top:130px"><span class=chip>SCREENSHOT THIS &middot; FOR PARENTS</span></div>
<div class="a glass" style="left:64px;right:64px;top:220px;padding:44px 46px">
 <div style="font-family:Disp;font-size:64px;line-height:1.1;letter-spacing:-1.5px">No bank, app or "support team" will <span class=hl>ever</span> ask for:</div>
 <div style="margin-top:30px;display:flex;flex-direction:column;gap:18px;font-family:Disp;font-size:52px">
  <div>&#10060; your OTP</div><div>&#10060; your PIN or password</div><div>&#10060; remote access to your phone</div><div>&#10060; payment to "unlock" your account</div></div></div>
<div class="a s" style="left:64px;right:64px;top:1080px;font-size:54px;line-height:1.1">If someone asks: hang up, then call the number on the back of your card.</div>""")
S.append(f"""<div class=a style="left:64px;top:130px"><span class=chip>DO IT TONIGHT</span></div>
<div class="a glass" style="left:64px;right:64px;top:210px;padding:36px 40px;font-size:38px;line-height:1.6">
<b>1.</b> haveibeenpwned.com<br><b>2.</b> No reused passwords<br><b>3.</b> Passkeys or authenticator app<br><b>4.</b> Never click "breach" messages</div>
<div class="a d" style="left:64px;right:64px;top:640px;font-size:68px">The person who needs this most <span class=hl>won't find it alone.</span></div>
<div class="a glass" style="left:64px;right:64px;top:900px;padding:26px 34px">
 <div class="s" style="font-size:42px;line-height:1.1">Send it to your family group.</div>
 <div style="font-family:Disp;font-size:44px;letter-spacing:-1px;margin-top:10px"><span style="background:#2A0E10;color:#fff;padding:2px 14px;border-radius:12px">Save this</span> + follow <span style="color:#D6322B">@theaikhabari</span></div>
 <div class=t style="font-size:28px;margin-top:8px">Tech news that actually protects you.</div></div>
<div class="a m" style="left:64px;right:64px;top:1200px;font-size:17px;line-height:1.5;color:#6A4A4A">Sources: Capcom breach (Engadget, Tech Insider, Oct 2026); SBI leak (The Hacker News, The Week, Oct 2026). Not sponsored.</div>""")
N=len(S)
with sync_playwright() as p:
    b=p.chromium.launch(args=['--allow-file-access-from-files'])
    for i,body in enumerate(S,1):
        open(f'{OUT}/s{i}.html','w').write(page(i,N,body))
        pg=b.new_page(viewport={'width':1080,'height':1350});pg.goto(f'file://{OUT}/s{i}.html');pg.wait_for_timeout(700)
        pg.screenshot(path=f'{OUT}/slide{i}.jpg',type='jpeg',quality=93)
print('ok',N)
