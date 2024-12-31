import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests

recognizer=sr.Recognizer()
engine=pyttsx3.init()
newsapi="6a02a10d15c542c1231d"


def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
    client=OpenAI(api_keys="sk-proj-ZtHKoXHfgcyuRjjxR62S38htLyEyFU4_bDuGsptpCiKedRDWOK89GSqbD2gcrlKCtdiQyU4slVviqj7EkCv1mEh1U0fNkv3_doIYXM03Sd3RMi8lBpEXxqRAvTKM-b1bX-fSUWqRBsA",)
    completion=client.chat.completions.create(model="gpt-3.5-turbo",messages=[{"role":"system","content":"You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},{"role":"user","content":command}])

    return completion.choices[0].message.content
    
def processCommand(c):
    if "open google"in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube"in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open facebook"in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open linkedin"in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=musiclibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r=requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=6a02a10d15c542cf8c61da297f2={newsapi}")
        if r.status_code==200:
            #Parse the JSON response
            data=r.json()

            #extract the articles
            articles=data.get('articles',{})

            #print the headlines
            for article in articles:
                speak(article['title'])

    else:
        #let OpenAi handel the request
        output=aiProcess(c)
        speak(output)







if __name__=="__main__":
    speak("Initialising Jarvis...")
    while True:
        #Listen for the wake word "Jarvis"
        #obtain audio from the microphone
        r=sr.Recognizer()
        print("recognising...")
            #recognize speech using Sphinx
        try:
            with sr.Microphone() as source:
                audio=r.listen(source,timeout=2,phrase_time_limit=1)
                print("Listening...")
                
            
 
            word=r.recognize_google(audio)
            if(word.lower()=="Jarvis"):
                speak ("Ya")
                  #listen for command
                with sr.Microphone() as source:
                    print("Jarvis active..")
                    audio=r.listen(source)
                    command=r.recognize_google(audio)

                    processCommand(command)


                
        except Exception as e:
            print("error;{0}".format(e))