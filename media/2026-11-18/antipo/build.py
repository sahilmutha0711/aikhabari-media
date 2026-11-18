from playwright.sync_api import sync_playwright
D='/home/claude/aikhabari-media/media/2026-11-18/antipo'
F='file:///mnt/skills/examples/canvas-design/canvas-fonts/'
BG,TX,AC,INK='#020617','#F0F9FF','#22D3EE','#020617'
css=f"""@font-face{{font-family:BS;src:url('{F}BigShoulders-Bold.ttf')}}@font-face{{font-family:GL;src:url('{F}Gloock-Regular.ttf')}}@font-face{{font-family:MO;src:url('{F}IBMPlexMono-Bold.ttf')}}
*{{margin:0;padding:0;box-sizing:border-box}}body{{width:1080px;height:1350px;background:{BG};color:{TX};font-family:BS;position:relative;overflow:hidden}}
.top{{position:absolute;top:44px;left:60px;right:60px;display:flex;justify-content:space-between;font-family:MO;font-size:24px;letter-spacing:3px;opacity:.8}}
.bot{{position:absolute;bottom:40px;left:60px;font-family:MO;font-size:24px;opacity:.7}}
.cr{{position:absolute;bottom:40px;right:60px;font-family:MO;font-size:17px;opacity:.55}}
.H{{text-transform:uppercase;line-height:.9;letter-spacing:-1px}}
.box{{background:{AC};color:{INK};padding:0 22px;border-radius:70px;display:inline-block}}
.pill{{display:inline-block;font-family:MO;font-size:30px;padding:12px 28px;border-radius:60px;border:3px solid {AC};color:{AC};letter-spacing:2px}}
.ser{{font-family:GL;font-size:46px;line-height:1.25}}
.num{{width:150px;height:150px;border-radius:50%;background:{AC};color:{INK};display:flex;align-items:center;justify-content:center;font-size:96px;flex:none}}
.row{{display:flex;gap:40px;align-items:center}}
.ph{{position:absolute;inset:0;background-size:cover;background-position:center;filter:grayscale(1) contrast(1.1)}}
.sh{{position:absolute;inset:0;background:linear-gradient(180deg,{BG}CC 0%,{BG}55 35%,{BG}EE 70%,{BG} 100%)}}
.glow{{position:absolute;width:900px;height:900px;border-radius:50%;background:radial-gradient({AC}26,transparent 65%);right:-300px;top:-250px}}
"""
def page(n,body,photo=None,cred=''):
    ph=f"<div class=ph style=\"background-image:url('file://{D}/{photo}')\"></div><div class=sh></div>" if photo else "<div class=glow></div>"
    return f"<!doctype html><html><head><meta charset=utf-8><style>{css}</style></head><body>{ph}<div class=top><span>● THE AI KHABARI</span><span>{n} / 7</span></div>{body}<div class=bot>@theaikhabari</div><div class=cr>{cred}</div></body></html>"
