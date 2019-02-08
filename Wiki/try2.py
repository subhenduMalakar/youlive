import glob
from PIL import Image
from selenium import webdriver 
import os

# get a list of all the files to open
glob_folder = os.path.join('D:\Progra work\videoyoutube\Subtitlefixed', '*.html')

html_file_list = glob.glob(glob_folder)
index = 1

for html_file in html_file_list:

    # get the name into the right format
    temp_name = "file://" + html_file

    # open in webpage
    print(temp_name)
    driver.get(temp_name)
    save_path='D:\Progra work\videoyoutube\Subtitlefixed'
    save_name = '00' + str(index) + '.png'       
    driver.save_screenshot(save_path, save_name)
    driver.quit()
    index += 1

    # crop as required
    img = Image.open(save_path, save_name)
    box = (1, 1, 1000, 1000)
    area = img.crop(box)
    area.save('cropped_image' + str(index), 'png')
    
    
    



'''
from selenium import webdriver
 
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "C:/cr/chromedriver.exe"
driver = webdriver.Chrome(chrome_options=options)

 
driver.get('file:///D:/Progra%20work/videoyoutube/Subtitlefixed/a.html')
driver.save_screenshot("screenshot.png")
 
driver.close()

'''


from PIL import Image

from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/cr/chromedriver.exe')
driver.get('file:///D:/Progra%20work/videoyoutube/Subtitlefixed/a.html')
driver.save_screenshot("screenshot.png")
driver.close()















                        #File_Name_of_photos = re.sub('[^A-Za-z0-9]+', ' ', summery[0:30])
                        response = google_images_download.googleimagesdownload()   #class instantiation

                        arguments = {"keywords":dirC,"limit":4,"print_urls":True,"format":"jpg"}   #creating list of arguments
                        paths = response.download(arguments)   #passing the arguments to the function
                        print(paths)

                        tts = gTTS(summery, lang='en')
                        tts.save(dirC+'.mp3')
                        sendsum=summery
                        summery=summery.replace('\n', '')

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
                        audio=format(int(audio/4))

                        from PIL import Image
                        import os

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

--------------------------------------------------------------------------------------------------
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
                        font = ImageFont.truetype("a.ttf",200, encoding="unic")
    
                        # get the line size
                        text_width, text_height = font.getsize(unicode_text)
    
                        # create a blank canvas with extra space between lines
                        canvas = Image.new('RGB', (1920,1080), "orange")
    
                        # draw the text onto the text canvas, and use black as the text color
                        draw = ImageDraw.Draw(canvas)
                        draw.text((100,450), search_List[0], 'blue', font)
    
                        # save the blank canvas to a file
                        canvas.save("unicode-text.png", "PNG")

    
                        title1=RES +" | Information about "+ search_List[0]
                        title1=title1.capitalize()
                        discrip=". This content under the Creative Commons Attribution-ShareAlike License, all text used in this video is from wikipedia. I do not own it. I just make video out of this so that some people get some help."
                        strL="youtube-upload --title="+"'"+title1+"'"+" --description='A detail information about "+RES+discrip+"'"+" --category='Music' --tags="+"'"+RES+", "+search_List[0]+"'"+" --default-language='en' --default-audio-language='en' --client-secrets='my_client_secrets.json' --credentials-file='my_credentials.json' --thumbnail='unicode-text.png' output.mp4"
                        subprocess.call(strL, shell=True)
                        print("-------------------------------------- 6")

                        try:
                            os.remove("vtt.vtt")
                        except Exception:
                            pass
                        try:
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
                except Exception:
                    pass
                
                
def wrap_by_word(s, n):
    '''returns a string where \\n is inserted between every n words'''
    a = s.split()
    ret = ''
    for i in range(0, len(a), n):
        ret += ' '.join(a[i:i+n]) + '\n'

    return ret

x = wrap_by_word('There is a dog and fox fighting in the park and there is an apple falling down.', 3)
print(x)