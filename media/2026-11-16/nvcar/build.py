from playwright.sync_api import sync_playwright
D='/home/claude/aikhabari-media/media/2026-11-16/nvcar'
F='file:///mnt/skills/examples/canvas-design/canvas-fonts/'
BG,TX,AC,INK='#110F0B','#F5F1E8','#FFC24B','#110F0B'
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
<div class=pill>TUESDAY · NOV 17 · AFTER THE BELL</div>
<div class=H style="font-size:170px;margin-top:40px">NVIDIA<br>REPORTS<br><span class=box>TOMORROW</span></div>
<div class=ser style="margin-top:40px">5 numbers that decide your AI stocks this week</div></div>""",'nvda_hq.jpg','PHOTO: COOLCAESAR · CC BY-SA 4.0'))
S.append(page(2,f"""<div style="position:absolute;left:70px;right:70px;top:230px">
<div class=H style="font-size:120px">FIRST REPORT<br>WITHOUT <span class=box>JENSEN</span></div>
<div class=ser style="margin-top:60px">Jensen Huang resigned as CEO. CFO <b>Colette Kress</b> is interim CEO while Nvidia searches for a permanent one.</div>
<div class=ser style="margin-top:40px;opacity:.85">The quarter being reported ended <i>before</i> the leadership change, so the forward-looking numbers matter most.</div></div>""",None))
S.append(numslide(3,'1','REVENUE','$109B','what Wall Street expects (Nvidia guided $108B, +/- 2%)','Clearly above $109B = a beat.<br>Close to the $108B guide = "in line",<br>and the stock can still drop.'))
S.append(numslide(4,'2','PROFIT / SHARE','$2.47','adjusted EPS analysts expect','#3 GROSS MARGIN: guided 74% ± 0.5 pt.<br>Below that = chips are getting costlier to make.'))
S.append(page(5,f"""<div style="position:absolute;left:70px;right:70px;top:220px">
<div class=row><div class=num>4</div><div class=H style="font-size:92px">NEXT-QUARTER<br>GUIDANCE</div></div>
<div class=ser style="margin-top:40px">The number traders react to most. Do customers keep spending? China data-center sales are left out of the outlook.</div>
<div class=row style="margin-top:80px"><div class=num>5</div><div class=H style="font-size:92px">THE PLAN<br>WITHOUT JENSEN</div></div>
<div class=ser style="margin-top:40px">Blackwell Ultra ramp, when Vera Rubin starts selling, and any word on the next CEO.</div></div>""",None))
S.append(page(6,f"""<div style="position:absolute;left:70px;right:70px;top:190px">
<div class=pill>SCREENSHOT THIS</div>
<div class=H style="font-size:96px;margin:30px 0 40px">TUESDAY CHEAT SHEET</div>
""" + ''.join(f"""<div style="display:flex;justify-content:space-between;align-items:center;border-radius:80px;background:#1E1A12;border:3px solid #3A3220;padding:26px 40px;margin-bottom:22px;font-family:MO;font-size:34px"><span>{a}</span><span style="color:{AC}">{b}</span></div>""" for a,b in [('Revenue','≈ $109B'),('Adj. EPS','≈ $2.47'),('Gross margin','74% ± 0.5'),('Q4 guide','growth?'),('CEO update','any name?')]) + """
<div class=ser style="margin-top:34px;font-size:38px">If Nvidia moves, AMD, Broadcom, Micron and TSMC often move with it.</div></div>""",None))
S.append(page(7,f"""<div style="position:absolute;left:70px;right:70px;top:300px;text-align:center">
<div class=H style="font-size:150px"><span class=box>SAVE THIS</span><br>FOR TUESDAY</div>
<div class=ser style="margin-top:60px">Send it to the friend who holds NVDA and checks the stock every hour.</div>
<div class=H style="font-size:64px;margin-top:70px">FOLLOW @THEAIKHABARI</div>
<div class=ser style="font-size:34px;opacity:.8;margin-top:14px">Full breakdown after the bell</div>
<div style="font-family:MO;font-size:22px;opacity:.6;margin-top:80px">Sources: Saxo, StoneX (Bloomberg consensus) · Not financial advice</div></div>""",None))
with sync_playwright() as p:
    b=p.chromium.launch(args=['--allow-file-access-from-files']);pg=b.new_page(viewport={'width':1080,'height':1350})
    for i,h in enumerate(S,1):
        open(f'{D}/s.html','w').write(h);pg.goto(f'file://{D}/s.html');pg.wait_for_timeout(500);pg.screenshot(path=f'{D}/slide{i}.jpg',type='jpeg',quality=92)
from PIL import Image
M=Image.new('RGB',(7*360,450))
for i in range(7):M.paste(Image.open(f'{D}/slide{i+1}.jpg').resize((360,450)),(i*360,0))
M.save(f'{D}/sheet.jpg',quality=85)
