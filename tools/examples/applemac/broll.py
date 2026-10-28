import json,subprocess,sys
pal=sys.argv[1];C=json.load(open('clips.json'))
ins=['-i',f'mesh_{pal}.mp4','-loop','1','-i','cardmask.png']
fc=[f"[1:v]format=gray,scale=1000:720,split={len(C)}"+''.join(f'[m{i}]' for i in range(len(C)))];last='[0:v]'
for i,(a,b,s) in enumerate(C):
    ins+=['-itsoffset',str(a),'-i',f'clip{i}.mp4']
    fc.append(f"[{i+2}:v]format=yuva420p[c{i}];[c{i}][m{i}]alphamerge[k{i}]")
    fc.append(f"{last}[k{i}]overlay=40:520:eof_action=pass:enable='between(t,{a},{b})'[o{i}]");last=f'[o{i}]'
fc.append(f"{last}format=yuv420p[v]")
subprocess.run(['ffmpeg','-v','error','-y',*ins,'-filter_complex',';'.join(fc),'-map','[v]','-t','78.4','-r','30','-c:v','libx264','-crf','17','-preset','fast',f'broll_{pal}.mp4'],check=True)
print('ok',pal)
