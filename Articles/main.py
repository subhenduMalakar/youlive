'''
#!pip3 install wikipedia google_images_download gtts request mutagen shutil requests_html pixabay requests_html inscriptis python-pixabay$
!pip3 install --upgrade google-api-python-client oauth2client progressbar2 Pillow==4.0.0 mutagen
!wget https://github.com/subhenduMalakar/neededit/archive/master.zip
!unzip master.zip
!os.chdir('/content/neededit/')
!sudo python setup.py install
'''
#import urllib
#import re
#import schedule
from datetime import datetime
import shutil
import subprocess
#import wikipedia as wi
from google_images_download import google_images_download
import re
from gtts import gTTS
#import requests, json
import time


from requests_html import HTMLSession

session = HTMLSession()
for k in range(1,2000):
    r = session.get("https://ezinearticles.com/?cat=Health-and-Fitness&page="+str(k))
    r=str(r.content).split('''<a class="article-title-link" href="''')
    link={}
    for i in range(0,20):
        #try:
        print('---------------Links >>>>i')

        print(i)
        print('---------------Pages >>>>k')

        print(k)
        p=r[i+1].split('''">''')
        link[i]=p[0]

        fobj = open("data.txt")
        text = fobj.read().split('\n')
        if link[i] in text:
            print("Matched found in text file")
            fobj.close()
            continue
        else:
            print('The program will be run')
            fobj.close()
            fobj = open("data.txt",'a')
            fobj.write('\n'+link[i])
            fobj.close()


        from requests_html import HTMLSession

        session = HTMLSession()
        r = session.get('''https://ezinearticles.com'''+link[i])
        print("------------------------------------------1")
        print('''https://ezinearticles.com'''+link[i])
        print("------------------------------------------1")
        
        title=str(r.content)
        title=title.split("<h1>")
        title=title[1].split("</h1>")
        title=title[0]
        print("------------------------------------------")
        print(title)
        print("------------------------------------------")

        r=str(r.content).split("""<div id="article-content">""")
        file = open("testfile.txt","w")
        file.write(r[1]) 
        file.close()
        
        
        print(r)
        
        
        p=r[1].split("""</div>""")
        p=p[0]
        from inscriptis import get_text
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

        RES=' '.join(title.split()[:5])

        print(RES)

        maintitle=title

        summery=text+" Subscribe our channel for more such video. Hit like for this video"

        #dirC=' '.join(new1.split()[:5])
        dirC=title
        dirC = re.sub(r"[-()\"#&/@;:<>{}`+=~|?.!,]", "", dirC)
        dirC = dirC.replace(" ","-")




        response = google_images_download.googleimagesdownload()   #class instantiation
        arguments = {"keywords":dirC,"limit":5,"print_urls":True,"format":"jpg","usage_rights":"labeled-for-reuse"}
        paths = response.download(arguments)
        print(paths)






        """
        from pixabay import Image, Video
        API_KEY = '11260031-f9096042a465b94c202846550'
        image = Image(API_KEY)
        ims = image.search(q='dirC',
                     lang='es',)

        import os
        if not os.path.exists("downloads/"+dirC+"/"):
            os.makedirs("downloads/"+dirC+"/")


        import urllib
        for i in range(0,5):
            '''
            t1 = open("downloads/"+dirC+"/"+str(i+1)+".jpg", 'wb')
            urllib.request.urlretrieve(ims['hits'][i]['largeImageURL'], "downloads/"+dirC+"/"+str(i+1)+".jpg")
            t1.close()
            '''

            f = open("downloads/"+dirC+"/"+str(i+1)+".jpg",'wb')
            f.write(urllib.request.urlopen(ims['hits'][i]['largeImageURL']).read())
            f.close()
        """


        tts = gTTS(summery, lang='en')
        tts.save(dirC+'.mp3')
        sendsum=summery
        summery=summery.replace('\n', '')
        summery = re.sub(r"[-()\"#&/@;:<>{}`+=~|!?]", "", summery)

        import datetime

        sentence_sends=summery
        #sentence_sends=sentence_sends.replace(',','.')
        sentence_sends=sentence_sends.split('.')
        current_time=datetime.datetime(100,1,10,0,0)
        number=0
        time=datetime.datetime(100,1,1,0,0,0)
        with open("vtt.vtt","a",encoding="utf-8") as f:
            f.write("WEBVTT\nKind: captions\nLanguage: en\n")
        for sentence_send in sentence_sends:
            time_add=(len(sentence_send.split()))*0.5
            time_add=int(time_add)
            end_time=current_time+datetime.timedelta(0,time_add)

            str_current_time=format(current_time.time())
            str_end_time=format(end_time.time())
            current_time=end_time#datetime.timedelta(0,1)
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
            number=number+1

        oo=1
        import os
        for filename in os.listdir("downloads/"+dirC): 
            dst =format(oo) + ".jpg"
            src ="downloads/" + dirC+"/" + filename 
            dst ="downloads/" + dirC+"/" + dst
            os.rename(src, dst)
            oo=oo+1

        from mutagen.mp3 import MP3
        audio = MP3(dirC+'.mp3')
        audio=int(audio.info.length)
        audio=format(int(audio/5))

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

        a1='ffmpeg -framerate 1/'+audio+' -i downloads/'+dirC+'/%1d.jpg -c:v libx264 -r 30 -pix_fmt yuv420p downloads/'+dirC+'/slideshow.mp4'

        subprocess.call(a1, shell=True)
        print("-------------------------------------- 2")
        b1='ffmpeg -i downloads/'+dirC+'/slideshow.mp4 -i '+dirC+'.mp3 -c copy -map 0:0 -map 1:0 downloads/'+dirC+'/Output1.mp4'
        subprocess.call(b1, shell=True)
        print("-------------------------------------- 3")
        c1='''ffmpeg -i downloads/'''+dirC+'''/Output1.mp4 -vf "subtitles=vtt.vtt:force_style='Name=Default,Fontname=Arial,Fontsize=28,PrimaryColour=&Hffffff,SecondaryColour=&Hffffff,OutlineColour=&H44000000,BackColour=&H0,BorderStyle=3,Shadow=0'" -strict -2 downloads/'''+dirC+'''/out.mp4'''
        subprocess.call(c1, shell=True)
        print("-------------------------------------- 4")

        os.remove("vtt.vtt")
        os.remove(dirC+'.mp3')
        with open("my_credentials.json","w",encoding="utf-8") as f:
            f.write("""{"access_token": "ya29.GluRBhebN8C_3eig3yI4oW4deABx0iQ78H_-sFQL1vVy259-W69dDcyu5Api81LngsLk9Sl_EeqWsNjiYoy59WxtUGN9YiFrZ8rkO8423eUk_QtAU_zNu2_HxP-v", "client_id": "968217601437-7li1ovd4v6k843iv79t1eun8kh2pa6s4.apps.googleusercontent.com", "client_secret": "65jISUDVSDhUan2KOLDho_5_", "refresh_token": "1/qwD_5r8Vi8V_dGCtfKBQXiFIluX-P4c2tPSd1wsbwrg", "token_expiry": "2019-01-14T20:14:42Z", "token_uri": "https://www.googleapis.com/oauth2/v3/token", "user_agent": null, "revoke_uri": "https://oauth2.googleapis.com/revoke", "id_token": null, "id_token_jwt": null, "token_response": {"access_token": "ya29.GluRBhebN8C_3eig3yI4oW4deABx0iQ78H_-sFQL1vVy259-W69dDcyu5Api81LngsLk9Sl_EeqWsNjiYoy59WxtUGN9YiFrZ8rkO8423eUk_QtAU_zNu2_HxP-v", "expires_in": 3600, "refresh_token": "1/qwD_5r8Vi8V_dGCtfKBQXiFIluX-P4c2tPSd1wsbwrg", "scope": "https://www.googleapis.com/auth/youtube.upload https://www.googleapis.com/auth/youtube", "token_type": "Bearer"}, "scopes": ["https://www.googleapis.com/auth/youtube.upload", "https://www.googleapis.com/auth/youtube"], "token_info_uri": "https://oauth2.googleapis.com/tokeninfo", "invalid": false, "_class": "OAuth2Credentials", "_module": "oauth2client.client"}""")

        with open("my_client_secrets.json","w",encoding="utf-8") as f:
            f.write("""{"installed":{"client_id":"968217601437-7li1ovd4v6k843iv79t1eun8kh2pa6s4.apps.googleusercontent.com","project_id":"what-is-it-all-about","auth_uri":"https://accounts.google.com/o/oauth2/auth","token_uri":"https://www.googleapis.com/oauth2/v3/token","auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs","client_secret":"65jISUDVSDhUan2KOLDho_5_","redirect_uris":["urn:ietf:wg:oauth:2.0:oob","http://localhost"]}}
        """)
        print("-------------------------------------- 5")

        '''
        RES=RES.capitalize()
        from PIL import Image,ImageDraw,ImageFont

        # sample text and font
        unicode_text = "Hello World!"
        font = ImageFont.truetype("a.ttf",200, encoding="unic")

        # get the line size
        text_width, text_height = font.getsize(unicode_text)

        # create a blank canvas with extra space between lines
        canvas = Image.new('RGB', (1920,1080), "orange")

        # draw the text onto the text canvas, and use black as the text color
        draw = ImageDraw.Draw(canvas)
        draw.text((100,500), RES, 'blue', font)

        # save the blank canvas to a file
        canvas.save("unicode-text.png", "PNG")
        '''

        RES=RES.capitalize()

        title1=maintitle
        title1=title1.capitalize()
        discrip=". The content used in this video is under the Creative Commons Attribution-ShareAlike License, all text used in this video is from various sources. I do not own it. I just make video out of this so that some people get some help.Article source "+"https://ezinearticles.com"+link[i]
        strL="youtube-upload --title="+"'"+title1+"'"+" --description='A detail information about "+title1+discrip+"'"+" --category='Music' --tags="+"'"+RES+", "+title1+"'"+" --default-language='en' --default-audio-language='en' --client-secrets='my_client_secrets.json' --credentials-file='my_credentials.json' --thumbnail=downloads/"+dirC+"/1.jpg downloads/"+dirC+"/out.mp4"
        subprocess.call(strL, shell=True)
        print("-------------------------------------- 6")
        
        #except Exception:
            #pass

        try:
            os.remove("vtt.vtt")
        except Exception:
            pass
        try:
            os.remove(dirC+'.mp3')
        except Exception:
            pass
        try:
            shutil.rmtree('downloads/'+dirC)
        except Exception:
            pass
        import time
        
        time.sleep(100)
        