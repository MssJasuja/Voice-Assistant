import speech_recognition as sr
import webbrowser
import pyttsx3
import music

rcognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://goggle.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open amazon" in c.lower():
        webbrowser.open("https://www.amazon.in")
    elif c.lower().startswith("play"):
        words = c.lower().split(" ")
        if len(words) > 1:
            song = words[1]
            link = music.music.get(song)
        if link:
            webbrowser.open(link)
        else:
            speak(f"Sorry, I couldn't find the song {song}.")
    else:
        speak("Please specify the song name after saying play.")

if __name__== "__main__":
    speak ("initializing clara..")
    while True:
        #Listen for the wake word "Clara"
        # obtain audio from the microphone
        r = sr.Recognizer()
        
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening..")
                audio = r.listen(source, timeout=5, phrase_time_limit=10)
            word = r.recognize_google(audio)
            if (word.lower() == "clara"):
                speak("Yas")
                #listen for command
                with sr.Microphone() as source:
                    print("clara active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)


        except Exception as e:
            print("Error; {0}".format(e))
