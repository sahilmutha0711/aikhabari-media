from playwright.sync_api import sync_playwright
F='file:///mnt/skills/examples/canvas-design/canvas-fonts/'
OUT='/home/claude/car/health2'
K='#1C1530';A='#6B3DF0';P='#FF8A65'
CSS=f"""
@font-face{{font-family:Disp;src:url('{F}BricolageGrotesque-Bold.ttf')}}
@font-face{{font-family:Ser;src:url('{F}InstrumentSerif-Italic.ttf')}}
@font-face{{font-family:Mono;font-weight:700;src:url('{F}JetBrainsMono-Bold.ttf')}}
@font-face{{font-family:MonoR;src:url('{F}JetBrainsMono-Regular.ttf')}}
@font-face{{font-family:Sans;src:url('{F}InstrumentSans-Regular.ttf')}}
@font-face{{font-family:Sans;font-weight:700;src:url('{F}InstrumentSans-Bold.ttf')}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;overflow:hidden;color:{K};font-family:Sans;position:relative;background:#FFF6EF}}
.mesh{{position:absolute;inset:-10%;filter:blur(60px)}}
.grain{{position:absolute;inset:0;opacity:.10;mix-blend-mode:multiply}}
.a{{position:absolute}}.d{{font-family:Disp;letter-spacing:-3px;line-height:.98}}.s{{font-family:Ser}}.m{{font-family:Mono;font-weight:700}}
.top{{position:absolute;left:64px;right:64px;top:52px;display:flex;justify-content:space-between;font-family:Mono;font-weight:700;font-size:21px;letter-spacing:3px;z-index:5}}
.bot{{position:absolute;left:64px;right:64px;bottom:44px;display:flex;justify-content:space-between;font-family:Mono;font-weight:700;font-size:21px;z-index:5}}
.glass{{background:rgba(255,255,255,.62);backdrop-filter:blur(18px);border:1.5px solid rgba(255,255,255,.9);border-radius:36px;box-shadow:0 24px 60px rgba(60,30,90,.14)}}
.chip{{display:inline-block;font-family:Mono;font-weight:700;font-size:20px;letter-spacing:2px;background:{K};color:#fff;padding:8px 16px;border-radius:30px}}
.hl{{background:{K};color:#fff;padding:0 16px;border-radius:14px}}
.ic{{width:92px;height:92px;border-radius:26px;display:flex;align-items:center;justify-content:center;font-family:Disp;font-size:40px;color:#fff}}
.k{{font-family:Disp;font-size:60px;letter-spacing:-1.5px}}
.t{{font-size:36px;line-height:1.3;color:#3B3350}}
.ex{{font-family:MonoR;font-size:28px;line-height:1.4;color:{A};margin-top:14px}}
"""
GRAIN='<svg class=grain width="1080" height="1350"><filter id=n><feTurbulence type=fractalNoise baseFrequency=.9 numOctaves=3 stitchTiles=stitch/><feColorMatrix values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 .55 0"/></filter><rect width=100% height=100% filter=url(#n)/></svg>'
MESHES=[
 [('#FF9E80',8,12,48),('#B69CFF',92,18,50),('#FFD66B',25,95,50),('#FFF6EF',70,60,45)],
 [('#B69CFF',10,8,48),('#FFB59E',95,45,48),('#FFE7A0',15,92,50),('#FFF6EF',55,50,40)],
 [('#FFD66B',90,8,45),('#FF9E80',5,55,48),('#C7B4FF',85,95,55),('#FFF6EF',50,40,40)],
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
S.append(f"""<div class=a style="left:64px;top:130px"><span class=chip>FOR DOCTORS &middot; MEDICAL CODERS &middot; BILLING</span></div>
<div class="a d" style="left:64px;right:64px;top:200px;font-size:118px">Work in healthcare? Claude has a <span class=hl>medical toolkit</span> now.</div>
<div class="a glass" style="left:64px;right:64px;top:860px;padding:30px 36px">
 <div class=m style="font-size:20px;letter-spacing:2px;color:{A}">PLUGGED STRAIGHT INTO THE CHAT</div>
 <div style="display:flex;gap:16px;margin-top:18px;flex-wrap:wrap">
 {''.join(f'<span style="font-family:Disp;font-size:40px;background:#fff;border-radius:18px;padding:10px 22px">{x}</span>' for x in ['ICD-10','CMS Coverage','NPI Registry','PubMed'])}</div>
 <div class=s style="font-size:44px;margin-top:22px">Real medical databases. No copy-paste.</div></div>""")
S.append(f"""<div class=a style="left:64px;top:130px"><span class=chip>CONNECTORS &middot; 1 / 2</span></div>
<div class="a d" style="left:64px;right:64px;top:200px;font-size:84px">Codes and coverage, in seconds</div>
<div class=a style="left:64px;right:64px;top:430px;display:flex;flex-direction:column;gap:40px">
{tool('#','#6B3DF0','ICD-10','Look up diagnosis and procedure codes, from CMS and CDC data.','"Which ICD-10 code fits type 2 diabetes with kidney disease?"')}
{tool('&#10003;','#FF7A59','CMS Coverage','What Medicare covers: local and national coverage rules for prior auth and appeals.','"What does Medicare require to cover a knee MRI?"')}
</div><div class="a s" style="left:64px;right:64px;top:1185px;font-size:46px;line-height:1.1">Fewer denied claims start with the right code.</div>""")
S.append(f"""<div class=a style="left:64px;top:130px"><span class=chip>CONNECTORS &middot; 2 / 2</span></div>
<div class="a d" style="left:64px;right:64px;top:200px;font-size:84px">Providers and research, verified</div>
<div class=a style="left:64px;right:64px;top:430px;display:flex;flex-direction:column;gap:40px">
{tool('ID','#1C1530','NPI Registry','Verify any US provider for credentialing, directories and claims.','"Check the NPI and specialty for Dr. [name], [city]"')}
{tool('&#9783;','#E0A100','PubMed','Search 35M+ biomedical papers and get answers with citations.','"Latest trials on GLP-1 drugs and sleep apnea, with links"')}
</div><div class="a s" style="left:64px;right:64px;top:1185px;font-size:46px;line-height:1.1">Every answer with a source you can check.</div>""")
S.append(f"""<div class=a style="left:64px;top:130px"><span class=chip>AGENT SKILLS &middot; READY-MADE WORKFLOWS</span></div>
<div class="a d" style="left:64px;right:64px;top:200px;font-size:84px">Hours of paperwork, as one skill</div>
<div class=a style="left:64px;right:64px;top:430px;display:flex;flex-direction:column;gap:40px">
{tool('PA','#FF7A59','Prior auth review','Cross-checks coverage rules and clinical guidelines against the patient record, then proposes a decision for review.','For payers and provider billing teams')}
{tool('CT','#6B3DF0','Trial protocol draft','Drafts a clinical trial protocol with endpoint ideas, with FDA guidance and the regulatory path in mind.','For pharma and research teams')}
</div>""")
S.append(f"""<div class=a style="left:64px;top:130px"><span class=chip>TRY IT &middot; CONNECTORS ON</span></div>
<div class="a d" style="left:64px;right:64px;top:200px;font-size:84px">One prompt, two databases</div>
<div class="a glass" style="left:64px;right:64px;top:440px;overflow:hidden;background:rgba(28,21,48,.92);border-color:rgba(255,255,255,.2)">
 <div style="display:flex;gap:10px;align-items:center;padding:18px 28px;border-bottom:1.5px solid rgba(255,255,255,.15)"><i style="width:18px;height:18px;border-radius:9px;background:#FF5F57"></i><i style="width:18px;height:18px;border-radius:9px;background:#FEBC2E"></i><i style="width:18px;height:18px;border-radius:9px;background:#28C840"></i><span class=m style="color:#C9B6FF;font-size:21px;margin-left:12px">Claude</span></div>
 <div style="font-family:MonoR;font-size:34px;line-height:1.45;padding:30px 34px;color:#fff">Using the CMS Coverage and ICD-10 connectors: what documentation does Medicare need to cover <b style="color:#FFB199">[procedure]</b> for <b style="color:#FFB199">[diagnosis]</b>?<br><br>Give me the matching codes and a prior-auth checklist I can tick off.</div></div>
<div class="a s" style="left:64px;right:64px;top:1100px;font-size:44px;line-height:1.1">Answers come from the real coverage rules, not memory.</div>""")
S.append(f"""<div class=a style="left:64px;top:130px"><span class=chip>SWITCH IT ON</span></div>
<div class="a glass" style="left:64px;right:64px;top:210px;padding:36px 40px;font-size:38px;line-height:1.6">
<b>1.</b> claude.ai &rarr; Settings &rarr; <b>Connectors</b><br><b>2.</b> Add ICD-10, CMS Coverage, NPI, PubMed<br><b>3.</b> Ask in plain English</div>
<div class="a t" style="left:64px;right:64px;top:600px;font-size:28px">Pro, Max, Team, Enterprise. Patient data only in a HIPAA-ready (Enterprise) setup.</div>
<div class="a d" style="left:64px;right:64px;top:700px;font-size:72px">Know someone in <span class=hl>healthcare</span>? Send this to them.</div>
<div class="a glass" style="left:64px;right:64px;top:900px;padding:26px 34px">
 <div class="s" style="font-size:42px;line-height:1.1">In healthcare yourself?</div>
 <div style="font-family:Disp;font-size:44px;letter-spacing:-1px;margin-top:10px"><span style="background:#1C1530;color:#fff;padding:2px 14px;border-radius:12px">Save this</span> + follow <span style="color:#6B3DF0">@theaikhabari</span></div>
 <div class=t style="font-size:28px;margin-top:8px">New AI tools for your field, every week.</div></div>
<div class="a m" style="left:64px;right:64px;top:1180px;font-size:17px;line-height:1.5;color:#5B536E">Source: Anthropic, "Advancing Claude in healthcare and the life sciences" (Jan 2026); Help Net Security. Example questions are ours. Not medical advice. Not sponsored.</div>""")
N=len(S)
with sync_playwright() as p:
    b=p.chromium.launch(args=['--allow-file-access-from-files'])
    for i,body in enumerate(S,1):
        open(f'{OUT}/s{i}.html','w').write(page(i,N,body))
        pg=b.new_page(viewport={'width':1080,'height':1350});pg.goto(f'file://{OUT}/s{i}.html');pg.wait_for_timeout(700)
        pg.screenshot(path=f'{OUT}/slide{i}.jpg',type='jpeg',quality=93)
print('ok',N)
