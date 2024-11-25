import webbrowser
import pyttsx3
import speech_recognition as sr
import musics
import requests

recognizer=sr.Recognizer
ttsx=pyttsx3.init()
engine = pyttsx3.init()
newsapi="95aa8da06cc14c2bb250b7f511698ec1"
def speak(text):
    engine.say(text)
    engine.runAndWait()

def processComand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open instagram"  in c.lower():
        webbrowser.open("https://instagram.com")
    elif "type game" in c.lower():
        webbrowser.open("https://www.nytimes.com/games/wordle")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link = musics.music[song]
        webbrowser.open(link)
    
    elif " news " in c.lower(): 
        r=requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")     

    else:



        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            
            # Extracting titles (headlines)
            titles = [article['title'] for article in articles if article.get('title')]
            
            # Output the titles
            for idx, title in enumerate(titles, 1):
                speak(f"{idx}. {title}")

            
         
if __name__ == "__main__":
    print(" Hey, Owais how may I help you." )
    while True:


        try:

            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("listening...")
                audio = r.listen(source,timeout=1,phrase_time_limit=3)
            
            print("Recognizing...")

            command=r.recognize_google(audio)
            print(command)
            if (command.lower()=="charlie"):
                speak("ya")
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Charlie Active...")
                audio = r.listen(source,timeout=2,phrase_time_limit=3)
                command=r.recognize_google(audio)
                
                processComand(command)
            print(command)

        





        except Exception as e:
            print("Error; {0}".format(e))
        







