import os

stream_url = "rtmp://a.rtmp.youtube.com/live2/0mhk-pmhj-ryg2-9tfb-62tg
video_file = "video.mp4"

while True:
    os.system(f"ffmpeg -re -stream_loop -1 -i {video_file} -c:v libx264 -preset veryfast -maxrate 3000k -bufsize 6000k -pix_fmt yuv420p -g 50 -c:a aac -b:a 128k -f flv {stream_url}")
