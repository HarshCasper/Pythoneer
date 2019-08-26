from plyer import notification 
from translate import Translator 
import keyboard
from tkinter import tk
import pyttsx3 
trans = Translator(from_lang="english",to_lang="hindi") 
engine = pyttsx3.init()
engine.setProperty('rate',150)
engine.setProperty('volume',10)
def speak_it_out():                       
    x = Tk().clipboard_get()
    engine.say(x)
    engine.runAndWait()
def translate_it():                            
    x = Tk().clipboard_get()
    print("Copied word : ",x)
    translation = trans.translate(x)
    notification.notify(
        title = x,
        message = translation
        )
while True:
    try:
        if keyboard.is_pressed('*'):  
            speak_it_out()
            continue;
        if keyboard.is_pressed('/'):   
            translate_it()
            continue;
    except:
        notification.notify(
            title = "We encountered some error",
            message = "Kindly give it a re-try"
            )
