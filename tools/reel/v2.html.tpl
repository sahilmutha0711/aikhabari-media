<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{font-family:Disp;src:url('file:///mnt/skills/examples/canvas-design/canvas-fonts/Boldonse-Regular.ttf')}
@font-face{font-family:Ser;font-style:italic;src:url('file:///mnt/skills/examples/canvas-design/canvas-fonts/InstrumentSerif-Italic.ttf')}
@font-face{font-family:Ser;src:url('file:///mnt/skills/examples/canvas-design/canvas-fonts/InstrumentSerif-Regular.ttf')}
@font-face{font-family:Mono;src:url('file:///mnt/skills/examples/canvas-design/canvas-fonts/JetBrainsMono-Regular.ttf')}
@font-face{font-family:Mono;font-weight:700;src:url('file:///mnt/skills/examples/canvas-design/canvas-fonts/JetBrainsMono-Bold.ttf')}
@font-face{font-family:Sans;font-weight:700;src:url('file:///mnt/skills/examples/canvas-design/canvas-fonts/InstrumentSans-Bold.ttf')}
@font-face{font-family:Sans;font-weight:400;src:url('file:///mnt/skills/examples/canvas-design/canvas-fonts/InstrumentSans-Regular.ttf')}
:root{--ink:#12100E;--ink2:#1D1A17;--cream:#F3EDE2;--clay:#E2704A;--mint:#6EE7A8;--red:#FF5F57;--dim:#8A8178}
*{margin:0;padding:0;box-sizing:border-box}
body{width:1080px;height:1920px;overflow:hidden;background:var(--ink);font-family:Sans;color:var(--cream)}
#cam{position:absolute;inset:0;transform-origin:50% 45%}
.abs{position:absolute}
.disp{font-family:Disp;line-height:1.32;letter-spacing:-1px;text-transform:uppercase}
.ser{font-family:Ser;font-style:italic;line-height:1}
.mono{font-family:Mono}
#grain{position:absolute;inset:-50px;pointer-events:none;opacity:.10;mix-blend-mode:overlay}
#vig{position:absolute;inset:0;background:radial-gradient(130% 90% at 50% 45%,transparent 55%,rgba(0,0,0,.55))}
#brand{position:absolute;left:64px;top:92px;font-family:Mono;font-weight:700;font-size:26px;letter-spacing:4px}
#prog{position:absolute;left:0;top:0;height:8px;background:var(--clay)}
#cap{position:absolute;left:60px;right:60px;top:1500px;text-align:center;font-family:Sans;font-weight:700;font-size:66px;line-height:1.15}
#cap span{padding:2px 12px;border-radius:12px;margin:0 2px;display:inline-block}
.win{border-radius:26px;background:#1C1917;box-shadow:0 40px 120px rgba(0,0,0,.6),0 0 0 2px rgba(255,255,255,.06)}
.bar{height:72px;display:flex;align-items:center;gap:14px;padding:0 28px;border-bottom:2px solid rgba(255,255,255,.06)}
.dot{width:20px;height:20px;border-radius:50%}
.chip{display:inline-block;padding:16px 34px;border-radius:60px;font-family:Mono;font-weight:700;font-size:34px;letter-spacing:2px}
</style></head><body>
<div style="position:absolute;width:1px;height:1px;overflow:hidden;opacity:.01"><img src="__OWLDIR__/closeup.png"><img src="__OWLDIR__/point.png"><img src="__DIR__/cut.png"><img src="__DIR__/bg.jpg"></div><div id="cam"><div id="stage"></div></div>
<svg id="grain" width="1180" height="2020"><filter id="n"><feTurbulence id="tb" type="fractalNoise" baseFrequency=".9" numOctaves="2" seed="1"/></filter><rect width="100%" height="100%" filter="url(#n)"/></svg>
<div id="vig"></div><div id="prog"></div><div id="brand"></div><div id="cap"></div>
<script>
const WD=__WORDS__,TOTAL=__TOTAL__,D='__DIR__',K='__OWLDIR__';
const cl=(x,a=0,b=1)=>Math.max(a,Math.min(b,x)),eo=x=>1-Math.pow(1-cl(x),3),eb=x=>{x=cl(x);const c=1.7;return 1+(c+1)*Math.pow(x-1,3)+c*Math.pow(x-1,2)};
const nm=s=>s.toLowerCase().replace(/[^a-z0-9$']/g,'');
const L=[];WD.forEach(w=>{if(L[w.line]===undefined)L[w.line]=w.s});L.push(TOTAL);
function W(word,line,k=0){const c=WD.filter(w=>w.line===line&&nm(w.w)===nm(word));return c.length?c[Math.min(k,c.length-1)].s:L[line]}
const P=(t,t0,d=.35)=>eo((t-t0)/d), B=(t,t0,d=.45)=>eb((t-t0)/d);
function typed(str,t,t0,cps=38){const n=Math.floor(cl((t-t0)*cps,0,str.length));return str.slice(0,n)+(t>t0&&n<str.length&&Math.floor(t*4)%2?'▍':'')}
function rise(t,t0,dy=60){const p=P(t,t0,.4);return `opacity:${p};transform:translateY(${(1-p)*dy}px)`}
function pop(t,t0){const p=B(t,t0,.45);return `opacity:${cl((t-t0)/.12)};transform:scale(${.6+.4*p})`}
let punch=0;
const S=[];
// 0 HOOK
S[0]=(t)=>{const z=1.1+t*.012,sw=Math.sin(t*.9)*4;
 return `<div class=abs style="inset:-60px;background:url(${D}/bg.jpg) center/cover;filter:blur(34px) brightness(.22);transform:scale(${z}) translateX(${-t*6}px)"></div>
 <div class="abs disp" style="left:0;right:0;top:150px;text-align:center;font-size:210px;color:var(--clay);opacity:${P(t,W('Linux',0),.5)};transform:scale(${1.25-.25*P(t,W('Linux',0),.6)})">LINUX</div>
 <div class=abs style="inset:0;background:url(${D}/cut.png) center 300px/1000px auto no-repeat;transform:perspective(1400px) rotateY(${sw}deg) scale(${1.0+t*.008}) translateX(${t*4}px);filter:drop-shadow(0 30px 60px rgba(0,0,0,.7))"></div>
 <div class=abs style="left:0;right:0;top:960px;height:960px;background:linear-gradient(180deg,transparent,rgba(18,16,14,.9) 35%,var(--ink) 60%)"></div>
 <div class="abs disp" style="left:64px;right:64px;top:1100px;font-size:62px;${rise(t,0)}">The man who made Linux</div>
 <div class="abs ser" style="left:64px;right:64px;top:1195px;font-size:92px;color:var(--cream);${rise(t,W('AI',0))}">just let <span style="color:var(--clay)">AI</span> rewrite part of it</div>
 <div class="abs disp" style="left:64px;top:1330px;font-size:64px;padding:6px 26px;background:var(--clay);color:var(--ink);border-radius:14px;transform-origin:left;${pop(t,W('three',0))};rotate:-3deg">3X FASTER</div>`};
// 1 HOST
S[1]=(t,lt)=>`<div class=abs style="inset:0;background:var(--cream)"></div>
 <div class=abs style="left:290px;top:${330+Math.sin(t*3)*10}px;width:500px;height:500px;background:url(${K}/closeup.png) center/contain no-repeat;${pop(t,L[1])}"></div>
 <div class="abs mono" style="left:0;right:0;top:880px;text-align:center;font-size:30px;letter-spacing:6px;color:var(--clay);font-weight:700;${rise(t,L[1]+.2)}">YOUR AI NEWS HOST</div>
 <div class="abs disp" style="left:0;right:0;top:940px;text-align:center;font-size:96px;color:var(--ink);${rise(t,L[1]+.35)}">The AI Khabari</div>
 <div class="abs ser" style="left:0;right:0;top:1100px;text-align:center;font-size:78px;color:var(--ink);${rise(t,W('matters',1))}">this matters even if you <span style="color:var(--clay)">never code</span></div>`;
// 2 WHERE LINUX RUNS
S[2]=(t)=>{const rows=[['01','Android phones','android'],['02','Most servers','servers'],['03','Every top supercomputer','supercomputer']];
 let h=`<div class=abs style="inset:0;background:var(--ink);background-image:linear-gradient(rgba(255,255,255,.04) 2px,transparent 2px),linear-gradient(90deg,rgba(255,255,255,.04) 2px,transparent 2px);background-size:90px 90px;background-position:0 ${-t*30}px"></div>
 <div class="abs mono" style="left:64px;top:300px;font-size:40px;color:var(--dim)"><span style="color:var(--clay)">$</span> ${typed('where does linux run?',t,L[2])}</div>
 <div class="abs disp" style="left:64px;right:64px;top:400px;font-size:64px;${rise(t,W('built',2))}">Torvalds built <span style="color:var(--clay)">Linux</span>.</div>`;
 rows.forEach((r,i)=>{const t0=W(r[2],2),p=P(t,t0,.4);h+=`<div class=abs style="left:64px;right:64px;top:${620+i*230}px;height:190px;border-radius:24px;background:var(--ink2);border:2px solid ${p>.9?'rgba(110,231,168,.5)':'rgba(255,255,255,.08)'};opacity:${p};transform:translateX(${(1-p)*200}px);display:flex;align-items:center;gap:34px;padding:0 40px">
  <div class=mono style="font-size:40px;color:var(--clay);font-weight:700">${r[0]}</div><div class=disp style="font-size:${r[1].length>16?40:52}px;flex:1">${r[1]}</div><div class=mono style="font-size:56px;color:var(--mint);opacity:${P(t,t0+.25,.2)}">✓</div></div>`});return h};
// 3 CLAUDE CODE TERMINAL (illustration)
S[3]=(t)=>{const t0=W('posted',3),q=W('direction',3);
 const lines=[['● Reading mm/filemap.c','var(--dim)'],['● Reading include/linux/pagemap.h','var(--dim)'],['● Editing filemap_read()','var(--cream)'],['- folio_get(folio);','var(--red)'],['+ rcu_read_lock();','var(--mint)'],['+ /* read without a page ref */','var(--mint)'],['✓ 8 patches ready for review','var(--mint)']];
 const ps=t0+1.6;let body='';lines.forEach((l,i)=>{const ti=ps+i*.42;if(t>ti)body+=`<div style="color:${l[1]};opacity:${P(t,ti,.2)};${l[0][0]=='-'||l[0][0]=='+'?'background:rgba(255,255,255,.04);padding-left:12px;border-radius:6px;':''}">${l[0]}</div>`});
 const qp=P(t,q,.45);
 return `<div class=abs style="inset:0;background:radial-gradient(90% 60% at 50% 30%,#2A1C14,var(--ink))"></div>
 <div class="abs win" style="left:54px;right:54px;top:250px;height:820px;transform:perspective(1600px) rotateX(${(1-P(t,L[3],.6))*18}deg) translateY(${(1-P(t,L[3],.6))*120}px) scale(${1-qp*.06});opacity:${P(t,L[3],.4)}">
  <div class=bar><div class=dot style="background:#FF5F57"></div><div class=dot style="background:#FEBC2E"></div><div class=dot style="background:#28C840"></div><div class=mono style="margin-left:18px;font-size:26px;color:var(--dim)">claude-code &mdash; ~/linux</div><div class=mono style="margin-left:auto;font-size:20px;letter-spacing:3px;color:var(--dim);border:1px solid #444;padding:4px 10px;border-radius:6px">ILLUSTRATION</div></div>
  <div class=mono style="padding:34px 36px;font-size:36px;line-height:1.7">
   <div><span style="color:var(--clay);font-weight:700">&gt;</span> ${typed('read the page cache without taking folio refs',t,t0,30)}</div>
   <div style="height:20px"></div>${body}</div></div>
 <div class=abs style="left:54px;right:54px;top:1040px;padding:36px 44px;border-radius:26px;background:var(--cream);color:var(--ink);opacity:${qp};transform:translateY(${(1-qp)*80}px) rotate(-1.5deg)">
  <div class=ser style="font-size:66px;line-height:1.08">&ldquo;done with an LLM coding assistant (Claude Code) <span style="color:var(--clay)">under my direction</span>&rdquo;</div>
  <div class=mono style="font-size:24px;margin-top:18px;letter-spacing:2px">LINUS TORVALDS &middot; KERNEL COMMIT, OCT 2026</div></div>`};
// 4 WORKERS / COUNTER DIAGRAM
S[4]=(t)=>{const sw=W('new',4),after=t>sw,pa=P(t,sw,.6),cx=540,cy=900;let h=`<div class=abs style="inset:0;background:var(--ink)"></div>
 <div class="abs mono" style="left:64px;top:280px;font-size:30px;letter-spacing:6px;font-weight:700;color:${after?'var(--mint)':'var(--red)'}">${after?'AFTER &middot; THE NEW CODE':'BEFORE'}</div>
 <div class="abs disp" style="left:64px;right:64px;top:340px;font-size:54px">${after?'Everyone reads <span style="color:var(--mint)">at once</span>':'8 readers, <span style="color:var(--red)">1 counter</span>'}</div>
 <div class=abs style="left:${cx-130}px;top:${cy-90}px;width:260px;height:180px;border-radius:24px;border:4px solid ${after?'var(--mint)':'var(--red)'};display:flex;align-items:center;justify-content:center;flex-direction:column;background:var(--ink2);transform:scale(${1+(!after?Math.abs(Math.sin(t*14))*.05:0)})"><div class=mono style="font-size:28px;color:var(--dim)">${after?'FILE':'COUNTER'}</div><div class=disp style="font-size:44px">${after?'READ':'WAIT'}</div></div>`;
 for(let i=0;i<8;i++){const a=i/8*Math.PI*2+t*.4;let r,x,y,col;
  if(!after){r=330-Math.abs(Math.sin(t*6+i))*90;x=cx+Math.cos(a)*r;y=cy+Math.sin(a)*r*0.9;col='var(--red)'}
  else{const ph=((t*0.9+i/8)%1);x=cx+Math.cos(i/8*Math.PI*2)*(460-ph*330)*(1-pa)+(-420+ph*840)*pa;y=cy+Math.sin(i/8*Math.PI*2)*(400-ph*300)*(1-pa)+(-300+i*85)*pa;col='var(--mint)'}
  h+=`<div class=abs style="left:${x-34}px;top:${y-34}px;width:68px;height:68px;border-radius:50%;background:${col};box-shadow:0 0 30px ${col};display:flex;align-items:center;justify-content:center;font-family:Mono;font-weight:700;font-size:28px;color:var(--ink);opacity:${P(t,L[4]+i*.08,.3)}">${i+1}</div>`}
 if(!after)h+=`<div class="abs ser" style="left:0;right:0;top:1300px;text-align:center;font-size:76px;color:var(--red);opacity:${P(t,W('fighting',4),.3)}">all fighting over it</div>`;
 return h};
// 5 RESULT BARS
S[5]=(t)=>{const a=W('ten',5),b=W('thirty',5),o=W('over',5),pv=cl((t-b)/1.6),v=Math.round(10+23*eo(pv));
 return `<div class=abs style="inset:0;background:var(--ink)"></div>
 <div class="abs mono" style="left:64px;top:290px;font-size:28px;letter-spacing:5px;color:var(--dim)">READS PER SECOND &middot; 8 THREADS &middot; HIS LAPTOP</div>
 <div class=abs style="left:64px;top:400px;width:952px">
  <div class=mono style="font-size:32px;color:var(--dim);opacity:${P(t,a)}">BEFORE</div>
  <div style="margin-top:12px;height:120px;border-radius:16px;background:#3A3530;width:${30.3*P(t,a,.6)}%;display:flex;align-items:center;padding-left:24px"><span class=disp style="font-size:52px">10M</span></div>
  <div class=mono style="font-size:32px;color:var(--clay);margin-top:60px;opacity:${P(t,b)}">AFTER</div>
  <div style="margin-top:12px;height:120px;border-radius:16px;background:var(--clay);width:${Math.max(30.3,100*v/33)*P(t,b,.2)}%;display:flex;align-items:center;padding-left:24px;color:var(--ink);opacity:${P(t,b,.2)}"><span class=disp style="font-size:52px">${v}M</span></div></div>
 <div class="abs disp" style="left:0;right:0;top:900px;text-align:center;font-size:260px;color:var(--clay);${pop(t,o)}">3.3X</div>
 <div class="abs ser" style="left:0;right:0;top:1380px;text-align:center;font-size:70px;opacity:${P(t,o+.3)}">faster, on this one test</div>`};
// 6 HYPE -> CODES WITH AI
S[6]=(t)=>{const h2=W('hype',6);
 return `<div class=abs style="inset:-40px;background:url(${D}/cut.png) center 20%/cover;filter:grayscale(1) contrast(1.2) brightness(.35);transform:scale(${1.2+t*.01})"></div>
 <div class=abs style="inset:0;background:repeating-linear-gradient(0deg,rgba(0,0,0,.25) 0 2px,transparent 2px 6px)"></div>
 <div class=abs style="left:64px;right:64px;top:420px;padding:34px 40px;border-radius:24px;background:rgba(29,26,23,.9);border:2px solid #444;${rise(t,L[6])}"><div class=mono style="font-size:34px;color:var(--dim);font-weight:700">2024</div><div class=disp style="font-size:50px;margin-top:10px">Called most AI talk <span style="color:var(--dim)">marketing hype</span></div></div>
 <div class=abs style="left:64px;right:64px;top:880px;padding:34px 40px;border-radius:24px;background:var(--clay);color:var(--ink);${pop(t,h2+.25)}"><div class=mono style="font-size:34px;font-weight:700">2026</div><div class=disp style="font-size:64px;margin-top:10px">Ships kernel code with AI</div></div>`};
// 7 CATCH
S[7]=(t)=>{const it=[['one test, on his own machine','test'],['some cases got slower','slower'],['not merged into Linux yet','merged']];
 let h=`<div class=abs style="inset:0;background:radial-gradient(80% 50% at 50% 40%,rgba(255,95,87,${.16+.08*Math.sin(t*5)}),var(--ink))"></div>
 <div class="abs disp" style="left:64px;top:330px;font-size:120px;color:var(--red);${pop(t,L[7])}">The catch</div>`;
 it.forEach((x,i)=>{const t0=W(x[1],7);h+=`<div class="abs mono" style="left:64px;right:64px;top:${620+i*170}px;font-size:46px;padding:30px 34px;border-radius:18px;background:rgba(255,95,87,.1);border:2px solid rgba(255,95,87,.5);opacity:${P(t,t0-.15,.25)}"><span style="color:var(--red);font-weight:700">[!]</span> ${typed(x[0],t,t0-.15,45)}</div>`});return h};
// 8 BIG IDEA
S[8]=(t)=>{const r=W('replaced',8),d=W('directing',8),s=P(t,d-.2,.35);
 return `<div class=abs style="inset:0;background:var(--ink)"></div>
 <div class="abs disp" style="left:64px;right:64px;top:400px;font-size:70px;${rise(t,W('top',8))}">Top engineers aren't being</div>
 <div class="abs disp" style="left:64px;top:690px;font-size:118px;color:${s>.5?'var(--dim)':'var(--cream)'};${rise(t,r)}">replaced<div style="position:absolute;left:-10px;top:52%;height:14px;background:var(--red);width:${s*104}%;border-radius:7px"></div></div>
 <div class="abs ser" style="left:64px;right:64px;top:900px;font-size:150px;color:var(--clay);${pop(t,d)}">they're directing AI.</div>`};
// 9 TAKEAWAY (cream)
S[9]=(t)=>{const it=[['AI does the heavy lifting','heavy'],['You set the goal','goal'],['You check the numbers','check'],['You stay the boss','boss']];
 let h=`<div class=abs style="inset:0;background:var(--cream)"></div>
 <div class="abs mono" style="left:64px;top:300px;font-size:30px;letter-spacing:5px;font-weight:700;color:var(--clay);${rise(t,L[9])}">WHAT YOU CAN TAKE FROM THIS</div>`;
 it.forEach((x,i)=>{const t0=W(x[1],9),c=P(t,t0,.25);h+=`<div class=abs style="left:64px;right:64px;top:${420+i*200}px;display:flex;align-items:center;gap:34px;color:var(--ink);${rise(t,t0-.3,40)}">
  <div style="width:92px;height:92px;border-radius:20px;border:5px solid var(--ink);background:${c>.5?'var(--clay)':'transparent'};display:flex;align-items:center;justify-content:center;font-family:Mono;font-weight:700;font-size:60px;color:var(--ink);transform:scale(${1+Math.sin(cl((t-t0)/.3)*Math.PI)*.15})">${c>.5?'✓':''}</div>
  <div class=disp style="font-size:46px">${x[0]}</div></div>`});return h};
// 10 CTA
S[10]=(t)=>`<div class=abs style="inset:0;background:radial-gradient(90% 60% at 50% 30%,#2A1C14,var(--ink))"></div>
 <div class="abs disp" style="left:64px;right:64px;top:320px;font-size:72px;${rise(t,L[10])}">Would you let AI touch code</div>
 <div class="abs ser" style="left:64px;right:64px;top:580px;font-size:150px;color:var(--clay);${rise(t,W('important',10))}">this important?</div>
 <div class="abs chip" style="left:64px;top:860px;background:var(--clay);color:var(--ink);${pop(t,W('send',10))}">SEND TO A FRIEND</div>
 <div class="abs chip" style="left:64px;top:980px;border:3px solid var(--cream);${pop(t,W('code',10,1))}">FOLLOW @THEAIKHABARI</div>
 <div class=abs style="right:30px;top:${1040+Math.sin(t*3)*12}px;width:420px;height:420px;background:url(${K}/point.png) center/contain no-repeat;transform:scaleX(-1);${'opacity:'+P(t,L[10]+.3,.4)}"></div>
 <div class="abs mono" style="left:64px;right:64px;top:1800px;font-size:20px;color:var(--dim)">Sources: kernel.org commit, Linuxiac, Phoronix (Oct 2026). Photo: Beraldo Leal / CC BY 2.0. Terminal is an illustration.</div>`;
const CREAM=new Set([1,9]);
function setT(t){
 let i=0;for(let k=0;k<S.length;k++)if(t>=L[k]-.12)i=k;
 const lt=t-(L[i]-.12),inP=eo(lt/.28);
 const st=document.getElementById('stage');
 st.innerHTML=`<div class=abs style="inset:0;transform:translateX(${(1-inP)*140}px);filter:blur(${(1-inP)*14}px)">${S[i](t,lt)}</div>`;
 // camera punch on big beats
 const beats=[W('three',0),W('over',5),W('directing',8)];let pz=0;beats.forEach(b=>{if(t>b&&t<b+.5)pz=Math.max(pz,(1-(t-b)/.5)*.05)});
 document.getElementById('cam').style.transform=`scale(${1+pz+Math.sin(t*.7)*.004}) rotate(${pz*8*Math.sin(t*40)}deg)`;
 document.getElementById('tb').setAttribute('seed',Math.floor(t*24)%97+1);
 document.getElementById('grain').style.transform=`translate(${(t*137)%40-20}px,${(t*91)%40-20}px)`;
 document.getElementById('prog').style.width=(t/TOTAL*100)+'%';
 const cream=CREAM.has(i),br=document.getElementById('brand');br.innerHTML=`<span style="color:var(--clay)">&#9679;</span> THE AI KHABARI`;br.style.color=cream?'var(--ink)':'var(--cream)';
 // captions: 3-word groups
 const cur=WD.findIndex(w=>t>=w.s&&t<w.e+.05);const cap=document.getElementById('cap');
 if(cur<0||t<0.05){cap.innerHTML='';return}
 const g=Math.floor(cur/3)*3,grp=WD.slice(g,g+3).filter(w=>w.line===WD[cur].line);
 cap.innerHTML=grp.map(w=>{const on=w===WD[cur];return `<span style="${on?'background:var(--clay);color:var(--ink);transform:scale(1.08)':'color:'+(cream?'var(--ink)':'var(--cream)')+';text-shadow:'+(cream?'none':'0 4px 18px rgba(0,0,0,.8)')}">${w.w.replace(/[{}]/g,'')}</span>`}).join(' ');
}
setT(0);
</script></body></html>
