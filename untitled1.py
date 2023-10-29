from tkinter import *
import speech_recognition as sr
import webbrowser
import pyttsx3
from datetime import datetime
import subprocess
import os 

root = Tk()
root.geometry("500x500")
root.configure(background="Light Blue")

label = Label(root, text="Welcome to your personal desktop assistant!", bg="Light Blue", font=("Bahnschrift Light", 15, "bold"))
label.place(relx=0.5, rely=0.1, anchor=CENTER)

text_to_speech = pyttsx3.init()

def speak(audio):
    
    text_to_speech.say(audio)
    text_to_speech.runAndWait()
def r_audio():
    speech_recognisor = sr.Recognizer()
    speak(" heyyyyy How can I help you..?")
    with sr.Microphone() as source:
        audio = speech_recognisor.listen(source)
        voice_data=''
        try:
            voice_data = speech_recognisor.recognize_google(audio, language='en-in')
        except sr.UnknownValueError:
            print('Please repeat I did not get that')
            speak('Please repeat i did not get that')
        respond(voice_data)
def respond(voice_data):
    print(voice_data)
    if "name" in voice_data:
        speak("My name is Blitz")
        print("My name is Blitz")
    if "time" in voice_data:
        speak("Current Time is:")
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        speak(current_time)
        print(current_time)
        
        
    if "classical" in voice_data:
        speak("Opening Song")
        print("Opening Song")
        os.startfile('C:/Users/bhavi/Downloads/New folder (2)/song2.mp3.mp3')
        
        
    if "sound machine" in voice_data:
        speak("Opening Song")
        print("Opening Song")
        os.startfile('C:/Users/bhavi/Downloads/New folder (2)/song.mp3.mp3')
        
        
    if "heart" in voice_data:
        speak("Opening the Song")
        print("Opening the Song")
        os.startfile('C:/Users/bhavi/Downloads/New folder (2)/song1.mp3.mp3')

        
btn = Button(root, text="Start", bg="red3", fg="white", padx=10, pady=1, font=("Arial", 11, "bold"), relief=FLAT, command=r_audio)
btn.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
