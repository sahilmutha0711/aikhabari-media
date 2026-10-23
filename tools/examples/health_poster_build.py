from playwright.sync_api import sync_playwright
F='file:///mnt/skills/examples/canvas-design/canvas-fonts/'
OUT='/home/claude/car/health'
Y='#FFC24B';K='#14161C';W='#F3EEE4'
CSS=f"""
@font-face{{font-family:Disp;src:url('{F}BricolageGrotesque-Bold.ttf')}}
@font-face{{font-family:Ser;src:url('{F}InstrumentSerif-Italic.ttf')}}
@font-face{{font-family:Mono;font-weight:700;src:url('{F}JetBrainsMono-Bold.ttf')}}
@font-face{{font-family:MonoR;src:url('{F}JetBrainsMono-Regular.ttf')}}
@font-face{{font-family:Sans;src:url('{F}InstrumentSans-Regular.ttf')}}
@font-face{{font-family:Sans;font-weight:700;src:url('{F}InstrumentSans-Bold.ttf')}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;overflow:hidden;background:{W};color:{K};font-family:Sans;position:relative}}
.a{{position:absolute}}.d{{font-family:Disp;letter-spacing:-2.5px;line-height:.98}}.m{{font-family:Mono;font-weight:700}}
.grid{{position:absolute;inset:0;background-image:linear-gradient(rgba(0,0,0,.05) 2px,transparent 2px),linear-gradient(90deg,rgba(0,0,0,.05) 2px,transparent 2px);background-size:54px 54px}}
.hl{{background:{Y};padding:0 12px;border-radius:10px}}
.card{{background:#fff;border:3px solid {K};border-radius:20px;padding:14px 18px}}
.card b{{font-family:Disp;font-size:30px;letter-spacing:-.5px;display:block}}
.card span{{font-size:22px;line-height:1.25;display:block;margin-top:4px;color:#3A3D45}}
.lab{{font-family:Mono;font-weight:700;font-size:20px;letter-spacing:2px;background:{K};color:{Y};padding:6px 14px;border-radius:30px;display:inline-block}}
"""
C=lambda t,s:f'<div class=card><b>{t}</b><span>{s}</span></div>'
body=f"""<div class=grid></div>
<svg class=a style="right:-70px;top:-70px" width="400" height="400" viewBox="0 0 100 100"><path d="M36 6h28v30h30v28H64v30H36V64H6V36h30z" fill="{Y}" stroke="{K}" stroke-width="3"/></svg>
<div class="a m" style="left:56px;top:46px;font-size:20px;letter-spacing:3px">&#9679; THE AI KHABARI</div>
<div class="a m" style="left:56px;top:96px;font-size:19px;letter-spacing:2px;color:#8A5A00">DOCTORS &middot; MEDICAL CODERS &middot; BILLING &middot; PHARMA</div>
<div class="a d" style="left:56px;right:330px;top:138px;font-size:72px">Work in healthcare? Claude has a <span class=hl>medical toolkit</span> now.</div>
<div class="a" style="left:56px;right:330px;top:375px;font-family:Ser;font-size:40px;line-height:1.1">Real medical databases, plugged straight into the chat.</div>
<div class="a" style="left:56px;top:470px"><span class=lab>CONNECTORS &middot; LIVE MEDICAL DATA</span></div>
<div class=a style="left:56px;right:56px;top:520px;display:grid;grid-template-columns:1fr 1fr;gap:14px">
{C('ICD-10','Diagnosis + procedure codes, from CMS and CDC data')}
{C('CMS Coverage','What Medicare covers: for prior auth and claim appeals')}
{C('NPI Registry','Verify any US provider for credentialing and claims')}
{C('PubMed','Search 35M+ biomedical papers and cite them')}
</div>
<div class="a" style="left:56px;top:830px"><span class=lab>AGENT SKILLS &middot; READY-MADE WORKFLOWS</span></div>
<div class=a style="left:56px;right:56px;top:878px;display:grid;grid-template-columns:1fr 1fr;gap:14px">
{C('Prior authorization review','Checks coverage rules against the patient record, drafts a decision')}
{C('Clinical trial protocol','Drafts protocols with endpoints and FDA guidance in mind')}
</div>
<div class=a style="left:56px;right:56px;top:1068px;background:{K};color:{W};border-radius:20px;padding:18px 22px">
 <div class=m style="font-size:18px;color:{Y};letter-spacing:2px">TRY IT (CONNECTORS ON)</div>
 <div style="font-family:MonoR;font-size:23px;line-height:1.38;margin-top:6px">Using CMS Coverage and ICD-10: what documentation does Medicare need to cover <span style="color:{Y}">[procedure]</span> for <span style="color:{Y}">[diagnosis]</span>? List the codes and a prior-auth checklist.</div></div>
<div class="a m" style="left:56px;right:56px;top:1252px;font-size:15px;line-height:1.5;color:#5A5D66">Switch on: claude.ai &rarr; Settings &rarr; Connectors. Pro, Max, Team, Enterprise. Patient data only in a HIPAA-ready (Enterprise) setup. Source: Anthropic, "Claude for Healthcare" (Jan 2026); Help Net Security. Not sponsored. &nbsp;&nbsp;@theaikhabari</div>
"""
html=f"<html><head><meta charset=utf-8><style>{CSS}</style></head><body>{body}</body></html>"
open(f'{OUT}/poster.html','w').write(html)
with sync_playwright() as p:
    b=p.chromium.launch(args=['--allow-file-access-from-files'])
    pg=b.new_page(viewport={'width':1080,'height':1350});pg.goto(f'file://{OUT}/poster.html');pg.wait_for_timeout(700)
    pg.screenshot(path=f'{OUT}/poster.jpg',type='jpeg',quality=94)
print('ok')
