# -*- coding: utf-8 -*-
'''

ffmpeg -ss 00:01:00 -i input.mp4 -to 00:02:00 -c copy output.mp4

ffmpeg -i input1.mp4 -c copy -bsf:v h264_mp4toannexb -f mpegts intermediate1.ts
ffmpeg -i input2.mp4 -c copy -bsf:v h264_mp4toannexb -f mpegts intermediate2.ts
ffmpeg -i "concat:intermediate1.ts|intermediate2.ts" -c copy -bsf:a aac_adtstoasc output.mp4


ffmpeg -i input.mp4 -vf "subtitles=vtt.vtt:force_style='Name=Default,Fontname=Arial,Fontsize=28,PrimaryColour=&Hffffff,SecondaryColour=&Hffffff,OutlineColour=&H44000000,BackColour=&H0,BorderStyle=4,Shadow=0" -strict -2 out1.mp4
'''

from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
ffmpeg_extract_subclip("video1.mp4", start_time, end_time, targetname="test.mp4")




ffmpeg -y -i a.mp4 -itsoffset 00:00:07 -i b.mp3 -map 0:0 -map 1:0 -c:v copy -async 1 out.mp4