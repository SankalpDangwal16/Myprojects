import webbrowser
import speech_recognition as sr
import pyttsx3
import pywhatkit 
import webbrowser
import wikipedia 
import os 
import sys




listner = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()


def talk_command():
    with sr.Microphone() as source:
        print("listening...")
        voice = listner.listen(source)
        command = listner.recognize_google(voice)
        command = command.lower()
        if 'boby' in command:
            command = command.replace('laptop','')
            print(command)
    
    return command

def run_alexa():
    while True:
        command = {}
        try:
            command = talk_command()
        except:
            pass
        if 'play' in command:
            song = command.replace('play', '')
            talk(' playing'+song)
            print('playing song')
            pywhatkit.playonyt(song)

        elif 'wikipedia' in command:
            talk("Searching wikipedia")
            result = wikipedia.summary(command,sentences=2)
            talk("accordng to wikipedia")
            print(result)
            talk(result)
            

        elif 'open youtube' in command:
            webbrowser.open('www.youtube.com')

        elif 'open google' in command:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in command:
            webbrowser.open("stackoverflow.com")  

        elif 'open outlook' in command:
            mailpath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE"
            os.startfile(mailpath)

        elif 'open hvd' in command:
            hpath = "C:\\Program Files (x86)\\VMware\\VMware Horizon View Client\\vmware-view.exe"  
            os.startfile(hpath)
           

        elif 'open teams' in command:
            tpath = "C:\\Users\\sankalp.dangwal\\AppData\\Local\\Microsoft\\Teams\\Teams.exe"
            
            os.startfile(tpath)
        elif 'you can rest' in command:
            talk("Thank you sir!!!!!. See you later")
            sys.exit()

run_alexa()