import subprocess
# window: (clip, start, end, clip_offset)
WIN=[('protein',9.8,12.45,0),('robotlab',24.0,31.75,0),('fam',54.4,58.6,0),('dna',58.6,63.75,0),('robotlab',65.4,71.35,8)]
T=87.6;W,H=980,760
inputs=['-f','lavfi','-i',f'color=c=black:s={W}x{H}:r=30:d={T}']
fc=[];last='[0:v]'
for k,(c,s,e,off) in enumerate(WIN):
    inputs+=['-stream_loop','-1','-i',f'clips/clip_{c}.mp4']
    d=e-s
    fc.append(f"[{k+1}:v]trim=start={off}:duration={d},setpts=PTS-STARTPTS+{s}/TB,scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},eq=saturation=1.1:contrast=1.05[c{k}]")
    fc.append(f"{last}[c{k}]overlay=0:0:enable='between(t,{s},{e})':eof_action=pass[o{k}]");last=f'[o{k}]'
cmd=['ffmpeg','-y','-loglevel','error',*inputs,'-filter_complex',';'.join(fc),'-map',last,'-t',str(T),'-r','30','-c:v','libx264','-preset','fast','-crf','20','-pix_fmt','yuv420p','work/cliptrack.mp4']
r=subprocess.run(cmd,capture_output=True,text=True);print(r.returncode,r.stderr[-400:])
