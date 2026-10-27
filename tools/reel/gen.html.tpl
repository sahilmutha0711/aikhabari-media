<!doctype html><html><head><meta charset="utf-8">
<style>
@font-face{font-family:'Brico';font-weight:700 800;src:url('file:///mnt/skills/examples/canvas-design/canvas-fonts/BricolageGrotesque-Bold.ttf')}
@font-face{font-family:'DMS';font-weight:400;src:url('file:///mnt/skills/examples/canvas-design/canvas-fonts/WorkSans-Regular.ttf')}
@font-face{font-family:'DMS';font-weight:700;src:url('file:///mnt/skills/examples/canvas-design/canvas-fonts/WorkSans-Bold.ttf')}
:root{--navy:#0B1030;--amber:#FFB400;--violet:#7C6CFF;--coral:#FF6B5A;--paper:#F4F1EA;--mute:#B9B7CC}
*{box-sizing:border-box;margin:0;padding:0}
body{width:1080px;height:1920px;overflow:hidden;background:var(--navy);font-family:'DMS',sans-serif;color:var(--paper)}
#stage{position:relative;width:1080px;height:1920px;overflow:hidden}
.abs{position:absolute}.scene{position:absolute;inset:0;opacity:0}
.it{position:absolute;left:90px;right:90px}
.big{font-family:'Brico';font-weight:800;font-size:150px;line-height:.95;letter-spacing:-2px}
.mid{font-family:'Brico';font-weight:800;font-size:100px;line-height:1.0;letter-spacing:-1px}
.sm{font-family:'Brico';font-weight:800;font-size:72px;line-height:1.05}
.txt{font-size:46px;font-weight:700;line-height:1.3;color:var(--paper)}
.am{color:var(--amber)}.co{color:var(--coral)}.mu{color:var(--mute)}
.hl{background:var(--amber);color:var(--navy);padding:0 18px;border-radius:12px}
.label{font-weight:700;font-size:32px;letter-spacing:6px;color:var(--amber)}
.chip{display:inline-block;border:4px solid var(--amber);color:var(--amber);border-radius:60px;padding:10px 32px;font-weight:700;font-size:38px;letter-spacing:3px;white-space:nowrap;background:rgba(11,16,48,.6)}
.chip.f{background:var(--amber);color:var(--navy)}.chip.c{border-color:var(--coral);background:var(--coral);color:#fff}
.card{border-radius:34px;padding:30px 38px;background:rgba(255,255,255,.07);border:4px solid rgba(255,255,255,.22)}
.card.a{border-color:var(--amber);background:rgba(255,180,0,.1)}.card.r{border-color:var(--coral);background:rgba(255,107,90,.1)}
.card .k{font-weight:700;font-size:28px;letter-spacing:5px;color:var(--mute);margin-bottom:10px}
.card .v{font-size:40px;line-height:1.3;font-weight:700}
.stamp{display:inline-block;border:7px solid var(--coral);color:var(--coral);font-family:'Brico';font-weight:800;font-size:54px;letter-spacing:3px;padding:6px 24px;border-radius:14px;background:rgba(11,16,48,.88);white-space:nowrap}
.photo{height:560px;border-radius:36px;overflow:hidden;border:5px solid var(--amber);background-size:cover;background-position:center}
.photo .pc{position:absolute;left:26px;bottom:24px}
.cred{position:absolute;right:16px;bottom:10px;font-size:18px;color:rgba(255,255,255,.75);text-shadow:0 1px 4px #000}
.owlwrap{position:absolute;perspective:900px}
.owlwrap img{display:block;width:100%;filter:drop-shadow(0 30px 40px rgba(0,0,0,.55));transform-origin:50% 90%}
#cap{position:absolute;left:60px;right:60px;top:1450px;text-align:center;font-family:'Brico';font-weight:800;font-size:76px;line-height:1.15;text-shadow:0 6px 24px rgba(0,0,0,.7)}
#cap span{display:inline-block;margin:0 10px;padding:0 10px;border-radius:12px}#cap span.on{background:var(--amber);color:var(--navy);text-shadow:none}
</style></head><body><div id="stage">
<div id="bg" class="abs" style="inset:0"></div>
<svg class="abs" width="1080" height="1920" style="left:0;top:0;opacity:.07"><g id="gridg" stroke="#fff" stroke-width="2"></g></svg>
<div id="scenes"></div>
<div id="owl" class="owlwrap"><img id="owlimg" src="__OWLDIR__/closeup.png"></div>
<div id="bub" class="abs" style="width:200px;height:200px;border-radius:50%;border:5px solid var(--amber);background:radial-gradient(circle at 50% 35%,#1d2470,#0B1030);opacity:0;box-shadow:0 10px 30px rgba(0,0,0,.5);left:840px;top:232px"></div>
<div id="bubname" class="abs chip f" style="font-size:22px;padding:4px 16px;opacity:0;left:868px;top:420px">KHABARI</div>
<div class="abs" style="left:90px;top:220px;font-weight:700;font-size:30px;letter-spacing:5px;color:var(--mute)"><span style="color:var(--amber)">●</span> THE AI KHABARI</div>
<div class="abs" style="left:90px;right:90px;top:200px;height:6px;border-radius:3px;background:rgba(255,255,255,.12)"><div id="prog" style="height:100%;width:0;border-radius:3px;background:var(--amber)"></div></div>
<div id="flash" class="abs" style="inset:0;background:#fff;opacity:0"></div>
<div id="cap"></div>
</div>
<script>
const WORDS=__WORDS__,ENV=__ENV__,TOTAL=__TOTAL__,FPS=__FPS__,SPEC=__SPEC__,DIR='__DIR__',OWL='__OWLDIR__';
const $=i=>document.getElementById(i),cl=(x,a=0,b=1)=>Math.max(a,Math.min(b,x)),p=(t,a,d)=>cl((t-a)/d),eo=x=>1-Math.pow(1-x,3);
const back=x=>{const c=1.70158;return 1+(c+1)*Math.pow(x-1,3)+c*Math.pow(x-1,2)};
const nm=s=>s.toLowerCase().replace(/[^a-z0-9$.%]/g,'').replace(/\.$/,'');
function W(a){if(a==null)return null;if(typeof a==='number')return a;const [w,l,d]=a;const x=WORDS.find(o=>nm(o.w)===nm(w)&&o.line===l);if(!x)throw Error('word '+w+' line '+l);return x.s+(d||0)}
function L(l){const ws=WORDS.filter(o=>o.line===l);return{s:ws[0].s,e:ws[ws.length-1].e}}
(()=>{let d='';for(let x=0;x<=1080;x+=135)d+=`M${x} 0V1920`;for(let y=0;y<=1920;y+=135)d+=`M0 ${y}H1080`;$('gridg').innerHTML=`<path d="${d}"/>`})();
const env=t=>ENV[Math.min(ENV.length-1,Math.max(0,Math.floor(t*FPS)))]||0;
// build scenes
const SC=SPEC.scenes.map((s,i)=>({...s,i,start:i===0?0:L(s.from).s-.2}));
SC.forEach((s,i)=>{s.end=i<SC.length-1?SC[i+1].start:TOTAL+1});
const box=$('scenes');
SC.forEach(s=>{const d=document.createElement('div');d.className='scene';d.id='sc'+s.i;let h='';
 if(s.bg)h+=`<div class="abs bgph" style="inset:-80px;background:url('${DIR}/${s.bg}') center/cover;filter:blur(${s.bgblur??10}px) brightness(${s.bgdim??.32})"></div><div class="abs" style="inset:0;background:linear-gradient(180deg,rgba(11,16,48,.45),rgba(11,16,48,.1) 40%,rgba(11,16,48,.92))"></div>`;
 if(s.label)h+=`<div class="it label" style="top:290px">${s.label}</div>`;
 (s.items||[]).forEach((it,j)=>{let inner=it.html||'';
  if(it.photo)inner=`<div class="photo" style="background-image:url('${DIR}/${it.photo}');position:relative${it.h?';height:'+it.h+'px':''}">${it.cap?`<div class="pc chip f" style="font-size:30px;padding:8px 24px">${it.cap}</div>`:''}${it.cred?`<div class="cred">${it.cred}</div>`:''}</div>`;
  if(it.count)inner=`<span id="cnt${s.i}_${j}">${it.count.fmt?'':''}</span>`;
  h+=`<div class="it ${it.cls||''}" id="it${s.i}_${j}" style="top:${it.top}px;${it.style||''}">${inner}</div>`});
 d.innerHTML=h;box.appendChild(d)});
function fmt(c,v){const n=c.dec?v.toFixed(c.dec):Math.round(v).toLocaleString('en-US');return (c.pre||'')+n+(c.suf||'')}
const CH=[];{let c=[];WORDS.forEach((w,i)=>{c.push(w);const n=WORDS[i+1];if(c.length>=3||/[,.?!:]$/.test(w.w)||!n||n.line!==w.line){CH.push(c);c=[]}})}
const HOST=SC.find(s=>s.type==='host'),CTA=SC.find(s=>s.type==='cta');
function setT(t){
 $('prog').style.width=cl(t/TOTAL)*100+'%';
 const cur=SC.find(s=>t>=s.start&&t<s.end)||SC[0];const cm=cur.coral?1:0;
 $('bg').style.background=`radial-gradient(900px 900px at ${80+Math.sin(t*.3)*8}% ${10+Math.cos(t*.25)*5}%, rgba(255,${180-73*cm},${90*cm},.38), transparent 62%), radial-gradient(1000px 1000px at ${5+Math.cos(t*.2)*6}% 95%, rgba(90,70,255,.5), transparent 60%), linear-gradient(160deg,#101745,#0B1030 70%)`;
 $('gridg').setAttribute('transform',`translate(0 ${(t*12)%135})`);
 let fl=0;
 SC.forEach(s=>{const el=$('sc'+s.i);const o=cl(p(t,s.start,.22)-p(t,s.end,.2));el.style.opacity=o;el.style.transform=`translateY(${(1-eo(p(t,s.start,.35)))*60}px)`;
  if(s.start>0&&t>=s.start)fl=Math.max(fl,.25*(1-p(t,s.start,.15)));
  const bg=el.querySelector('.bgph');if(bg)bg.style.transform=`scale(${1.05+(t-s.start)*.02})`;
  (s.items||[]).forEach((it,j)=>{const e=$('it'+s.i+'_'+j);const at=it.at?W(it.at):s.start+.1;const out=it.out?W(it.out):null;
   const q=p(t,at,it.anim==='stamp'?.25:.35);let o2=q;if(out!=null)o2=Math.min(o2,1-p(t,out,.2));e.style.opacity=o2;
   const r=it.rot||0;
   if(it.anim==='stamp')e.style.transform=`rotate(${r}deg) scale(${q<1?2.2-1.2*eo(q):1})`;
   else if(it.anim==='pop'){e.style.transform=`scale(${back(q)})`;e.style.transformOrigin='0 50%'}
   else if(it.anim==='zoom')e.style.transform=`scale(${1+(t-at)*.01})`;
   else e.style.transform=`translateX(${(1-eo(q))*-70}px)`;
   if(it.count){const c=it.count;const a=W(c.start),b=W(c.end);const k=eo(p(t,a,Math.max(.3,b-a)));$('cnt'+s.i+'_'+j).textContent=fmt(c,c.from+(c.to-c.from)*k)}
   if(it.type){const a=W(it.type.start),b=W(it.type.end);const k=p(t,a,Math.max(.3,b-a));const tx=it.type.text;e.querySelector('.ty').textContent=tx.slice(0,Math.floor(k*tx.length))+(k>0&&k<1&&Math.floor(t*4)%2?'|':'')}
  })});
 $('flash').style.opacity=fl;
 owlUpdate(t);
 const c=CH.find((c,i)=>t>=c[0].s-.05&&(i===CH.length-1?t<=c[c.length-1].e+.6:t<CH[i+1][0].s-.05));
 $('cap').innerHTML=c?c.map((w,j)=>{const n=c[j+1];return `<span class="${t>=w.s-.02&&(!n||t<n.s-.02)?'on':''}">${w.w}</span>`}).join(' '):'';
}
function owlUpdate(t){
 const o=$('owl'),im=$('owlimg'),bub=$('bub'),bn=$('bubname');
 const i0=HOST.start,i1=HOST.end-.15,c0=CTA.start;
 const talk=env(t);let x,y,w,op=1,rotY=Math.sin(t*1.7)*10,rotX=Math.sin(t*1.1)*4,tilt=Math.sin(t*2.3)*3,sq=1+talk*.06,bubOp=0,mir=1;
 if(t<i0){op=0;x=290;y=600;w=500}
 else if(t<i1){const a=back(p(t,i0,.5));x=290;y=560+(1-a)*500;w=500;if(!im.src.endsWith('closeup.png'))im.src=OWL+'/closeup.png';op=p(t,i0,.15)}
 else if(t<c0){const k=eo(p(t,i1,.6));x=290+565*k;y=560-318*k;w=500-350*k;bubOp=p(t,i1+.35,.25);
  let jump=0;(SPEC.jump||[]).forEach(a=>{jump+=Math.sin(Math.PI*p(t,W(a),.5))*26});y-=jump;
  (SPEC.shake||[]).forEach(a=>{const q=p(t,W(a),1.0);if(q>0&&q<1)tilt+=Math.sin(t*40)*6*(1-q)});
  if(cur_noowl(t)){op=0;bubOp=0}}
 else {const a=back(p(t,c0+.2,.6));if(!im.src.endsWith('point.png'))im.src=OWL+'/point.png';x=590+(1-a)*600;y=SPEC.ctaOwlY||930;w=390;op=p(t,c0,.2);rotY=Math.sin(t*1.7)*8;mir=-1}
 o.style.left=x+'px';o.style.top=y+'px';o.style.width=w+'px';o.style.opacity=op;
 im.style.transform=`scaleX(${mir}) rotateY(${rotY}deg) rotateX(${rotX}deg) rotate(${tilt}deg) scale(${sq},${2-sq})`;
 bub.style.opacity=bubOp;bn.style.opacity=bubOp;bub.style.zIndex=1;o.style.zIndex=2;
}
function cur_noowl(t){const s=SC.find(s=>t>=s.start&&t<s.end);return s&&s.noowl}
window.setT=setT;
</script></body></html>
