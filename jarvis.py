import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import datetime

engine = pyttsx3.init()
voices = engine.getProperty('voices')               #getting details of current voice
engine.setProperty('voice', voices[0].id)           #0 for male voice
engine.setProperty('rate', 165)                     # setting up new voice rate

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour =  (datetime.datetime.now().hour)   
    if(hour >= 0 and hour<12 ):
        speak("Good Morning..!")
        
    elif hour>=12 and hour<18:
        speak("Good Afternoon..!")

    else:
        speak("Good Eveninng..!")

    speak("HELLO ,I AM SIRI , HOW CAN I HELP YOU..?")    

def takecommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query


if __name__ == "__main__":
    wishme()

    query =  takecommand().lower()
    #logic for executing a task based on query
    if 'wikipedia' in query:
        speak("Searching  in wikipedia:")
        query = query.replace('wikipedia','')
        result = wikipedia.summary(query , sentences=2)
        speak("According to wikipedia ,")
        print(result)
        speak(result)

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")

    elif 'open google' in query:
        webbrowser.open("Google.com")

    elif 'open stack overflow' in query:
        webbrowser.open("stackoverflow.com")        

    elif 'open greeks for greeks' in query:
        webbrowser.open("greeks for greeks.com")     

    elif 'the time' in query:
        strtime = datetime.datetime.now().strftime("%H:%M:%S")    
        speak(strtime)

    elif 'jarvis quit' in query:
        exit(0)