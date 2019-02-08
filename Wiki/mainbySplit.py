import shutil
import subprocess
from google_images_download import google_images_download
import re
from gtts import gTTS
import requests
import time
import feedparser
with open("NewData.txt",'a'):
    print("The File Is Wreated")
new1='a'
while(True):
    url = 'https://news.google.com/rss/search?q=site%3Andtv.com&hl=en-IN&gl=IN&ceid=IN%3Aen'
    d = feedparser.parse(url)
    if(d.entries[1].title!=new1):
        new1=d.entries[0].title
        NewData = open("NewData.txt")
        text2 = NewData.read().split('\n')
        if new1 in text2:
            print("RSS Matched found in NewData file")
        else:
            print("New--->")
            NewData.close()
            NewData = open("NewData.txt",'a')
            NewData.write('\n'+new1)
            NewData.close()

            from requests_html import HTMLSession
            session = HTMLSession()
            r = session.get(d.entries[0].link)
            r=str(r.content).split("""<div itemprop="articleBody" class="ins_storybody" id="ins_storybody">""")
            p=r[1].split("""<div class="comments_slide dismiss""")
            p=p[0]
            from inscriptis import get_text
            text = get_text(p)
            text=text.replace("\n", "")
            text = get_text(p)
            text=text.replace("\n","")
            text=text.replace("\\t","")
            text=text.replace("\\n","")
            text=text.replace("*","")
            text=text.replace("\\r","")
            text=text.replace("\\t","")
            text=text.replace("\\n","")
            text=text.replace("*","")
            text=text.replace("  ","")
            text=text.replace('''\\''',"")

            RES=' '.join(new1.split()[:5])

            print(RES)

            maintitle=' '.join(new1.split()[:10])

            summery=text


            #dirC=' '.join(new1.split()[:5])
            dirC=new1
            dirC = re.sub(r"[-()\"#&/@;:<>{}`+=~|?.!,]", "", dirC)
            dirC = dirC.replace(" ","-")

            #File_Name_of_photos = re.sub('[^A-Za-z0-9]+', ' ', summery[0:30])
            response = google_images_download.googleimagesdownload()   #class instantiation

            arguments = {"keywords":dirC,"limit":4,"print_urls":True,"format":"jpg",'usage_rights':"labeled-for-reuse"}   #creating list of arguments
            paths = response.download(arguments)   #passing the arguments to the function
            print(paths)

            tts = gTTS(summery, lang='en')
            tts.save(dirC+'.mp3')
            sendsum=summery
            summery=summery.replace('\n', '.')
            summery = re.sub(r"[-()\"#&/@;:<>{}`+=~|!?]", "", summery)
            summery=summery.replace('\n', '')
            summery=summery.replace('..', '.')
            summery=summery.replace('. .', '.')
            summery=summery.replace('  ', ' ')


            from mutagen.mp3 import MP3
            audio = MP3(dirC+'.mp3')
            audio=int(audio.info.length)
            audio=format(int(audio/4))
            
            
            oo=1
            import os
            for filename in os.listdir("downloads/"+dirC):
                dst =format(oo) + ".jpg"
                src ="downloads/" + dirC+"/" + filename
                dst ="downloads/" + dirC+"/" + dst
                os.rename(src, dst)
                oo=oo+1
            
            
            a1='ffmpeg -framerate 1/'+audio+' -i downloads/'+dirC+'/%1d.jpg -c:v libx264 -r 30 -pix_fmt yuv420p downloads/'+dirC+'/slideshow.mp4'
            subprocess.call(a1, shell=True)



            start_time=0.1
            import datetime
            from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
            a=0
            b=1
            sentence_sends=summery
            sentence_sends=sentence_sends.split('.')
            sentence_sends = sentence_sends[:-1]
            #sentence_sends=sentence_sends.replace(',','.')
            current_time=datetime.datetime(100,1,10,0,0)
            number=0
            time=datetime.datetime(100,1,1,0,0,0)
            with open("vtt.vtt","a",encoding="utf-8") as f:
                f.write("WEBVTT\nKind: captions\nLanguage: en\n")
            for sentence_send in sentence_sends:
                '''-------------------------------------'''
                tts = gTTS(sentence_send, lang='en')
                tts.save(format(b)+'.mp3')
                import time
                time.sleep(2)
                audio = MP3(format(b)+'.mp3')
                audio=float(audio.info.length)
                a=a+audio
                
                
                
                import time
                time.sleep(2)
                print(a)
                '''-------------------------------------'''

                time_add=audio
                time_add=int(time_add)
                end_time=current_time+datetime.timedelta(0,time_add)
                str_current_time=format(current_time.time())
                str_end_time=format(end_time.time())
                #current_time=end_time#datetime.timedelta(0,1)
                with open("vtt.vtt","w",encoding="utf-8") as f:
                    f.write("WEBVTT\nKind: captions\nLanguage: en\n")
                with open("vtt.vtt","a",encoding="utf-8") as f:
                    print(sentence_send)
                    #.write(str(number))
                    f.write("\n")
                    f.write(str_current_time)
                    f.write(".1")
                    f.write(" --> ")
                    f.write(str_end_time)
                    f.write(".1")
                    f.write("\n")
                    f.write(sentence_send)
                    f.write("\n")
                    f.write("\n")
                
                end_time=start_time+audio
                ffmpeg_extract_subclip("downloads/"+dirC+"/slideshow.mp4", start_time, end_time, targetname="video/a.mp4")
                start_time=end_time
                
                
                
                b1="ffmpeg -i video/a.mp4 -i "+format(b)+".mp3 -c copy -map 0:0 -map 1:0 video/b.mp4"
                subprocess.call(b1, shell=True)
                
                
                
                
                c1='''ffmpeg -i video/b.mp4 -vf "subtitles=vtt.vtt:force_style='Name=Default,Fontname=Arial,Fontsize=28,PrimaryColour=&Hffffff,SecondaryColour=&Hffffff,OutlineColour=&H44000000,BackColour=&H0,BorderStyle=3,Shadow=0'" -strict -2 video/'''+str(number)+'''.mp4'''
                subprocess.call(c1, shell=True)
                
                
                
                
                number=number+1
                try:
                    os.remove(format(b)+".mp3")
                    import time
                    time.sleep(2)
                    os.remove("video/a.mp4")
                    os.remove("video/b.mp4")
                    b=b+1
                except Exception:
                    pass




            from PIL import Image
            import os, sys

            path = 'downloads/'+dirC
            directory = path
            for file_name in os.listdir(directory):
              print("Processing %s" % file_name)
              image = Image.open(os.path.join(directory, file_name))

              x,y = image.size
              new_dimensions = (1920,1080)
              output = image.resize(new_dimensions, Image.ANTIALIAS)

              output_file_name = os.path.join(directory,file_name)
              output.save(output_file_name, "JPEG", quality = 95)
            print("-------------------------------------- 1")
            import subprocess
            import os



            print(summery)

            # print("-------------------------------------- 2")
            #b1='ffmpeg -i downloads/'+dirC+'/slideshow.mp4 -i '+dirC+'.mp3 -c copy -map 0:0 -map 1:0 downloads/'+dirC+'/Output1.mp4'
            # subprocess.call(b1, shell=True)
            # print("-------------------------------------- 3")
            # c1='''ffmpeg -i downloads/'''+dirC+'''/Output1.mp4 -vf "subtitles=vtt.vtt:force_style='Name=Default,Fontname=Arial,Fontsize=28,PrimaryColour=&Hffffff,SecondaryColour=&Hffffff,OutlineColour=&H44000000,BackColour=&H0,BorderStyle=3,Shadow=0'" -strict -2 downloads/'''+dirC+'''/out.mp4'''
            # subprocess.call(c1, shell=True)
            # print("-------------------------------------- 4")
            # os.remove("vtt.vtt")
            # os.remove(dirC+'.mp3')
