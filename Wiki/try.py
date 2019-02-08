from __future__ import print_function
import shutil
import subprocess
from google_images_download import google_images_download
import re
from gtts import gTTS
import requests
import time
import feedparser
from mutagen.mp3 import MP3
import os

summery="""A Day In The Life Of An Affiliate Marketer 
Being in the affiliate marketing business is not that hard now with the internet at your disposable. It is much easier now compared to the days when people have to make use of the telephones and other mediums of information just to get the latest updates on the way their program is coming along. 

So with technology at hand, and assuming that the affiliate is working from home, a day in his or her life would sound something like this…

Upon waking up and after having breakfast, the computer is turned on to check out new developments in the network. As far as the marketer is concerned there might be new things to update and statistics to keep track on. 

"""
dirC="A Day In The Life Of An Affiliate Marketer"
RES=dirC

summery=summery.replace('\n', '')
summery=summery.replace('..', '.')
summery=summery.replace('...', '.')

summery=summery.replace('. .', '.')
summery=summery.replace('  ', ' ')


dirC = re.sub(r"[-()\"#&/@;:<>{}`+=~|?.!,]", "", dirC)
dirC = dirC.replace(" ","-")
response = google_images_download.googleimagesdownload()   #class instantiation
arguments = {"keywords":dirC,"limit":4,"print_urls":True,"format":"jpg",'usage_rights':"labeled-for-reuse"}   #creating list of arguments
paths = response.download(arguments)   #passing the arguments to the function
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
    #current_time=end_time#datetime.timedelta(0,1)
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

    a1='ffmpeg -framerate 1/'+perf+' -i downloads/'+dirC+'/1.jpg -c:v libx264 -r 30 -pix_fmt yuv420p video/'+format(i1)+'.mp4'
    subprocess.call(a1, shell=True)
    import time
    time.sleep(2)
    
    b1='ffmpeg -i video/'+format(i1)+'.mp4 -i mp3/'+format(b)+'.mp3 -c copy -map 0:0 -map 1:0 video2/'+format(i1)+'.mp4'
    subprocess.call(b1, shell=True)
    
    import time
    time.sleep(2)
     
    c1='''ffmpeg -i video2/'''+format(i1)+'''.mp4 -vf "subtitles=vtt.vtt:force_style='Name=Default,Fontname=Arial,Fontsize=28,PrimaryColour=&Hffffff,SecondaryColour=&Hffffff,OutlineColour=&H44000000,BackColour=&H0,BorderStyle=3,Shadow=0'" -strict -2 video3/'''+format(i1)+'''.mp4'''
    subprocess.call(c1, shell=True)
     
    i1=i1+1
    i2=i2+1
    print(b1)
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
test = 'video/*'
r = glob.glob(test)
for i in r:
   os.remove(i)
   
import glob, os
test = 'video2/*'
r = glob.glob(test)
for i in r:
   os.remove(i)

import glob, os
test = 'video3/*'
r = glob.glob(test)
for i in r:
   os.remove(i)

import glob, os
test = 'mp3/*'
r = glob.glob(test)
for i in r:
   os.remove(i)




with open("my_credentials.json","w",encoding="utf-8") as f:
    f.write("""{"access_token": "ya29.Glx7Bk7z5Ik_ygfLPiY8exQ92wSqE1leETW8F1WSXL44XeCpadTqIjMZAIgVj_C9v6I0rRd6vS8FlymfP4A-QvKKShamP6oQ5BR9Z6jCtTewcfNKCAybX2gjr0CQlQ", "client_id": "968217601437-7li1ovd4v6k843iv79t1eun8kh2pa6s4.apps.googleusercontent.com", "client_secret": "65jISUDVSDhUan2KOLDho_5_", "refresh_token": "1/j3pazwFEWotcf_ismaHPLlJC_DLioNb_-OlifaRp3OI", "token_expiry": "2018-12-23T19:13:03Z", "token_uri": "https://www.googleapis.com/oauth2/v3/token", "user_agent": null, "revoke_uri": "https://oauth2.googleapis.com/revoke", "id_token": null, "id_token_jwt": null, "token_response": {"access_token": "ya29.Glx7Bk7z5Ik_ygfLPiY8exQ92wSqE1leETW8F1WSXL44XeCpadTqIjMZAIgVj_C9v6I0rRd6vS8FlymfP4A-QvKKShamP6oQ5BR9Z6jCtTewcfNKCAybX2gjr0CQlQ", "expires_in": 3600, "scope": "https://www.googleapis.com/auth/youtube https://www.googleapis.com/auth/youtube.upload", "token_type": "Bearer"}, "scopes": ["https://www.googleapis.com/auth/youtube", "https://www.googleapis.com/auth/youtube.upload"], "token_info_uri": "https://oauth2.googleapis.com/tokeninfo", "invalid": false, "_class": "OAuth2Credentials", "_module": "oauth2client.client"}
""")

with open("my_client_secrets.json","w",encoding="utf-8") as f:
    f.write("""{"installed":{"client_id":"968217601437-7li1ovd4v6k843iv79t1eun8kh2pa6s4.apps.googleusercontent.com","project_id":"what-is-it-all-about","auth_uri":"https://accounts.google.com/o/oauth2/auth","token_uri":"https://www.googleapis.com/oauth2/v3/token","auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs","client_secret":"65jISUDVSDhUan2KOLDho_5_","redirect_uris":["urn:ietf:wg:oauth:2.0:oob","http://localhost"]}}
""")
print("-------------------------------------- 5")



from PIL import Image,ImageDraw,ImageFont

# sample text and font
unicode_text = "Hello World!"
font = ImageFont.truetype("Oxygen-Bold.ttf",200, encoding="unic")

# get the line size
text_width, text_height = font.getsize(unicode_text)

# create a blank canvas with extra space between lines
canvas = Image.new('RGB', (1920,1080), "#F7E394")

# draw the text onto the text canvas, and use black as the text color
draw = ImageDraw.Draw(canvas)
def wrap_by_word(s, n):
    '''returns a string where \\n is inserted between every n words'''
    s = s.split(" ")
    ret = ''
    for i in range(0, len(s), n):
        ret += ' '.join(s[i:i+n]) + '\n'

    return ret

x = wrap_by_word('This content under the Creative Commons',3)
print(x)
draw.text((100,200), x, '#5973EA', font)

# save the blank canvas to a file
canvas.save("unicode-text.png", "PNG")


title1=RES +" | Information about "+ dirC
title1=title1.capitalize()
discrip=". This content under the Creative Commons Attribution-ShareAlike License, all text used in this video is from wikipedia. I do not own it. I just make video out of this so that some people get some help."

strL="youtube-upload --title="+"'"+title1+"'"+" --description='A detail information about "+RES+discrip+"'"+" --category='Music' --tags="+"'"+RES+", "+dirC+"'"+" --default-language='en' --default-audio-language='en' --client-secrets='my_client_secrets.json' --credentials-file='my_credentials.json' --thumbnail='unicode-text.png' output.mp4"
subprocess.call(strL, shell=True)
print("-------------------------------------- 6")

try:
    os.remove("vtt.vtt")
except Exception:
    pass
try:
    os.remove('unicode-text.png')
    os.remove('output+.mp4')
except Exception:
    pass
try:
    shutil.rmtree('downloads/'+dirC)
except Exception:
    pass
print(format(l1)+a1+b1+c1+" Itaration--->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
import time
time.sleep(100)