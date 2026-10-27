from playwright.sync_api import sync_playwright
F='file:///mnt/skills/examples/canvas-design/canvas-fonts/'
OUT='/home/claude/car/ads'
CSS=f"""
@font-face{{font-family:Disp;src:url('{F}BigShoulders-Bold.ttf')}}
@font-face{{font-family:Ser;src:url('{F}InstrumentSerif-Italic.ttf')}}
@font-face{{font-family:Mono;font-weight:700;src:url('{F}JetBrainsMono-Bold.ttf')}}
@font-face{{font-family:Sans;src:url('{F}InstrumentSans-Regular.ttf')}}
@font-face{{font-family:Sans;font-weight:700;src:url('{F}InstrumentSans-Bold.ttf')}}
:root{{--bg:#FF5A1F;--ink:#0E0B14;--card:#FFFFFF}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;overflow:hidden;color:var(--ink);font-family:Sans;position:relative;
background:radial-gradient(700px 600px at 90% 5%,#FF8A3D,transparent 70%),radial-gradient(800px 700px at 0% 100%,#E8410F,transparent 70%),var(--bg)}}
.a{{position:absolute}}.d{{font-family:Disp;text-transform:uppercase;line-height:.95}}.s{{font-family:Ser}}.m{{font-family:Mono}}
.top{{position:absolute;left:64px;right:64px;top:50px;display:flex;justify-content:space-between;font-family:Mono;font-weight:700;font-size:22px;letter-spacing:3px}}
.bot{{position:absolute;left:64px;right:64px;bottom:42px;display:flex;justify-content:space-between;font-family:Mono;font-weight:700;font-size:22px}}
.box{{background:var(--ink);color:#fff;padding:0 16px}}
.win{{border-radius:28px;background:#171717;color:#EDEDED;box-shadow:0 40px 90px rgba(80,20,0,.45);overflow:hidden}}
.bar{{height:58px;display:flex;align-items:center;gap:12px;padding:0 24px;border-bottom:1px solid #2A2A2A}}
.dot{{width:15px;height:15px;border-radius:50%}}
.card{{border-radius:24px;background:#fff;padding:30px 34px;box-shadow:0 20px 50px rgba(80,20,0,.25)}}
.tag{{font-family:Mono;font-weight:700;font-size:18px;letter-spacing:2px;padding:5px 12px;border-radius:20px}}
"""
def page(n,N,body,dark=False):
    c='#fff' if dark else 'var(--ink)'
    bg='style="background:radial-gradient(700px 600px at 90% 5%,#2A1A3A,transparent 70%),#0E0B14;color:#fff"' if dark else ''
    return f"""<html><head><meta charset=utf-8><style>{CSS}</style></head><body {bg}>{body}
<div class=top style="color:{c}"><span><span style="color:{'#FF5A1F' if dark else '#fff'}">&#9679;</span> THE AI KHABARI</span><span>{n} / {N}</span></div>
<div class=bot style="color:{c}"><span>@theaikhabari</span><span>{'SAVE THIS' if n==N else 'SWIPE &rarr;'}</span></div></body></html>"""
def win(inner,label='chat'):
    return f'''<div class=win><div class=bar><div class=dot style="background:#FF5F57"></div><div class=dot style="background:#FEBC2E"></div><div class=dot style="background:#28C840"></div><span class=m style="margin-left:12px;font-size:18px;color:#8A8A8A">{label}</span><span class=m style="margin-left:auto;font-size:15px;letter-spacing:2px;color:#6A6A6A">ILLUSTRATION</span></div><div style="padding:26px 28px">{inner}</div></div>'''
