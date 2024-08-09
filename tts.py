import android 
import androidhelper
import wikipedia
import pyjokes
import time
import requests
import json
engine=androidhelper.Android() 
droid = android.Android() 
engine.ttsSpeak("Welcome how can I help you today")     
print("Welcome how can I help you today?") 
time.sleep(4)
(id, result, error) = droid.recognizeSpeech("Say something") 
if "news" in result:
    url=f"https://newsapi.org/v2/everything?q={result}&from=2024-01-13&sortBy=publishedAt&apiKey=70994f287ef3476c96007371ec9ed73a"
        final=requests.get(url) 
            news=json.loads(final.text) 
                for article in news["article"]:
                        print(article["title"]) 
                                print(article["description"])
                                        engine.ttsSpeak(article["title"])
                                                engine.ttsSpeak(article["description"]) 
                                                list=['https://youtu.be/euCqAq6BRa4?si=OAbX432U746mK_Q7','https://youtu.be/3AtDnEC4zak?si=y6YWdxZFOogRQPng'
                                                ,'https://youtu.be/RgKAFK5djSk?si=xSyOa6dZwtMfBwAU','https://youtu.be/nyuo9-OjNNg?si=smiuFDQu5gUDjoLp',
                                                "https://youtube.com/playlist?list=PLu0W_9lII9aiXlHcLx-mDH1Qul38wD3aR&si=sxpev7QKdhe3Q4ZM"]
                                                query=result
                                                if " camera" in query:
                                                    # Launch the camera preview
                                                        droid.cameraStartPreview()
                                                            # You can add a toast message here to indicate that the camera is open
                                                                droid.makeToast("Camera preview started")

                                                                # Optionally, you can close the camera preview after a certain duration
                                                                # time.sleep(10)  # Import time module if not imported
                                                                # droid.cameraStopPreview()

                                                                    #Take picture
                                                                       # droid.cameraCapturePicture("/sdcard/picture.jpg")
                                                                            #droid.startActivity("/sdcard/picture.jpg")
                                                                            if "spotify" in query:
                                                                                droid.startActivity('android.intent.action.VIEW','https://open.spotify.com/track/2qgXrzJsry4KgYoJCpuaul?si=XgTCc3vMQva9dzwIryE84g') 
                                                                                    engine.ttsSpeak("playing choo lo in spotify") 
                                                                                    if "Wikipedia" in query:
                                                                                        summery = wikipedia.summary(query, sentences = 10) 
                                                                                            engine.ttsSpeak(www.summery.wikipedia) #www.virat kohli.wikipedia
                                                                                                print(www.summery.wikipedia,error)   
                                                                                                if "joke" in query:
                                                                                                    My_joke=pyjokes.get_joke(language="en",category="all") 
                                                                                                        engine.ttsSpeak(My_joke) 
                                                                                                            print(My_joke) 
                                                                                                            elif "Harry" in query:
                                                                                                                droid.startActivity('android.intent.action.VIEW',list[4]) 
                                                                                                                    engine.ttsSpeak("playing")
                                                                                                                    elif "Twitter" in query:
                                                                                                                        droid.startActivity('android.intent.action.VIEW','https://x.com/') 
                                                                                                                            engine.ttsSpeak("opening x") 
                                                                                                                            elif "Facebook" in query:
                                                                                                                                droid.startActivity('android.intent.action.VIEW', 'https://www.facebook.com/') 
                                                                                                                                    engine.ttsSpeak("Opening facebook") 
                                                                                                                                    elif "YouTube" in query:
                                                                                                                                        droid.startActivity('android.intent.action.VIEW', 'https://www.youtube.com/') 
                                                                                                                                            engine.ttsSpeak("Opening youtube")
                                                                                                                                            elif "Justin Bieber" in query:
                                                                                                                                                time.sleep(2) 
                                                                                                                                                    droid.startActivity('android.intent.action.VIEW',list[0]) 
                                                                                                                                                        #droid.startActivity('android.intent.action.VIEW', 'https://youtu.be/euCqAq6BRa4?si=ume5lUgXMobjc86V')
                                                                                                                                                            engine.ttsSpeak("Playing justin bieber")  
                                                                                                                                                            elif "we don't talk anymore" in query:
                                                                                                                                                                time.sleep(2) 
                                                                                                                                                                    droid.startActivity('android.intent.action.VIEW',list[1]) 
                                                                                                                                                                        engine.ttsSpeak("playing")
                                                                                                                                                                        elif "see you again" in query:
                                                                                                                                                                            time.sleep(2) 
                                                                                                                                                                                droid.startActivity('android.intent.action.VIEW',list[2]) 
                                                                                                                                                                                    engine.ttsSpeak("playing")
                                                                                                                                                                                    elif "I wanna be yours" in query:
                                                                                                                                                                                        time.sleep(2) 
                                                                                                                                                                                            droid.startActivity('android.intent.action.VIEW',list[3])     
                                                                                                                                                                                                engine.ttsSpeak("playing") 
                                                                                                                                                                                                elif "Google" in query:
                                                                                                                                                                                                    time.sleep(2) 
                                                                                                                                                                                                        droid.startActivity('android.intent.action.VIEW','https://www.google.com/') 
                                                                                                                                                                                                            engine.ttsSpeak("Opening google") 
                                                                                                                                                                                                            #else:
                                                                                                                                                                                                            #    engine.ttsSpeak("sorry I didn't catch that") 

                                                                                                                                                                                                                     