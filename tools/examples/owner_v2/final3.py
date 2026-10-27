import subprocess,sys
R='/home/claude/reels/agi_owner';var=sys.argv[1];T=87.6
fc=(f"[1:a]asplit=2[vo][sc];[2:a]volume=0.09,atrim=0:{T}[m];[m][sc]sidechaincompress=threshold=0.04:ratio=5:attack=15:release=300[md];"
    f"[vo][md]amix=inputs=2:normalize=0:duration=first,afade=t=out:st={T-0.5}:d=0.5,loudnorm=I=-14:TP=-1.5:LRA=9[a]")
r=subprocess.run(['ffmpeg','-y','-loglevel','error','-i',f'{R}/work/video3_{var}.mp4','-i',f'{R}/work/clean48.wav','-i',f'{R}/work/music_full.wav','-filter_complex',fc,'-map','0:v','-map','[a]','-c:v','copy','-c:a','aac','-b:a','192k','-ar','48000','-t',str(T),'-movflags','+faststart',f'{R}/reel3_{var}.mp4'],capture_output=True,text=True)
print(var,'final ret',r.returncode,r.stderr[-300:])
