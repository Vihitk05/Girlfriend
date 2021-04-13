"""

    # Modules
    A module is single python file which has different functions or classes
    into it.

    # Packages
    A package is a collection of modules in a single directory.

"""

import pyttsx3
import speech_recognition as sr
import pywhatkit
import datetime
import wikipedia
import webbrowser
import pyjokes
from AlexaFunctions import read_book
from AlexaFunctions import greet

listen = sr.Recognizer()  # To recognize whatever we say
engine = pyttsx3.init()  # To initialize the audio

# To change the voice from male to female
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


# TAlK function to just print and say whatever we speak
def talk(text):
    print(text)
    engine.say(text)
    engine.runAndWait()


# the main Function
def main():
    greet()
    talk('I am Alexa your girlfriend!')
    talk('What can I do for you? ')
    while True:
        try:
            with sr.Microphone() as source:
                print('Listening...')
                voice = listen.listen(source)
                command = listen.recognize_google(voice)
                command = command.lower()
                print(command)
                if 'alexa' in command:
                    command = command.replace('alexa', '')
                    if 'play' in command:
                        song = command.replace('play', '')
                        talk(f'Playing {song}')
                        pywhatkit.playonyt(song)
                    elif 'time' in command:
                        current_time = datetime.datetime.now().strftime('%I:%M %p')
                        talk(f'Current time is {current_time}')
                    elif 'search' in command:
                        title = command.replace('search', '')
                        content = wikipedia.summary(title, 5)
                        talk(f'According to WIKIPEDIA,{content}')
                    elif 'open google' in command:
                        webbrowser.open('C:\Program Files\Google\Chrome\Application\chrome.exe')
                    elif 'joke' in command:
                        talk(pyjokes.get_joke())
                    elif 'book' in command:
                        read_book()
                    elif 'tata' in command:
                        talk('Bye Vihit! I love you')
                        break
                    elif 'i love you' in command:
                        talk('Aww! I love you too Vihit!')
                    elif 'i am feeling very alone' in command:
                        talk("Don't worry my love, I am always there with you!")
                    elif 'thank you' in command:
                        talk('My pleasure!')
        except Exception:
            pass


main()
