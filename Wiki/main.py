
'''
#!pip3 install wikipedia google_images_download gtts request mutagen shutil
!pip3 install --upgrade google-api-python-client oauth2client progressbar2 Pillow==4.0.0

!wget https://github.com/subhenduMalakar/neededit/archive/master.zip

!unzip master.zip
!os.chdir('/content/neededit/')
!sudo python setup.py install

'''


#import urllib
#import re
#import schedule
from mutagen.mp3 import MP3
from datetime import datetime
import shutil
import subprocess
import wikipedia as wi
from google_images_download import google_images_download
import re
from gtts import gTTS
import requests, json
import time
counting_video_number=1
def count(list):
    item_count = 0
    for item in list[:]:
        item_count = item_count + 1
    return item_count

for yi1 in range(97,123):
    ya1=chr(yi1)
    for yj1 in range(100,123):
        yb1=chr(yj1)
        if(yi1==97 and yj1==100):
            kk1=101
        else:
            kk1=97
        
            
        for yk1 in range(kk1,123):
            yc1=chr(yk1)
            print("Start-----1")

            
            
            
            """
            from lxml.html import fromstring
            import requests
            from itertools import cycle
            import traceback

            def get_proxies():
                url = 'https://free-proxy-list.net/'
                response = requests.get(url)
                parser = fromstring(response.text)
                proxies = set()
                for i in parser.xpath('//tbody/tr')[:10]:
                    if i.xpath('.//td[7][contains(text(),"yes")]'):
                        proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
                        proxies.add(proxy)
                return proxies

            #If you are copy pasting proxy ips, put in the list below
            #proxies = ['121.129.127.209:80', '124.41.215.238:45169', '185.93.3.123:8080', '194.182.64.67:3128', '106.0.38.174:8080', '163.172.175.210:3128', '13.92.196.150:8080']
            proxies = get_proxies()
            proxy_pool = cycle(proxies)
                #Get a proxy from the pool
            proxy = next(proxy_pool)
            print("Request #%d")
            try:
                response = requests.get(URL,proxies={"http": proxy, "https": proxy})
                print(response.json())
            except:
                #Most free proxies will often get connection errors. You will have retry the entire request using another proxy to work. 
                #We will just skip retries as its beyond the scope of this tutorial and we are only downloading a single url 
                print("Skipping. Connnection error")
                continue
            """
            #try:
            URL="http://suggestqueries.google.com/complete/search?client=firefox&q=what is "+ya1+yb1+yc1
            headers = {'user-agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5)'
                          'AppleWebKit/537.36 (KHTML, like Gecko)'
                          'Chrome/45.0.2454.101 Safari/537.36'),
                          'referer': 'http://stats.nba.com/scores/'}
            response = requests.get(URL, headers=headers)
            if response.status_code==400:
                
                print("\nProblem in Response 400---------------Get IN")
                print(URL)
                for jj in range(0,50):
                    time.sleep(0.2)
                    print(" 400 Response-",end =" ")

                    print(jj,end =" ")

                continue
            if response.status_code!=200:
                print("\nProblem in Response not 200---------------start\n")
                print(response.status_code)

                results = response.json()
                print(results)

                for jj in range(0,50):
                    time.sleep(0.2)
                    print(jj,end =" ")

                print("\nProblem in Response not 200---------------End\n")
                continue
            results = response.json()
            print(results)
            #except Exception:
            #    print("Problem----------------------->")
             #   continue
              #  pass

            
            try:
                for l1 in range(0,(count(results[1])-1)):
                    print(str(l1)+ya1+yb1+yc1)

                    """
                    headers = {'User-agent':'Mozilla/5.0'}
                    response = requests.get(URL, headers=headers)
                    print(response)
                    """
                    RES=results[1][l1]

                    fobj = open("data.txt")
                    text = fobj.read().split('\n')
                    search_List=wi.search(RES)
                    print(search_List)
                    if count(search_List)==0:
                        print("Empty")
                        continue
                    summery=wi.summary(search_List[0])
                    dirC=search_List[0]
                    print(dirC)
                    s=dirC
                    if s in text:
                        print("Matched found in text file")
                    else:
                        print('The program will be run')
                        fobj.close()
                        fobj = open("data.txt",'a')
                        fobj.write('\n'+s)
                        fobj.close()

                        print(RES)
                        search_List=wi.search(RES)
                        summery=wi.summary(search_List[0])
                        dirC=search_List[0]
                        dirC = dirC.replace("-"," ")

                        summery=summery+".Subscribe Our Channel for More Such Informative Short Video."
                        summery=summery.replace('\n', '')
                        summery=summery.replace('..', '.')
                        summery=summery.replace('...', '.')

                        summery=summery.replace('. .', '.')
                        summery=summery.replace('  ', ' ')


                        dirC = re.sub(r"[-()\"#&/@;:<>{}`+=~|?.!,]", "", dirC)
                        dirC = dirC.replace(" ","-")
                        response = google_images_download.googleimagesdownload()   
                        arguments = {"keywords":dirC,"limit":2,"print_urls":True,"format":"jpg",'usage_rights':"labeled-for-reuse"}   
                        paths = response.download(arguments) 
                        print(paths)

                        sendsum=summery
                        summery=summery.replace('\n', '.')
                        summery = re.sub(r"[-()\"#&/@;:<>{}`+=~|!?]", "", summery)
                        summery=summery.replace('\n', '')
                        summery=summery.replace('..', '.')
                        summery=summery.replace('. .', '.')
                        summery=summery.replace('  ', ' ')

                        oo=1
                        import os
                        for filename in os.listdir("downloads/"+dirC):
                            dst =format(oo) + ".jpg"
                            src ="downloads/" + dirC+"/" + filename
                            dst ="downloads/" + dirC+"/" + dst
                            os.rename(src, dst)
                            oo=oo+1

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


                        len=0.01
                        start_time=0.1
                        import datetime
                        from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
                        a=0
                        b=1
                        i1=1
                        i2=2
                        sentence_sends=summery
                        sentence_sends=sentence_sends.split('.')
                        sentence_sends = sentence_sends[:-1]
                        current_time=datetime.datetime(100,1,10,0,0)
                        number=0
                        time=datetime.datetime(100,1,1,0,0,0)

                        for sentence_send in sentence_sends:
                            '''-------------------------------------'''
                            print("Start of LOOP ------------------------->")

                            tts = gTTS(sentence_send, lang='en')
                            tts.save('mp3/'+format(b)+'.mp3')
                            import time
                            time.sleep(2)
                            audio = MP3('mp3/'+format(b)+'.mp3')
                            audio=float(audio.info.length)
                            perf=format(audio)
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
                            with open("vtt.vtt","w",encoding="utf-8") as f:
                                f.write("WEBVTT\nKind: captions\nLanguage: en\n")

                            with open("vtt.vtt","a",encoding="utf-8") as f:
                                print(sentence_send)
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

                            a123='ffmpeg -framerate 1/'+perf+' -i downloads/'+dirC+'/1.jpg -c:v libx264 -r 30 -pix_fmt yuv420p video/'+format(i1)+'.mp4'
                            subprocess.call(a123, shell=True)
                            import time
                            time.sleep(2)

                            b123='ffmpeg -i video/'+format(i1)+'.mp4 -i mp3/'+format(b)+'.mp3 -c copy -map 0:0 -map 1:0 video2/'+format(i1)+'.mp4'
                            subprocess.call(b123, shell=True)

                            import time
                            time.sleep(2)

                            c123='''ffmpeg -i video2/'''+format(i1)+'''.mp4 -vf "subtitles=vtt.vtt:force_style='Name=Default,Fontname=Arial,Fontsize=25,PrimaryColour=&Hffffff,SecondaryColour=&Hffffff,OutlineColour=&H44000000,BackColour=&40,BorderStyle=2,Shadow=3'" -strict -2 video3/'''+format(i1)+'''.mp4'''
                            subprocess.call(c123, shell=True)

                            i1=i1+1
                            i2=i2+1
                            #print(b1)
                            len=len+audio
                            number=number+1
                            b=b+1

                            with open("mylist1.txt","w",encoding="utf-8") as f:
                                f.write("")
                        path = 'video3/'
                        files = os.listdir(path)
                        for i in range(0,1000):
                            if format(i)+".mp4" in files:
                                print(format(i)+".mp4")
                                with open("video3/mylist1.txt","a",encoding="utf-8") as f:
                                    f.write("file "+"'"+format(i)+".mp4"+"'")
                                    f.write("\n")
                        subprocess.call("ffmpeg -f concat -safe 0 -i video3/mylist1.txt -c copy output.mp4", shell=True)

                        import glob, os

                        try:
                            test = 'video/*'
                            r = glob.glob(test)
                            for i in r:
                                os.remove(i)
                        except Exception:
                            pass
                        try:
                            test = 'video2/*'
                            r = glob.glob(test)
                            for i in r:
                               os.remove(i)
                        except Exception:
                            pass
                        try:
                            test = 'video3/*'
                            r = glob.glob(test)
                            for i in r:
                               os.remove(i)
                        except Exception:
                            pass
                        try:
                            test = 'mp3/*'
                            r = glob.glob(test)
                            for i in r:
                               os.remove(i)
                        except Exception:
                            pass
                        try:
                            os.remove("vtt.vtt")
                        except Exception:
                            pass




                        with open("my_credentials.json","w",encoding="utf-8") as f:
                            f.write("""{"access_token": "ya29.GlujBtd3ao_k_bDDO1Ui7YixBlaD7LfeN9n7ez8OEPgQDjII2ZVh7STUG9KX7BZf29sNiPWkCxKmy6NUjONaDv45dr47-RQMeIpJ8yXI90K4tGiMrQVmETLq50Jc", "client_id": "968217601437-7li1ovd4v6k843iv79t1eun8kh2pa6s4.apps.googleusercontent.com", "client_secret": "65jISUDVSDhUan2KOLDho_5_", "refresh_token": "1/TEJLLAh67LqeA2ENOeGzVFirCVZy8v4GIZWwoL6YAVg", "token_expiry": "2019-02-01T19:18:31Z", "token_uri": "https://www.googleapis.com/oauth2/v3/token", "user_agent": null, "revoke_uri": "https://oauth2.googleapis.com/revoke", "id_token": null, "id_token_jwt": null, "token_response": {"access_token": "ya29.GlujBtd3ao_k_bDDO1Ui7YixBlaD7LfeN9n7ez8OEPgQDjII2ZVh7STUG9KX7BZf29sNiPWkCxKmy6NUjONaDv45dr47-RQMeIpJ8yXI90K4tGiMrQVmETLq50Jc", "expires_in": 3600, "refresh_token": "1/TEJLLAh67LqeA2ENOeGzVFirCVZy8v4GIZWwoL6YAVg", "scope": "https://www.googleapis.com/auth/youtube https://www.googleapis.com/auth/youtube.upload", "token_type": "Bearer"}, "scopes": ["https://www.googleapis.com/auth/youtube", "https://www.googleapis.com/auth/youtube.upload"], "token_info_uri": "https://oauth2.googleapis.com/tokeninfo", "invalid": false, "_class": "OAuth2Credentials", "_module": "oauth2client.client"}
                        """)

                        with open("my_client_secrets.json","w",encoding="utf-8") as f:
                            f.write("""{"installed":{"client_id":"968217601437-7li1ovd4v6k843iv79t1eun8kh2pa6s4.apps.googleusercontent.com","project_id":"what-is-it-all-about","auth_uri":"https://accounts.google.com/o/oauth2/auth","token_uri":"https://www.googleapis.com/oauth2/v3/token","auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs","client_secret":"65jISUDVSDhUan2KOLDho_5_","redirect_uris":["urn:ietf:wg:oauth:2.0:oob","http://localhost"]}}
                        """)
                        print("-------------------------------------- 5")



                        from PIL import Image,ImageDraw,ImageFont

                        # sample text and font
                        unicode_text = "Hello World!"
                        font = ImageFont.truetype("Oxygen-Bold.ttf",150, encoding="unic")

                        # get the line size
                        text_width, text_height = font.getsize(unicode_text)

                        # create a blank canvas with extra space between lines
                        canvas = Image.new('RGB', (1920,1080), "#F7E394")

                        # draw the text onto the text canvas, and use black as the text color
                        draw = ImageDraw.Draw(canvas)




                        def wrap_by_word(s, n):
                            '''returns a string where \\n is inserted between every n words'''
                            a12 = s.split()
                            ret = ''
                            for i in range(0, count(a12), n):
                                ret += ' '.join(a12[i:i+n]) + '\n'

                            return ret

                        x = wrap_by_word(search_List[0], 3)
                        print(x)
                        draw.text((100,200), x, '#5973EA', font)

                        # save the blank canvas to a file
                        canvas.save("downloads/unicode-text.png", "PNG")
                        import time
                        time.sleep(5)


                        title1="Learn about "+ search_List[0]+" | " +RES
                        title1=title1.capitalize()
                        discrip=". This content under the Creative Commons Attribution-ShareAlike License, all text used in this video is from wikipedia. I do not own it. I just make video out of this so that some people get some help."
                        strL="youtube-upload --title="+"'"+title1+"'"+" --description='A detail information about "+RES+discrip+"'"+" --category='Music' --tags="+"'"+RES+", "+search_List[0]+"'"+" --default-language='en' --default-audio-language='en' --client-secrets='my_client_secrets.json' --credentials-file='my_credentials.json' --thumbnail='downloads/unicode-text.png' output.mp4"
                        subprocess.call(strL, shell=True)
                        print("-------------------------------------- 6")

                        try:
                            os.remove("vtt.vtt")
                        except Exception:
                            pass
                        try:
                            os.remove('output.mp4')
                        except Exception:
                            pass

                        try:
                            os.remove('output.mp4')
                        except Exception:
                            pass

                        try:
                            shutil.rmtree('downloads/'+dirC)
                        except Exception:
                            pass
                        print(format(l1)+ya1+yb1+yc1+" Itaration--->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                        print(format(counting_video_number)+"<<<<<<<---------------------------Number Video Is This.")
                        counting_video_number=counting_video_number+1
                        import time
                        print("Sleep--------------------2")
                        for jj in range(0,50):
                            time.sleep(0.1)
                            
                        print("Sleep--------------------2 End")
                        #import os
                        #os.system('cls||clear')
        
            except Exception:
                print("Exception")
                print(" and sleep---------->")
                for jj in range(0,50):
                    time.sleep(0.2)
                    print(jj,end =" ")
                pass