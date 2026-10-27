import json,sys
from playwright.sync_api import sync_playwright
R='/home/claude/reels/agi_owner'
with sync_playwright() as p:
    b=p.chromium.launch(args=['--allow-file-access-from-files'])
    for mode in ['short','long']:
        d=json.load(open(f'{R}/work/edit_{mode}.json'))
        h=open(f'{R}/tpl.html').read()
        for k,v in {'__WORDS__':json.dumps(d['words']),'__TOTAL__':str(round(d['duration'],2)),'__DIR__':'file://'+R}.items():h=h.replace(k,v)
        open(f'{R}/reel_{mode}.html','w').write(h)
        pg=b.new_page();pg.goto(f'file://{R}/reel_{mode}.html');pg.wait_for_timeout(500)
        bi=pg.evaluate('BINT()');json.dump(bi,open(f'{R}/work/bint_{mode}.json','w'));print(mode,[(round(a,2),round(c,2)) for a,c,_ in bi])
