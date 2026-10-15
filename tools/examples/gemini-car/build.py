from playwright.sync_api import sync_playwright
F='file:///mnt/skills/examples/canvas-design/canvas-fonts/'
D='file:///home/claude/car/gemini/'
CSS=f"""
@font-face{{font-family:Disp;src:url('{F}Outfit-Bold.ttf')}}
@font-face{{font-family:Ser;src:url('{F}Lora-Italic.ttf')}}
@font-face{{font-family:Mono;src:url('{F}RedHatMono-Regular.ttf')}}
@font-face{{font-family:Sans;src:url('{F}InstrumentSans-Regular.ttf')}}
@font-face{{font-family:Sans;font-weight:700;src:url('{F}InstrumentSans-Bold.ttf')}}
:root{{--bg:#0F1214;--sf:#171B1E;--tx:#F2F2EF;--ac:#5DD6B0;--a2:#5DD6B0;--dim:#9AA3A6}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;overflow:hidden;background:var(--bg);color:var(--tx);font-family:Sans;position:relative}}
.a{{position:absolute}}
.d{{font-family:Disp;letter-spacing:-2px;line-height:1.0}}
.s{{font-family:Ser;font-style:italic;line-height:1.1}}
.m{{font-family:Mono}}
.top{{position:absolute;left:70px;right:70px;top:56px;display:flex;justify-content:space-between;font-family:Mono;font-size:24px;letter-spacing:4px}}
.bot{{position:absolute;left:70px;right:70px;bottom:44px;display:flex;justify-content:space-between;font-family:Mono;font-size:20px;color:var(--dim)}}
.card{{border-radius:28px;background:var(--sf);border:1.5px solid #262C30;backdrop-filter:blur(6px);padding:30px 34px}}
.chip{{display:inline-block;padding:10px 26px;border-radius:40px;font-family:Mono;font-size:26px;letter-spacing:3px}}
.grain{{position:absolute;inset:0;opacity:.05;mix-blend-mode:overlay;pointer-events:none}}
"""
MESH0=['background:radial-gradient(700px 700px at 20% 15%,#00D4FF,transparent 70%),radial-gradient(800px 800px at 90% 85%,#00F0C0,transparent 70%),#0047E0','background:radial-gradient(800px 800px at 85% 10%,#00D4FF,transparent 70%),radial-gradient(700px 700px at 10% 90%,#0020A0,transparent 70%),#0047E0','background:radial-gradient(800px 800px at 15% 85%,#00D4FF,transparent 70%),radial-gradient(700px 700px at 90% 20%,#00F0C0,transparent 65%),#0038C8']
MESH=['background:radial-gradient(900px 700px at 10% 0%,rgba(93,214,176,.10),transparent 70%),radial-gradient(900px 800px at 100% 100%,rgba(80,140,200,.07),transparent 70%),#0F1214','background:radial-gradient(900px 700px at 90% 0%,rgba(93,214,176,.09),transparent 70%),#0F1214','background:radial-gradient(1000px 800px at 0% 100%,rgba(93,214,176,.08),transparent 70%),#0F1214']
BRIGHT='linear-gradient(180deg,#F6F4EF,#ECE8DF)'
SUN='background:radial-gradient(800px 800px at 20% 15%,#FF2E63,transparent 70%),radial-gradient(800px 800px at 85% 90%,#FF9500,transparent 70%),#FF4D2E'
def page(n,N,body,light=False,credit=''):
    c='#121414' if light else 'var(--tx)'
    return f"""<html><head><meta charset=utf-8><style>{CSS}</style></head><body style="{'background:'+BRIGHT+';color:#121414' if light else MESH[n%len(MESH)]}">{body}
<svg class=grain width=1080 height=1350><filter id=n><feTurbulence type=fractalNoise baseFrequency=.9 numOctaves=2 seed={n}/></filter><rect width=100% height=100% filter=url(#n)/></svg>
<div class=top style="color:{c}"><span><span style="color:{'#138A6B' if light else 'var(--ac)'}">&#9679;</span> THE AI KHABARI</span><span>{n} / {N}</span></div>
<div class=bot style="{'color:#6B6B66' if light else ''}"><span style="color:{c};font-weight:700">@theaikhabari</span><span>{credit}</span></div></body></html>"""
S=[]
# 1 cover
S.append(("""
<div class="a d" style="left:0;right:0;top:120px;text-align:center;font-size:230px;color:#fff;">GEMINI 4</div>
<div class=a style="left:190px;top:400px;width:700px;height:700px;border-radius:50%;background:radial-gradient(circle at 35% 30%,#3E8F7C,#1F5247 55%,#15302B)"></div><div class=a style="left:0;right:0;top:360px;height:780px;background:url(D/pichai_cut.png) center top/auto 780px no-repeat;filter:drop-shadow(0 30px 50px rgba(0,0,0,.5))"></div>
<div class=a style="left:0;right:0;top:820px;height:530px;background:linear-gradient(180deg,rgba(15,18,20,0),#0F1214 40%)"></div>
<div class="a" style="left:70px;top:900px"><span class=chip style="background:var(--ac);color:#0F1214">NEW MODEL</span> <span class=chip style="border:2px solid var(--ac);color:var(--ac)">AI</span></div>
<div class="a d" style="left:70px;right:70px;top:975px;font-size:88px">Google's new AI is out</div>
<div class="a s" style="left:70px;right:70px;top:1080px;font-size:50px;color:var(--ac)">at half the API price of Claude's top model</div>""",False,'Photo: Lukasz Kobus / EC, CC BY 4.0'))
# 2 what / where
rows=[('Gemini app','Google AI Pro + Ultra'),('AI Mode in Search','Pro + Ultra'),('Antigravity (coding)','Ultra only'),('Gemini API','Developers, pay per use')]
S.append((f"""
<div class="a m" style="left:70px;top:170px;font-size:28px;letter-spacing:5px;color:var(--a2)">ROLLED OUT OCT 13</div>
<div class="a d" style="left:70px;right:70px;top:220px;font-size:92px">Gemini 4 <span style="color:var(--ac)">Argon</span></div>
<div class="a s" style="left:70px;right:70px;top:330px;font-size:48px;color:var(--dim)">Google's newest frontier model. Here's where you get it:</div>
<div class=a style="left:70px;right:70px;top:480px">{''.join(f'<div class=card style="display:flex;justify-content:space-between;align-items:center;margin-bottom:22px"><span class=d style="font-size:50px;letter-spacing:-1px">{a}</span><span class=m style="font-size:28px;color:var(--a2)">{b}</span></div>' for a,b in rows)}</div>
<div class="a m" style="left:70px;right:70px;top:1180px;font-size:28px;color:#fff;font-weight:700">No free tier. Swipe for the price war &rarr;</div>""",False,'Sources: Tech Insider, Cryptopolitan'))
# 3 price war
bars=[('Gemini 4 Argon*','$2','$10',10,'#5DD6B0'),('Claude Opus 5.5','$4','$20',20,'#C9CFCC'),('GPT-6 Astra','$10','$50',50,'#6E7679')]
S.append((f"""
<div class="a m" style="left:70px;top:170px;font-size:28px;letter-spacing:5px;color:var(--a2)">THE PRICE WAR</div>
<div class="a d" style="left:70px;right:70px;top:220px;font-size:84px">Cost per 1M output tokens</div>
<div class=a style="left:70px;right:70px;top:440px">{''.join(f'<div style="margin-bottom:46px"><div style="display:flex;justify-content:space-between;font-size:38px;font-weight:700;margin-bottom:12px"><span>{n}</span><span class=m style="color:var(--dim);font-size:28px">input {i}</span></div><div style="height:96px;border-radius:18px;background:{c};width:{max(18,w/50*100)}%;display:flex;align-items:center;padding-left:26px;color:#121414"><span class=d style="font-size:56px">{o}</span></div></div>' for n,i,o,w,c in bars)}</div>
<div class="a m" style="left:70px;right:70px;top:1130px;font-size:26px;line-height:1.5;color:var(--dim)">*Intro price until Nov 30, then $4 in / $20 out. API prices, as reported.</div>""",False,'Source: Cryptopolitan'))
# 4 how good
S.append(("""
<div class="a m" style="left:70px;top:170px;font-size:28px;letter-spacing:5px;color:var(--a2)">HOW GOOD IS IT?</div>
<div class="a d" style="left:70px;right:70px;top:220px;font-size:84px">Close to the top. Not #1.</div>
<div class="a card" style="left:70px;right:70px;top:430px"><div class=m style="font-size:24px;color:var(--dim)">ARTIFICIAL ANALYSIS INTELLIGENCE INDEX</div>
<div style="display:flex;gap:30px;margin-top:18px;align-items:baseline"><span class=d style="font-size:120px;color:var(--ac)">53</span><span style="font-size:36px">ties GPT-6 Astra.<br>Claude Opus 5.5 still ~5 points ahead.</span></div></div>
<div class="a card" style="left:70px;right:70px;top:790px"><div class=m style="font-size:24px;color:var(--dim)">PROMPT-INJECTION ATTACKS THAT WORKED (lower = safer)</div>
<div style="display:flex;justify-content:space-between;margin-top:22px">
<div><div class=d style="font-size:80px;color:var(--ac)">0.7%</div><div style="font-size:28px">Argon</div></div>
<div><div class=d style="font-size:80px">1.0%</div><div style="font-size:28px">Opus 5.5</div></div>
<div><div class=d style="font-size:80px;color:#E58C7A">8.5%</div><div style="font-size:28px">GPT-6 Astra</div></div></div></div>""",False,'Source: Cryptopolitan (Artificial Analysis, Gray Swan)'))
# 5 superpower
S.append(("""<style>.top,.top span,.bot,.bot span{color:#121414!important}</style><div class=a style="inset:0;background:BRIGHTBG"></div>
<div class="a m" style="left:70px;top:170px;font-size:28px;letter-spacing:5px;color:#138A6B;font-weight:700">ITS SUPERPOWER</div>
<div class="a d" style="left:0;right:0;top:300px;text-align:center;font-size:330px;color:#138A6B">1M</div>
<div class="a d" style="left:70px;right:70px;top:650px;text-align:center;font-size:72px;color:#121414">tokens in a single answer</div>
<div class="a s" style="left:120px;right:120px;top:800px;text-align:center;font-size:50px;color:#55554F">That's roughly 750,000 words. Full reports, whole codebases, entire books, in one go.</div>""",False,'Source: Google via Tech Insider'))
# 6 catch
items=['No free tier. You need Google AI Pro or Ultra.','The coding app, Antigravity, is Ultra only.',"Google's 14-of-18 benchmark wins are its own table.",'The cheap API price ends Nov 30.']
S.append((f"""
<div class="a d" style="left:70px;top:190px;font-size:130px;color:#fff">The catch<span style="color:#E58C7A">.</span></div>
<div class=a style="left:70px;right:70px;top:420px">{''.join(f'<div class="card m" style="margin-bottom:22px;font-size:36px;line-height:1.35;border-color:#262C30;background:#171B1E"><span style="color:var(--ac)">[!]</span> {x}</div>' for x in items)}</div>""",False,'Sources: Tech Insider, Cryptopolitan'))
# 7 takeaways (light)
S.append(("""<div class="a m" style="left:70px;top:170px;font-size:28px;letter-spacing:5px;color:#138A6B;font-weight:700">WHAT YOU CAN TAKE FROM THIS</div>
<div class=a style="left:70px;right:70px;top:240px">
<div style="display:flex;gap:26px;align-items:flex-start;margin-bottom:34px"><div class=d style="flex:none;width:70px;height:70px;border-radius:50%;background:#121414;color:#F6F4EF;font-size:40px;display:flex;align-items:center;justify-content:center">1</div><div style="font-size:40px;line-height:1.3">Already pay for Google AI Pro? Try Argon on your <b>longest</b> task: a full report, a big doc, a whole plan.</div></div>
<div style="display:flex;gap:26px;align-items:flex-start;margin-bottom:34px"><div class=d style="flex:none;width:70px;height:70px;border-radius:50%;background:#121414;color:#F6F4EF;font-size:40px;display:flex;align-items:center;justify-content:center">2</div><div style="font-size:40px;line-height:1.3">Building with AI? Test it <b>before Nov 30</b>, while the API price is half.</div></div>
<div style="display:flex;gap:26px;align-items:flex-start"><div class=d style="flex:none;width:70px;height:70px;border-radius:50%;background:#121414;color:#F6F4EF;font-size:40px;display:flex;align-items:center;justify-content:center">3</div><div style="font-size:40px;line-height:1.3">Copy this prompt for long answers:</div></div>
<div class=m style="margin-top:22px;font-size:31px;line-height:1.5;background:#121414;color:#fff;border-radius:20px;padding:28px 30px;border:3px dashed #121414">Read this whole document and write a complete section-by-section report. Don't summarize. Cover every section in full, with headings.</div></div>""",True,''))
# 8 CTA
S.append(("""<style>.top,.top span,.bot,.bot span{color:#121414!important}</style><div class=a style="inset:0;background:BRIGHTBG"></div>
<div class="a d" style="left:70px;right:70px;top:260px;font-size:110px;color:#121414">Which AI do you actually pay for?</div>
<div class="a s" style="left:70px;right:70px;top:540px;font-size:60px;color:#55554F">Tell me in the comments.</div>
<div class=a style="left:70px;top:720px"><div class=chip style="background:#121414;color:#F6F4EF;font-size:30px;padding:16px 32px">SEND TO THE FRIEND PAYING FOR 3 AI APPS</div></div>
<div class=a style="left:70px;top:830px"><div class=chip style="border:3px solid #121414;color:#121414;font-size:30px;padding:16px 32px">FOLLOW @THEAIKHABARI</div></div>
<div class="a m" style="left:70px;right:70px;top:1120px;font-size:22px;line-height:1.5;color:#55554F">Sources: Tech Insider (citing Ars Technica, The Verge, Engadget, 9to5Google), Cryptopolitan, Google blog. Prices as reported, Oct 2026.</div>""",False,''))
N=len(S)
with sync_playwright() as p:
    b=p.chromium.launch(args=['--allow-file-access-from-files'])
    for i,(body,light,cred) in enumerate(S,1):
        open(f'/home/claude/car/gemini/s{i}.html','w').write(page(i,N,body.replace('url(D/',f'url({D}').replace('BRIGHTBG',BRIGHT),light,cred))
        pg=b.new_page(viewport={'width':1080,'height':1350});pg.goto(f'file:///home/claude/car/gemini/s{i}.html');pg.wait_for_timeout(700)
        ov=pg.evaluate("()=>[...document.querySelectorAll('*')].filter(e=>e.scrollWidth>e.clientWidth+2&&getComputedStyle(e).overflow!='visible').length")
        pg.screenshot(path=f'/home/claude/car/gemini/slide{i}.jpg',type='jpeg',quality=92);pg.close()
    b.close()
from PIL import Image
ims=[Image.open(f'/home/claude/car/gemini/slide{i}.jpg').resize((540,675)) for i in range(1,N+1)]
s=Image.new('RGB',(540*4,675*2))
for i,im in enumerate(ims): s.paste(im,((i%4)*540,(i//4)*675))
s.save('/tmp/claude-0/gem_sheet.jpg',quality=85);print('ok')
