import sys,json,numpy as np
sys.path.insert(0,'work');from words_master import W
mode=sys.argv[1]
db=np.load('work/db.npy')
if mode=='short':
    drop={'A0','A1','B0','X','D0','F0','J0','L0','N0','P0','I1','K','K2'}; GAPMAX=0.24
else:
    drop={'X','A0'}; GAPMAX=0.80
keep=[i for i,w in enumerate(W) if w[3] not in drop]
def argmin(a,b):
    i0,i1=int(a*100),int(b*100)
    if i1<=i0: return a
    return (i0+int(np.argmin(db[i0:i1])))/100
pieces=[];s=None
for n,i in enumerate(keep):
    w=W[i]
    if s is None:
        lo=W[i-1][2]+0.02 if (i>0 and W[i-1][2]<=w[1]) else w[1]-0.22
        s=argmin(max(lo,w[1]-0.22),w[1]-0.01) if w[1]-0.01>max(lo,w[1]-0.22) else max(lo,w[1]-0.03)
    j=keep[n+1] if n+1<len(keep) else None
    brk = j is None or j!=i+1 or (W[j][1]-w[2])>GAPMAX or W[j][1]<w[2]
    if brk:
        hi=W[i+1][1]-0.02 if (i+1<len(W) and W[i+1][1]>=w[2]) else w[2]+0.3
        lo=w[2]+0.04
        e=argmin(lo,min(hi,w[2]+0.28)) if min(hi,w[2]+0.28)>lo else min(hi,w[2]+0.02)
        # ensure we don't cut before word end
        e=max(e,min(w[2]+0.04,hi))
        pieces.append((s,e));s=None
fixed=[]
for x,y in pieces:
    if x<38.6<y: y=38.6
    if 46.9<x<47.0 or (x<46.98<y and x>46.0 and abs(x-46.98)<0.25): x=46.97
    fixed.append((x,y))
pieces=fixed
out=[(round(x*30)/30,round(y*30)/30) for x,y in pieces if y-x>0.05]
T=0;tl=[]
for a,b in out: tl.append((a,b,T));T+=b-a
words=[]
for i in keep:
    w,s0,e0,seg=W[i]
    for ps,pe,pt in tl:
        if ps-0.06<=s0<pe:
            words.append({'w':w,'s':round(pt+max(s0,ps)-ps,3),'e':round(pt+min(e0,pe)-ps,3),'seg':seg});break
    else: print('unmapped',w,s0)
json.dump({'pieces':out,'tl':tl,'words':words,'duration':round(T,3)},open(f'work/edit_{mode}.json','w'))
print(mode,'pieces',len(out),'duration',round(T,2),'words',len(words),'/',len(keep))
