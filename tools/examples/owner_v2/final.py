import json,subprocess,sys
R='/home/claude/reels/agi_owner';mode=sys.argv[1]
d=json.load(open(f'{R}/work/edit_{mode}.json'));T=round(d['duration'],2)
bi=json.load(open(f'{R}/work/bint_{mode}.json'))
en='+'.join(f"between(t,{a+0.15:.2f},{b-0.05:.2f})" for a,b,_ in bi)
fc=(f"[1:v]crop=760:760:160:470,scale=320:320,format=rgba,geq=r='r(X,Y)':g='g(X,Y)':b='b(X,Y)':a='if(lte(hypot(X-160,Y-160),156),255,0)'[pip];"
    f"color=c=0xFF6B4A:s=340x340,format=rgba,geq=r='255':g='107':b='74':a='if(lte(hypot(X-170,Y-170),169),255,0)'[ring];"
    f"[0:v][ring]overlay=x=690:y=1480:enable='{en}'[v1];[v1][pip]overlay=x=700:y=1490:enable='{en}',format=yuv420p[v];"
    f"[2:a]asplit=2[vo][sc];[3:a]volume=0.10,atrim=0:{T}[m];[m][sc]sidechaincompress=threshold=0.04:ratio=5:attack=15:release=300[md];"
    f"[vo][md]amix=inputs=2:normalize=0:duration=first,afade=t=out:st={T-0.6}:d=0.6,loudnorm=I=-14:TP=-1.5:LRA=9[a]")
cmd=['ffmpeg','-y','-loglevel','error','-i',f'{R}/work/video_{mode}.mp4','-i',f'{R}/work/base_{mode}.mp4','-i',f'{R}/work/voice_{mode}.wav','-i',f'{R}/work/music_{mode}.wav',
 '-filter_complex',fc,'-map','[v]','-map','[a]','-c:v','libx264','-preset','medium','-crf','19','-c:a','aac','-b:a','192k','-ar','48000','-t',str(T),'-movflags','+faststart',f'{R}/reel_{mode}.mp4']
r=subprocess.run(cmd,capture_output=True,text=True);print(mode,'final ret',r.returncode,r.stderr[-500:])
