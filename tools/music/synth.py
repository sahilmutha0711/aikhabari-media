# Original royalty-free background bed: python3 synth.py out.wav seconds bpm mood(dark|bright)
import numpy as np,wave,sys
out,dur,bpm,mood=sys.argv[1],float(sys.argv[2]),float(sys.argv[3]),sys.argv[4]
sr=44100;N=int(sr*dur);mix=np.zeros((N,2));beat=60/bpm;rng=np.random.default_rng(7)
def note(f):return 440*2**((f-69)/12)
def add(sig,t,pan=0.5,g=1):
    i=int(t*sr);j=min(N,i+len(sig))
    if i>=N:return
    mix[i:j,0]+=sig[:j-i]*g*(1-pan);mix[i:j,1]+=sig[:j-i]*g*pan
def env(n,a=.005,d=.2):
    t=np.arange(n)/sr;return np.minimum(1,t/a)*np.exp(-t/d)
def kick():
    t=np.arange(int(.35*sr))/sr;f=50+90*np.exp(-t*30);return np.sin(2*np.pi*np.cumsum(f)/sr)*np.exp(-t*9)
def hat(d=.04):
    n=int(.08*sr);x=rng.standard_normal(n);x=np.diff(np.concatenate([[0],x]));return x*env(n,.001,d)*.25
def snap():
    n=int(.2*sr);x=rng.standard_normal(n);x=np.convolve(x,np.ones(6)/6,'same');t=np.arange(n)/sr;return (x*.5+np.sin(2*np.pi*190*t)*.4)*env(n,.001,.07)
def pluck(m,d=.35):
    n=int(d*sr);t=np.arange(n)/sr;f=note(m);s=np.sign(np.sin(2*np.pi*f*t))*.3+np.sin(2*np.pi*f*t)*.7
    s=np.convolve(s,np.ones(8)/8,'same');return s*env(n,.003,.12)
def pad(ms,d):
    n=int(d*sr);t=np.arange(n)/sr;s=sum(np.sin(2*np.pi*note(m)*t*(1+dt))+np.sin(2*np.pi*note(m)*t*(1-dt)) for m in ms for dt in (0.003,))
    a=np.minimum(1,t/.4)*np.minimum(1,(d-t)/.4);return s*a*.06
def bass(m,d):
    n=int(d*sr);t=np.arange(n)/sr;f=note(m);return (np.sin(2*np.pi*f*t)+.3*np.sin(4*np.pi*f*t))*env(n,.01,d*.6)*.5
prog={'dark':[(57,[57,60,64]),(53,[53,57,60]),(48,[55,60,64]),(55,[55,59,62])],   # Am F C G
      'bright':[(48,[60,64,67]),(55,[59,62,67]),(57,[57,60,64]),(53,[57,60,65])]}[mood]  # C G Am F
bar=4*beat;nb=int(dur/bar)+1
for b in range(nb):
    root,ch=prog[b%4];t0=b*bar
    add(pad(ch,bar),t0,.5,1)
    for k in range(8):add(bass(root-12,beat/2*.9),t0+k*beat/2,.5,.9 if k%2==0 else .5)
    arp=[ch[0]+12,ch[1]+12,ch[2]+12,ch[1]+12]
    for k in range(8):add(pluck(arp[k%4]),t0+k*beat/2,.3 if k%2 else .7,.35)
    intro=b<1
    for k in range(4):
        if not intro:add(kick(),t0+k*beat,.5,.8)
        if k in(1,3) and not intro:add(snap(),t0+k*beat,.5,.35)
    for k in range(8):add(hat(),t0+k*beat/2+(0.012 if k%2 else 0),.6,.6 if k%2 else .9)
# master: soft clip + fade
mix=np.tanh(mix*1.2);mix/=np.abs(mix).max()+1e-9
f=int(1.5*sr);mix[-f:]*=np.linspace(1,0,f)[:,None];mix[:int(.3*sr)]*=np.linspace(0,1,int(.3*sr))[:,None]
w=wave.open(out,'w');w.setnchannels(2);w.setsampwidth(2);w.setframerate(sr);w.writeframes((mix*.9*32767).astype(np.int16).tobytes());w.close()
