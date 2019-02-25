import subeprocess

ffmpeg -v error -re -loop 1 -f image2 -i b.png -i audio.mp3 -c:v libx264 -pix_fmt yuv420p -preset veryfast -b:v 400k -r 30.0 -g 60.0 -maxrate 400k -bufsize 200k -shortest -strict experimental -f flv rtmp://a.rtmp.youtube.com/live2/mff6-g3t6-xs8d-f8sb