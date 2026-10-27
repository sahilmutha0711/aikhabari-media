import sys
from playwright.sync_api import sync_playwright
F='/mnt/skills/examples/canvas-design/canvas-fonts/'
def html(bg,pos,body,dim):
    return f"""<html><head><style>
@font-face{{font-family:B;src:url('file://{F}BricolageGrotesque-Bold.ttf')}}
@font-face{{font-family:W;src:url('file://{F}WorkSans-Bold.ttf')}}
*{{margin:0;padding:0;box-sizing:border-box}}body{{width:1080px;height:1920px;overflow:hidden;background:#0B1030;font-family:W;color:#F4F1EA}}
.bg{{position:absolute;inset:0;background:url('file://{bg}') {pos}/cover;filter:brightness({dim})}}
.g{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(11,16,48,.0) 0%,rgba(11,16,48,.15) 30%,rgba(11,16,48,.85) 55%,#0B1030 80%)}}
.c{{position:absolute;left:70px;right:70px}}
.chip{{display:inline-block;background:#FF6B5A;color:#fff;border-radius:40px;padding:10px 28px;font-size:34px;letter-spacing:4px}}
h1{{font-family:B;font-size:128px;line-height:.95;letter-spacing:-3px;margin-top:26px;text-shadow:0 8px 40px rgba(0,0,0,.6)}}
.am{{color:#FFB400}}.co{{color:#FF6B5A}}
.box{{display:inline-block;background:#FFB400;color:#0B1030;border-radius:22px;padding:10px 30px;font-family:B;font-size:76px;margin-top:34px}}
.brand{{position:absolute;left:70px;top:1620px;font-size:30px;letter-spacing:6px;color:#D9D6E8}}.brand b{{color:#FFB400}}
</style></head><body><div class=bg></div><div class=g></div>{body}<div class=brand><b>●</b> THE AI KHABARI</div></body></html>"""
covers={
 'cai':('/home/claude/reels/cai/bg.jpg','center top',.8,"<div class='c' style='top:820px'><span class=chip>BREAKING</span><h1><span class=am>Character.AI</span> just went <span class=co>bankrupt</span></h1><div class=box>Disney bids $20M</div></div>"),
 'linus':('/home/claude/reels/linus/bg.jpg','center top',.95,"<div class='c' style='top:860px'><span class=chip>AI + LINUX</span><h1 style=font-size:114px>The man behind <span class=am>Linux</span> just coded with AI</h1><div class=box>3X FASTER</div></div>")}
with sync_playwright() as p:
    b=p.chromium.launch(args=['--allow-file-access-from-files'])
    for k,(bg,pos,dim,body) in covers.items():
        open(f'{k}.html','w').write(html(bg,pos,body,dim));pg=b.new_page(viewport={'width':1080,'height':1920})
        pg.goto(f'file:///home/claude/covers/{k}.html');pg.wait_for_timeout(600);pg.screenshot(path=f'{k}_cover.jpg',type='jpeg',quality=92);pg.close()
    b.close()
