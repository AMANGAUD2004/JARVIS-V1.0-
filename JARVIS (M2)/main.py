import pyttsx3
import speech_recognition as sr
import datetime
import os
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
        return query.lower()
    except Exception as e:
        print(e)
        speak("Sorry, I can't understand")
        return ""

def wish():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        greeting = "Good Morning BOSS!"
    elif 12 <= hour < 17:
        greeting = "Good Afternoon BOSS!"
    elif 17 <= hour < 21:
        greeting = "Good Evening BOSS!"
    else:
        greeting = "Good Night BOSS!"
    
    speak(greeting)

def execute_command(query):
    if 'time' in query:
        str_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Sir, the time is {str_time}")
        speak(f"Sir, the time is {str_time}")
    
    elif 'open chrome' in query:
        speak("Opening Chrome, Sir")
        chrome_path = r"C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome.lnk"
        os.startfile(chrome_path)
    
    elif 'search' in query:
        search_term = query.replace("search", "").strip()
        if search_term:
            speak(f"Searching {search_term} on Google")
            webbrowser.open(f"https://www.google.com/search?q={search_term}")
        else:
            speak("What do you want to search, Sir?")
    
    elif 'stop' in query:
        speak("Okay Sir, shutting down. Have a great day!")
        print("Exiting...")
        return True

    else:
        speak("I didn't understand the command, Sir")

    return False

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    wish()
    
    while True:
        query = listen()
        if query:
            if execute_command(query):
                break
