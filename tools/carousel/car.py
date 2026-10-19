# usage: python3 car.py spec.json outdir   -> renders slide1..N.jpg, prints checks
# needs: pip install playwright "opencv-python==4.11.0.86" requests pillow; python3 -m playwright install chromium
# fonts: ./fonts/Bricolage.ttf, ./fonts/DMSans.ttf next to this file (setup.sh downloads them)
import json,sys,os,time,requests,cv2
from PIL import Image,ImageFilter
from playwright.sync_api import sync_playwright
SP=json.load(open(sys.argv[1]));OUT=sys.argv[2];os.makedirs(OUT,exist_ok=True)
HERE=os.path.dirname(os.path.abspath(__file__))
H={'User-Agent':'AIKhabariBot/1.0 (https://instagram.com/theaikhabari)'}
cc=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml');cc2=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_alt2.xml')
def fetch(title,key):
    p=f'{OUT}/src_{key}.jpg'
    if os.path.exists(p): return p
    for a in range(4):
        try:
            r=requests.get('https://commons.wikimedia.org/w/api.php',params={'action':'query','titles':'File:'+title,'prop':'imageinfo','iiprop':'url|size','iiurlwidth':2000,'format':'json'},headers=H,timeout=30).json()
            ii=list(r['query']['pages'].values())[0]['imageinfo'][0]
            c=requests.get(ii.get('thumburl',ii['url']),headers=H,timeout=60)
            if c.status_code==200: open(p,'wb').write(c.content);Image.open(p).convert('RGB').save(p,quality=95);return p
        except Exception: pass
        time.sleep(5)
    raise SystemExit('fetch failed '+title)
def crop(src,dst,FH,face=True,tw=400,cyf=.45,blur=0,xoff=0):
    im=Image.open(src).convert('RGB');W,Hh=im.size;fc=None
    if face:
        g=cv2.cvtColor(cv2.imread(src),cv2.COLOR_BGR2GRAY);f=cc.detectMultiScale(g,1.1,6,minSize=(int(W*.06),int(W*.06)))
        if not len(f): f=cc2.detectMultiScale(g,1.05,4,minSize=(int(W*.1),int(W*.1)))
        if len(f): x,y,w,h=sorted(f,key=lambda r:-r[2])[0];fc=(x+w/2,y+h/2,w)
    if fc: cx,cy,fw=fc;s=max(tw/fw,1080/W,FH/Hh)
    else: cx,cy,fw=W/2+xoff,Hh/2,0;s=max(1080/W,FH/Hh)
    cw,ch=1080/s,FH/s;x0=min(max(cx-540/s,0),W-cw)
    y0=min(max(cy-(cyf*FH)/s,0),Hh-ch) if fc else (min(Hh*.06,Hh-ch) if face else (Hh-ch)/2)
    out=im.crop((int(x0),int(y0),int(x0+cw),int(y0+ch))).resize((1080,FH),Image.LANCZOS)
    if blur: out=out.filter(ImageFilter.GaussianBlur(blur))
    out.save(dst,quality=92);return (round(s,2), int((cy-y0)*s+fw*s*.65) if fc else None)
CSS=open(f'{HERE}/car.css').read().replace('FONTDIR',HERE+'/fonts/')
def page(n,N,bg,grad,body,credit):
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body><div class='s'>{bg}<div class='ov' style='background:{grad}'></div><div class='ov' style='background:radial-gradient(700px 500px at 90% 8%,rgba(124,108,255,.28),transparent 70%)'></div><div class='ov' style='background:linear-gradient(180deg,rgba(11,16,48,.7),transparent 13%)'></div>{body}<div class='top'><span><b>●</b> THE AI KHABARI</span><span>{n} / {N}</span></div><div class='bot'><span class='h'>@theaikhabari</span><span>{credit}</span></div></div></body></html>"
N=len(SP['slides']);report=[]
for i,sl in enumerate(SP['slides'],1):
    src=fetch(sl['img'],sl['key']);kind=sl.get('kind','person')
    if kind in('person','hook'):
        FH=sl.get('fh',900 if kind=='hook' else 720)
        sc,chin=crop(src,f'{OUT}/f{i}.jpg',FH,True,sl.get('tw',440 if kind=='hook' else 380),sl.get('cyf',.45))
        bg=f"<div class='ph' style=\"background-image:url('file://{OUT}/f{i}.jpg');bottom:auto;height:{FH}px\"></div>"
        grad=f'linear-gradient(180deg,rgba(11,16,48,0) {int(FH*.6)}px,rgba(11,16,48,.85) {FH-40}px,#0B1030 {FH}px)'
    else:
        sc,chin=crop(src,f'{OUT}/f{i}.jpg',1350,False,blur=sl.get('blur',0),xoff=sl.get('xoff',0))
        bg=f"<div class='ph' style=\"background-image:url('file://{OUT}/f{i}.jpg')\"></div>"
        grad=sl.get('grad','linear-gradient(180deg,rgba(11,16,48,.1) 25%,rgba(11,16,48,.6) 42%,rgba(11,16,48,.93) 56%,#0B1030 72%)')
    open(f'{OUT}/s{i}.html','w').write(page(i,N,bg,grad,sl['body'],sl['credit']));report.append((i,kind,sc,chin))
with sync_playwright() as p:
    b=p.chromium.launch(args=['--disable-dev-shm-usage','--disable-gpu','--allow-file-access-from-files','--renderer-process-limit=1'])
    for (i,kind,sc,chin) in report:
        pg=b.new_page(viewport={'width':1080,'height':1350});pg.goto(f'file://{OUT}/s{i}.html');pg.wait_for_timeout(700)
        ov=pg.evaluate("()=>[...document.querySelectorAll('.c *')].filter(e=>e.scrollWidth>e.clientWidth+2).length")
        top=pg.evaluate("()=>{const c=[...document.querySelectorAll('.c')];return c[c.length-1].getBoundingClientRect().top}")
        bot=pg.evaluate("()=>Math.max(...[...document.querySelectorAll('.c')].map(e=>e.getBoundingClientRect().bottom))")
        pg.screenshot(path=f'{OUT}/slide{i}.jpg',type='jpeg',quality=92);pg.close()
        flag='' if (chin is None or chin<top-10) else ' !!FACE-UNDER-TEXT'
        print(i,kind,'scale',sc,'chin',chin,'text',int(top),'-',int(bot),'overflow',ov,flag+(' !!LOW' if bot>1250 else '')+(' !!UPSCALE' if sc and sc>1.3 else ''))
    b.close()