def numslide(n,k,title,big,sub,note):
    return page(n,f"""<div style="position:absolute;left:70px;right:70px;top:200px">
<div class=row><div class=num>{k}</div><div class=H style="font-size:92px">{title}</div></div>
<div class=H style="font-size:230px;margin-top:80px;color:{AC}">{big}</div>
<div class=ser style="margin-top:30px">{sub}</div>
<div style="margin-top:60px;font-family:MO;font-size:30px;line-height:1.5;opacity:.85;border-left:6px solid {AC};padding-left:26px">{note}</div></div>""")
S=[]
S.append(page(1,f"""<div style="position:absolute;left:70px;right:70px;top:470px">
<div class=pill>ANT · NASDAQ · THURSDAY NOV 19</div>
<div class=H style="font-size:160px;margin-top:40px">ANTHROPIC<br>IPO <span class=box>TOMORROW</span></div>
<div class=ser style="margin-top:40px">Read this before you hit "buy"</div></div>""",'nasdaq2.jpg','PHOTO: LUCA MARFÈ · CC BY 2.0'))
S.append(numslide(2,'1','THE PRICE','$70–78','expected range per share · final price set tonight','825 million shares on offer.<br>Trading is expected to start Thursday.<br>Ticker: ANT'))
S.append(numslide(3,'2','THE SIZE','~$968B','market value at the $74 midpoint','Range: about $917B to $1,020B.<br>Nearly a trillion dollars,<br>on its first day of trading.'))
S.append(page(4,f"""<div style="position:absolute;left:70px;right:70px;top:220px">
<div class=row><div class=num>3</div><div class=H style="font-size:92px">THE DEMAND</div></div>
<div class=H style="font-size:230px;margin-top:60px;color:{AC}">~6×</div>
<div class=ser style="margin-top:20px">orders vs shares on offer by the 4th day of the roadshow</div>
<div style="margin-top:60px;font-family:MO;font-size:30px;line-height:1.5;opacity:.85;border-left:6px solid {AC};padding-left:26px">Up to 20% of shares may go to retail,<br>but your broker can't guarantee you any.</div></div>""",None))
S.append(page(5,f"""<div style="position:absolute;left:70px;right:70px;top:220px">
<div class=row><div class=num>4</div><div class=H style="font-size:92px">THE TRAP</div></div>
<div class=H style="font-size:200px;margin-top:60px;color:{AC}">−20.5%</div>
<div class=ser style="margin-top:20px">where 2026's 10 biggest US IPOs trade vs their IPO price, on average (FT)</div>
<div style="margin-top:60px;font-family:MO;font-size:30px;line-height:1.5;opacity:.85;border-left:6px solid {AC};padding-left:26px">Cerebras priced at $185, jumped on day one,<br>and now trades below $185.</div></div>""",None))
S.append(page(6,f"""<div style="position:absolute;left:70px;right:70px;top:190px">
<div class=pill>SCREENSHOT THIS</div>
<div class=H style="font-size:96px;margin:30px 0 40px">BEFORE YOU BUY ANT</div>
""" + ''.join(f"""<div style="display:flex;justify-content:space-between;align-items:center;border-radius:80px;background:#0B1630;border:3px solid #1E3A5F;padding:26px 40px;margin-bottom:22px;font-family:MO;font-size:32px"><span>{a}</span><span style="color:{AC}">{b}</span></div>""" for a,b in [('IPO price','≠ opening price'),('Order type','use a LIMIT order'),('Position size','only what you can lose'),('Day-one pop','= price of hype'),('Patience','first earnings report')]) + """
<div class=ser style="margin-top:34px;font-size:38px">The first trade often happens hours after the market opens.</div></div>""",None))
S.append(page(7,f"""<div style="position:absolute;left:70px;right:70px;top:280px;text-align:center">
<div class=H style="font-size:150px"><span class=box>SAVE THIS</span><br>FOR TOMORROW</div>
<div class=ser style="margin-top:60px">Send it to the friend who's buying ANT at the open.</div>
<div class=H style="font-size:64px;margin-top:70px">FOLLOW @THEAIKHABARI</div>
<div class=ser style="font-size:34px;opacity:.8;margin-top:14px">Full breakdown after the bell</div>
<div style="font-family:MO;font-size:22px;opacity:.6;margin-top:70px;line-height:1.6">Made with Claude, Anthropic's AI, so we're not neutral.<br>Sources: Anthropic S-1/A via StockTitan, TradingKey, FT · Not financial advice</div></div>""",None))
with sync_playwright() as p:
    b=p.chromium.launch(args=['--allow-file-access-from-files']);pg=b.new_page(viewport={'width':1080,'height':1350})
    for i,h in enumerate(S,1):
        open(f'{D}/s.html','w').write(h);pg.goto(f'file://{D}/s.html');pg.wait_for_timeout(500);pg.screenshot(path=f'{D}/slide{i}.jpg',type='jpeg',quality=92)
from PIL import Image
M=Image.new('RGB',(7*360,450))
for i in range(7):M.paste(Image.open(f'{D}/slide{i+1}.jpg').resize((360,450)),(i*360,0))
M.save(f'{D}/sheet.jpg',quality=85)
