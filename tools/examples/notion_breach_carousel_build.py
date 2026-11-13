from playwright.sync_api import sync_playwright
F='file:///mnt/skills/examples/canvas-design/canvas-fonts/'
OUT='/home/claude/car/notion'
K='#0E1A24';A='#0E7C6B';P='#FF5A4E'
CSS=f"""
@font-face{{font-family:Disp;src:url('{F}BricolageGrotesque-Bold.ttf')}}
@font-face{{font-family:Ser;src:url('{F}InstrumentSerif-Italic.ttf')}}
@font-face{{font-family:Mono;font-weight:700;src:url('{F}JetBrainsMono-Bold.ttf')}}
@font-face{{font-family:MonoR;src:url('{F}JetBrainsMono-Regular.ttf')}}
@font-face{{font-family:Sans;src:url('{F}InstrumentSans-Regular.ttf')}}
@font-face{{font-family:Sans;font-weight:700;src:url('{F}InstrumentSans-Bold.ttf')}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;overflow:hidden;color:{K};font-family:Sans;position:relative;background:#F2FBF8}}
.mesh{{position:absolute;inset:-10%;filter:blur(60px)}}
.grain{{position:absolute;inset:0;opacity:.10;mix-blend-mode:multiply}}
.a{{position:absolute}}.d{{font-family:Disp;letter-spacing:-3px;line-height:.98}}.s{{font-family:Ser}}.m{{font-family:Mono;font-weight:700}}
.top{{position:absolute;left:64px;right:64px;top:52px;display:flex;justify-content:space-between;font-family:Mono;font-weight:700;font-size:21px;letter-spacing:3px;z-index:5}}
.bot{{position:absolute;left:64px;right:64px;bottom:44px;display:flex;justify-content:space-between;font-family:Mono;font-weight:700;font-size:21px;z-index:5}}
.glass{{background:rgba(255,255,255,.62);backdrop-filter:blur(18px);border:1.5px solid rgba(255,255,255,.9);border-radius:36px;box-shadow:0 24px 60px rgba(20,60,70,.14)}}
.chip{{display:inline-block;font-family:Mono;font-weight:700;font-size:20px;letter-spacing:2px;background:{K};color:#fff;padding:8px 16px;border-radius:30px}}
.hl{{background:{K};color:#fff;padding:0 16px;border-radius:14px}}
.ic{{width:92px;height:92px;border-radius:26px;display:flex;align-items:center;justify-content:center;font-family:Disp;font-size:40px;color:#fff}}
.k{{font-family:Disp;font-size:60px;letter-spacing:-1.5px}}
.t{{font-size:36px;line-height:1.3;color:#2E3E47}}
.ex{{font-family:MonoR;font-size:28px;line-height:1.4;color:{A};margin-top:14px}}
"""
GRAIN='<svg class=grain width="1080" height="1350"><filter id=n><feTurbulence type=fractalNoise baseFrequency=.9 numOctaves=3 stitchTiles=stitch/><feColorMatrix values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 .55 0"/></filter><rect width=100% height=100% filter=url(#n)/></svg>'
MESHES=[
 [('#7EE6D2',8,12,48),('#A9CCFF',92,18,50),('#FFE58A',25,95,50),('#F2FBF8',70,60,45)],
 [('#A9CCFF',10,8,48),('#8FEBD8',95,45,48),('#FFE9A6',15,92,50),('#F2FBF8',55,50,40)],
 [('#FFE58A',90,8,45),('#7EE6D2',5,55,48),('#B9D6FF',85,95,55),('#F2FBF8',50,40,40)],
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
S.append(f"""<div class=a style="left:64px;top:130px"><span class=chip>NOTION USERS &middot; DEVS &middot; PMs</span></div>
<div class="a d" style="left:64px;right:64px;top:200px;font-size:112px">Pasted a password into <span class=hl>Notion AI</span>? Change it today.</div>
<div class="a glass" style="left:64px;right:64px;top:820px;padding:34px 40px">
 <div class=m style="font-size:21px;letter-spacing:2px;color:{P}">&#9888; CONFIRMED BY NOTION</div>
 <div class=t style="font-size:38px;margin-top:14px;color:{K}">Hackers broke into <b>Fireworks AI</b>, a company Notion used to run some of its AI. Some <b>Notion AI chat transcripts</b> were exposed.</div>
 <div class=s style="font-size:44px;margin-top:18px">Fewer than 1% of workspaces. Here's how to check yours.</div></div>""")
def row(d,t,c='#fff'):
    return f'<div style="display:flex;gap:26px;align-items:center"><span class=m style="flex:none;width:190px;text-align:center;font-size:26px;background:{c};color:{K if c=="#fff" else "#fff"};padding:14px 0;border-radius:40px">{d}</span><span class=t style="font-size:34px;color:{K}">{t}</span></div>'
S.append(f"""<div class=a style="left:64px;top:130px"><span class=chip>WHAT HAPPENED</span></div>
<div class="a d" style="left:64px;right:64px;top:200px;font-size:86px">Your AI chats went through a company you never heard of</div>
<div class="a glass" style="left:64px;right:64px;top:520px;padding:38px 36px;display:flex;flex-direction:column;gap:30px">
{row('OCT 6','Fireworks AI discovers a breach')}
{row('OCT 23-24','Attackers hit a cloud provider, reach Fireworks dev machines')}
{row('NOV 2','Notion gets notified')}
{row('NOV 3','Notion cuts Fireworks off and deletes its data there',A)}
</div>
<div class="a s" style="left:64px;right:64px;top:1150px;font-size:44px;line-height:1.1">Fireworks has 10,000+ business customers.</div>""")
def box(ic,col,k,t):
    return f'<div class="glass" style="padding:30px 36px;display:flex;gap:28px;align-items:center"><div class=ic style="background:{col};flex:none">{ic}</div><div><div class=k style="font-size:50px">{k}</div><div class=t style="font-size:31px">{t}</div></div></div>'
S.append(f"""<div class=a style="left:64px;top:130px"><span class=chip>WHAT WAS EXPOSED</span></div>
<div class="a d" style="left:64px;right:64px;top:200px;font-size:86px">The part that should worry you</div>
<div class=a style="left:64px;right:64px;top:400px;display:flex;flex-direction:column;gap:24px">
{box('!',P,'Notion AI chats','Anything typed into an AI chat, and what the AI answered')}
{box('i','#0E1A24','Insights + early-access data','AI requests Notion sent out for classification and testing')}
{box('&#10003;',A,'Not hit: AI Meeting Notes','Unless you pasted them into an AI chat')}
</div>
<div class="a glass" style="left:64px;right:64px;top:1085px;padding:22px 34px;background:rgba(14,26,36,.92);border-color:rgba(255,255,255,.2)">
 <div class=m style="font-size:20px;letter-spacing:2px;color:#8FEBD8">SMART FACT</div>
 <div class=t style="font-size:33px;color:#fff;margin-top:6px">Notion says the data was <b>kept</b>, despite a contract promising <b>zero data retention</b>.</div></div>""")
S.append(f"""<div class=a style="left:64px;top:130px;display:flex;gap:14px"><span class=chip>CHECK IN 60 SECONDS</span><span class=chip style="background:{P}">SCREENSHOT THIS</span></div>
<div class="a d" style="left:64px;right:64px;top:200px;font-size:86px">Am I affected?</div>
<div class="a glass" style="left:64px;right:64px;top:360px;padding:46px 48px;font-size:44px;line-height:1.55;color:{K}">
<b>1.</b> Open Notion in a <b>desktop browser</b> (latest version, not the phone app)<br>
<b>2.</b> Sidebar &rarr; <b>?</b> &rarr; <span class=hl>Security incident review</span><br>
<b>3.</b> Pasted a password, API key or token into Notion AI? <b>Rotate it now.</b><br>
<b>4.</b> No message from Notion = not identified as affected (investigation ongoing)</div>
<div class="a s" style="left:64px;right:64px;top:1130px;font-size:46px;line-height:1.1">Workspace owners can download the list of affected members there too.</div>""")
S.append(f"""<div class=a style="left:64px;top:130px"><span class=chip>SAY THIS AT WORK</span></div>
<div class="a d" style="left:64px;right:64px;top:200px;font-size:80px">"Zero data retention is a <span class=hl>promise</span>, not a guarantee. Never paste secrets into AI chats."</div>
<div class="a d" style="left:64px;right:64px;top:640px;font-size:62px">Send this to the teammate who pastes <span style="color:{A}">API keys</span> into AI.</div>
<div class="a glass" style="left:64px;right:64px;top:850px;padding:26px 34px">
 <div style="font-family:Disp;font-size:44px;letter-spacing:-1px"><span style="background:{K};color:#fff;padding:2px 14px;border-radius:12px">Save this</span> + follow <span style="color:{A}">@theaikhabari</span></div>
 <div class=t style="font-size:28px;margin-top:8px">AI news that actually affects your work, every day.</div></div>
<div class="a m" style="left:64px;right:64px;top:1150px;font-size:17px;line-height:1.5;color:#4A5A62">Sources: Notion help centre notice on the Fireworks AI incident; The Record (Recorded Future News); TechCrunch. Not sponsored.</div>""")
N=len(S)
with sync_playwright() as p:
    b=p.chromium.launch(args=['--allow-file-access-from-files'])
    for i,body in enumerate(S,1):
        open(f'{OUT}/s{i}.html','w').write(page(i,N,body))
        pg=b.new_page(viewport={'width':1080,'height':1350});pg.goto(f'file://{OUT}/s{i}.html');pg.wait_for_timeout(700)
        pg.screenshot(path=f'{OUT}/slide{i}.jpg',type='jpeg',quality=93)
print('ok',N)