S=[]
adwin=win('''<div style="margin-left:auto;max-width:640px;background:#2F2F2F;border-radius:26px 26px 6px 26px;padding:18px 24px;font-size:32px">best CRM for a 10-person startup?</div>
<div style="margin-top:22px;font-size:28px;color:#BDBDBD;line-height:1.4">Here are a few good options for small teams...</div>
<div style="margin-top:18px;border-radius:18px;border:2px solid #FF5A1F;padding:18px 22px;display:flex;gap:18px;align-items:center"><div style="width:64px;height:64px;border-radius:14px;background:#FF5A1F"></div><div><div class=m style="font-size:16px;color:#FF8A5C;letter-spacing:2px">SPONSORED</div><div style="font-size:28px;font-weight:700">YourBrand CRM · try free</div></div><div class=m style="margin-left:auto;font-size:26px;color:#FF8A5C">~$5/click</div></div>''','chatbot answer with an ad')
S.append((f'''<div class="a m" style="left:64px;top:118px;font-size:24px;font-weight:700;letter-spacing:4px">FOR ANYONE WHO PAYS FOR ADS</div>
<div class="a d" style="left:64px;right:40px;top:165px;font-size:150px">Google: $30–50<br>a click.</div>
<div class="a d" style="left:64px;right:40px;top:465px;font-size:150px"><span class=box>ChatGPT: ~$5.</span></div>
<div class=a style="left:70px;right:70px;top:680px;transform:rotate(-1.5deg)">{adwin}</div>
<div class="a s" style="left:64px;right:64px;top:1150px;font-size:58px;color:#fff">Marketers are quietly moving money. Swipe.</div>''',False))
S.append(('''<div class="a m" style="left:64px;top:130px;font-size:24px;font-weight:700;letter-spacing:4px">WHAT HAPPENED</div>
<div class="a d" style="left:64px;right:64px;top:180px;font-size:120px">ChatGPT's ad business just <span class=box>tripled</span></div>
<div class=a style="left:64px;right:64px;top:520px;display:flex;gap:30px;align-items:flex-end">
 <div style="flex:1"><div class=d style="font-size:56px">Late Aug</div><div style="height:120px;background:rgba(14,11,20,.25);border-radius:14px;margin-top:12px"></div><div class=d style="font-size:90px;margin-top:10px">~20K</div></div>
 <div style="flex:1"><div class=d style="font-size:56px">Early Oct</div><div style="height:360px;background:var(--ink);border-radius:14px;margin-top:12px"></div><div class=d style="font-size:90px;margin-top:10px">~60K</div></div></div>
<div class="a" style="left:64px;right:64px;top:1110px;font-size:32px;line-height:1.35">Advertisers on ChatGPT (New Street Research, via The Information). OpenAI cut prices and built a ~140-person ad team, many from Meta.</div>''',False))
S.append(('''<div class="a m" style="left:64px;top:130px;font-size:24px;font-weight:700;letter-spacing:4px">THE PRICE GAP</div>
<div class="a d" style="left:64px;right:64px;top:180px;font-size:100px">Cost per click, <span class=box>business software</span></div>
<div class=a style="left:64px;right:64px;top:540px">
 <div class=d style="font-size:60px">Google search</div><div style="display:flex;align-items:center;gap:20px;margin-top:10px"><div style="height:110px;width:660px;background:var(--ink);border-radius:14px"></div><div class=d style="font-size:80px">$30–50</div></div>
 <div class=d style="font-size:60px;margin-top:50px">ChatGPT</div><div style="display:flex;align-items:center;gap:20px;margin-top:10px"><div style="height:110px;width:110px;background:#fff;border-radius:14px"></div><div class=d style="font-size:80px">~$5</div></div></div>
<div class="a card" style="left:64px;right:64px;top:1000px;font-size:30px;line-height:1.35"><b>The fine print:</b> that's one agency's clients, per The Information. Your price will vary, and a click isn't a customer.</div>''',False))
S.append(('''<div class="a m" style="left:64px;top:130px;font-size:24px;font-weight:700;letter-spacing:4px">MY THEORY (NOT CONFIRMED)</div>
<div class="a d" style="left:64px;right:64px;top:180px;font-size:130px">Cheap clicks <span class=box>won't last</span></div>
<div class=a style="left:64px;right:64px;top:520px;display:flex;flex-direction:column;gap:22px">
 <div class=card style="font-size:40px"><b class=d style="font-size:56px">1.</b> New ad platforms start cheap to pull advertisers in.</div>
 <div class=card style="font-size:40px"><b class=d style="font-size:56px">2.</b> More advertisers = more bidding for the same spots.</div>
 <div class=card style="font-size:40px"><b class=d style="font-size:56px">3.</b> So the early, cheap window may be now.</div></div>
<div class="a s" style="left:64px;right:64px;top:1110px;font-size:44px;color:#fff">What would prove me wrong: prices staying flat as advertisers pile in.</div>''',False))
S.append(('''<div class="a" style="left:64px;top:120px"><span class=tag style="background:#FF5A1F;color:#0E0B14">SCREENSHOT THIS</span></div>
<div class="a d" style="left:64px;right:64px;top:180px;font-size:120px;color:#fff">If you run ads</div>
<div class=a style="left:64px;right:64px;top:340px;display:flex;flex-direction:column;gap:24px;font-size:42px;color:#fff">
 <div style="display:flex;gap:24px"><b class=d style="font-size:64px;color:#FF5A1F">1</b><span>Ask if you can get ChatGPT ads access, and test a <b>small</b> budget first.</span></div>
 <div style="display:flex;gap:24px"><b class=d style="font-size:64px;color:#FF5A1F">2</b><span>Judge by <b>cost per customer</b>, not cost per click.</span></div>
 <div style="display:flex;gap:24px"><b class=d style="font-size:64px;color:#FF5A1F">3</b><span>Write ads as <b>answers</b> to the questions people type.</span></div>
 <div style="display:flex;gap:24px"><b class=d style="font-size:64px;color:#FF5A1F">4</b><span>Keep Google running until the numbers prove the switch.</span></div></div>
<div class="a d" style="left:64px;right:64px;top:1010px;font-size:80px;color:#fff">If you use ChatGPT</div>
<div class="a" style="left:64px;right:64px;top:1100px;font-size:40px;color:#fff">Check whether a suggestion is <b style="color:#FF5A1F">sponsored</b> before you trust it.</div>''',True))
S.append(('''<div class="a d" style="left:64px;right:64px;top:170px;font-size:170px">Save this</div>
<div class="a s" style="left:64px;right:64px;top:350px;font-size:64px;color:#fff">for your next ad budget meeting.</div>
<div class="a card" style="left:64px;right:64px;top:540px;display:flex;align-items:center;gap:28px">
 <svg width=90 height=90 viewBox="0 0 24 24"><path d="M3 11.5L21 3l-8.5 18-2.2-7.3L3 11.5z" fill="#FF5A1F"/></svg>
 <div><div class=m style="font-size:22px;color:#FF5A1F;letter-spacing:2px">SEND THIS TO</div><div class=d style="font-size:64px">your friend in marketing still paying Google $40 a click</div></div></div>
<div class="a d" style="left:64px;right:64px;top:930px;font-size:90px"><span class=box>Follow @theaikhabari</span></div>
<div class="a" style="left:64px;right:64px;top:1060px;font-size:36px">Daily AI news you can actually use.</div>
<div class="a m" style="left:64px;right:64px;top:1230px;font-size:18px">Sources: The Information via Shopifreaks (Oct 15), Quartz/Digiday.</div>''',False))
N=len(S)
with sync_playwright() as p:
    b=p.chromium.launch(args=['--allow-file-access-from-files'])
    for i,(body,dark) in enumerate(S,1):
        open(f'{OUT}/s{i}.html','w').write(page(i,N,body,dark))
        pg=b.new_page(viewport={'width':1080,'height':1350});pg.goto(f'file://{OUT}/s{i}.html');pg.wait_for_timeout(600)
        pg.screenshot(path=f'{OUT}/slide{i}.jpg',type='jpeg',quality=92);pg.close()
    b.close()
from PIL import Image
ims=[Image.open(f'{OUT}/slide{i}.jpg').resize((540,675)) for i in range(1,N+1)]
s=Image.new('RGB',(540*3,675*2),'white')
for i,im in enumerate(ims): s.paste(im,((i%3)*540,(i//3)*675))
s.save('/tmp/claude-0/ads_sheet.jpg',quality=85);print('ok',N)
