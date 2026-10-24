from playwright.sync_api import sync_playwright
F='file:///mnt/skills/examples/canvas-design/canvas-fonts/'
OUT='/home/claude/car/fin'
K='#0F1E2E';A='#0E7C66';P='#FFB020'
CSS=f"""
@font-face{{font-family:Disp;src:url('{F}BricolageGrotesque-Bold.ttf')}}
@font-face{{font-family:Ser;src:url('{F}InstrumentSerif-Italic.ttf')}}
@font-face{{font-family:Mono;font-weight:700;src:url('{F}JetBrainsMono-Bold.ttf')}}
@font-face{{font-family:MonoR;src:url('{F}JetBrainsMono-Regular.ttf')}}
@font-face{{font-family:Sans;src:url('{F}InstrumentSans-Regular.ttf')}}
@font-face{{font-family:Sans;font-weight:700;src:url('{F}InstrumentSans-Bold.ttf')}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;overflow:hidden;color:{K};font-family:Sans;position:relative;background:#F2FBF7}}
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
.t{{font-size:36px;line-height:1.3;color:#2E3B45}}
.ex{{font-family:MonoR;font-size:28px;line-height:1.4;color:{A};margin-top:14px}}
"""
GRAIN='<svg class=grain width="1080" height="1350"><filter id=n><feTurbulence type=fractalNoise baseFrequency=.9 numOctaves=3 stitchTiles=stitch/><feColorMatrix values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 .55 0"/></filter><rect width=100% height=100% filter=url(#n)/></svg>'
MESHES=[
 [('#5EE3B4',8,12,48),('#8EC9FF',92,18,50),('#FFD66B',25,95,50),('#F2FBF7',70,60,45)],
 [('#8EC9FF',10,8,48),('#7FE8C2',95,45,48),('#FFE7A0',15,92,50),('#F2FBF7',55,50,40)],
 [('#FFD66B',90,8,45),('#5EE3B4',5,55,48),('#A9D4FF',85,95,55),('#F2FBF7',50,40,40)],
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
S.append(f"""<div class=a style="left:64px;top:130px"><span class=chip>FOR ANALYSTS &middot; BANKERS &middot; INVESTORS</span></div>
<div class="a d" style="left:64px;right:64px;top:200px;font-size:118px">Work in finance? Claude has a <span class=hl>Wall Street toolkit</span> now.</div>
<div class="a glass" style="left:64px;right:64px;top:860px;padding:30px 36px">
 <div class=m style="font-size:20px;letter-spacing:2px;color:{A}">PLUGGED STRAIGHT INTO THE CHAT</div>
 <div style="display:flex;gap:14px;margin-top:18px;flex-wrap:wrap">
 {''.join(f'<span style="font-family:Disp;font-size:36px;background:#fff;border-radius:18px;padding:10px 20px">{x}</span>' for x in ['PitchBook','Morningstar','S&amp;P Capital IQ','LSEG',"Moody's"])}</div>
 <div class=s style="font-size:44px;margin-top:22px">Live market data + ready-made models.</div></div>""")
S.append(f"""<div class=a style="left:64px;top:130px"><span class=chip>CONNECTORS &middot; 1 / 2</span></div>
<div class="a d" style="left:64px;right:64px;top:200px;font-size:84px">Markets and credit, live</div>
<div class=a style="left:64px;right:64px;top:430px;display:flex;flex-direction:column;gap:40px">
{tool('&#8599;','#0E7C66','LSEG','Live market data: equities, FX, fixed income, macro indicators, analyst estimates.','"How did EUR/USD and the 10-year yield move this week?"')}
{tool('Aa','#0F1E2E',"Moody's",'Credit ratings, research and company data on 600M+ public and private companies.','"Summarise the rating history and outlook for [company]"')}
</div><div class="a s" style="left:64px;right:64px;top:1185px;font-size:46px;line-height:1.1">No more copy-pasting from five terminals.</div>""")
S.append(f"""<div class=a style="left:64px;top:130px"><span class=chip>CONNECTORS &middot; 2 / 2</span></div>
<div class="a d" style="left:64px;right:64px;top:200px;font-size:84px">Private deals and fund research</div>
<div class=a style="left:64px;right:64px;top:430px;display:flex;flex-direction:column;gap:40px">
{tool('PB','#2F6BFF','PitchBook','Private markets: funding rounds, valuations, investors, M&amp;A.','"Climate-tech Series B rounds this quarter, with lead investors"')}
{tool('&#9733;','#E0A100','Morningstar','Fund and stock research, ratings and performance data.','"Compare fees and 5-year returns of these 3 funds"')}
</div><div class="a s" style="left:64px;right:64px;top:1185px;font-size:46px;line-height:1.1">Plus S&amp;P Capital IQ for company financials.</div>""")
S.append(f"""<div class=a style="left:64px;top:130px"><span class=chip>AGENT SKILLS &middot; READY-MADE MODELS</span></div>
<div class="a d" style="left:64px;right:64px;top:200px;font-size:84px">The analyst work, as skills</div>
<div class=a style="left:64px;width:1056px;top:420px;display:flex;flex-direction:column;gap:26px;zoom:.9">
{tool('DCF','#0E7C66','DCF model','Free cash flow projections, WACC, scenario toggles and sensitivity tables.','For valuation and pitch work')}
{tool('CO','#2F6BFF','Comparable companies','Valuation multiples and operating metrics, easy to refresh.','For comps tables')}
{tool('EA','#E0A100','Earnings analysis','Pulls key metrics, guidance changes and management commentary from the quarter.','For earnings season')}
</div>""")
S.append(f"""<div class=a style="left:64px;top:130px"><span class=chip>TRY IT &middot; SKILL + CONNECTOR</span></div>
<div class="a d" style="left:64px;right:64px;top:200px;font-size:84px">A valuation in one prompt</div>
<div class="a glass" style="left:64px;right:64px;top:440px;overflow:hidden;background:rgba(15,30,46,.93);border-color:rgba(255,255,255,.2)">
 <div style="display:flex;gap:10px;align-items:center;padding:18px 28px;border-bottom:1.5px solid rgba(255,255,255,.15)"><i style="width:18px;height:18px;border-radius:9px;background:#FF5F57"></i><i style="width:18px;height:18px;border-radius:9px;background:#FEBC2E"></i><i style="width:18px;height:18px;border-radius:9px;background:#28C840"></i><span class=m style="color:#7FE8C2;font-size:21px;margin-left:12px">Claude</span></div>
 <div style="font-family:MonoR;font-size:33px;line-height:1.45;padding:30px 34px;color:#fff">Use the DCF skill with my S&amp;P Capital IQ data: build a 5-year DCF for <b style="color:#FFD66B">[company]</b> with base, bull and bear cases and a WACC sensitivity table.<br><br>Then list the 3 assumptions that move the value most.</div></div>
<div class="a s" style="left:64px;right:64px;top:1120px;font-size:44px;line-height:1.1">Check every number before it goes in a deck.</div>""")
S.append(f"""<div class=a style="left:64px;top:130px"><span class=chip>SWITCH IT ON</span></div>
<div class="a glass" style="left:64px;right:64px;top:210px;padding:36px 40px;font-size:36px;line-height:1.6">
<b>1.</b> claude.ai &rarr; Settings &rarr; <b>Connectors</b><br><b>2.</b> Sign in with your firm's data accounts<br><b>3.</b> Skills: Settings &rarr; Capabilities</div>
<div class="a t" style="left:64px;right:64px;top:520px;font-size:28px">Data connectors use your own subscriptions to those providers. Skills: Max, Team, Enterprise.</div>
<div class="a d" style="left:64px;right:64px;top:640px;font-size:68px">Know someone in <span class=hl>finance</span>? Send this to them.</div>
<div class="a glass" style="left:64px;right:64px;top:830px;padding:26px 34px">
 <div class="s" style="font-size:42px;line-height:1.1">In finance yourself?</div>
 <div style="font-family:Disp;font-size:44px;letter-spacing:-1px;margin-top:10px"><span style="background:#0F1E2E;color:#fff;padding:2px 14px;border-radius:12px">Save this</span> + follow <span style="color:#0E7C66">@theaikhabari</span></div>
 <div class=t style="font-size:28px;margin-top:8px">New AI tools for your field, every week.</div></div>
<div class="a m" style="left:64px;right:64px;top:1180px;font-size:17px;line-height:1.5;color:#4A5A66">Source: Anthropic, "Advancing Claude for Financial Services"; CFA UK community. Example questions are ours. Not investment advice. Not sponsored.</div>""")
N=len(S)
with sync_playwright() as p:
    b=p.chromium.launch(args=['--allow-file-access-from-files'])
    for i,body in enumerate(S,1):
        open(f'{OUT}/s{i}.html','w').write(page(i,N,body))
        pg=b.new_page(viewport={'width':1080,'height':1350});pg.goto(f'file://{OUT}/s{i}.html');pg.wait_for_timeout(700)
        pg.screenshot(path=f'{OUT}/slide{i}.jpg',type='jpeg',quality=93)
print('ok',N)
