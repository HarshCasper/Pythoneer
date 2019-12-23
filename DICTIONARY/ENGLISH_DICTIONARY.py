# Python implementation of a simple English Dictionary 
#-----------------------Importing the Modules-----------------------
import json
import pyttsx3
from difflib import get_close_matches
import tkinter.messagebox

#-----------------------Creating a Tkinter Window-----------------------

window=Tk()
window.title('Word Dictionary')

#-----------------------Loading the JSON File-----------------------

file = open("WORD_DICTIONARY.json","r")
data = json.load(file)

#-----------------------Building the Engine for Speaking-----------------------

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

#-----------------------Function of Speaking-----------------------

def speak(s):
    engine.say(s)
    engine.runAndWait()
def speakWord():
    w=(str(e1.get())).lower()
    speak(w)
    text1.insert(END,"The word pronounced is %s" %w)
    

#-----------------------Finding the Meaning of the Word-----------------------
    
def findMeaning():
    w = (str(e1.get())).lower()
    if w in data:
        for i in range(len(data[w])):
            axe=str(data[w][i])
            text1.insert(END,w+" : "+axe+"\n")
            speak(axe)
    elif len(get_close_matches(w,data.keys())) > 0:
        tkinter.messagebox.showinfo("Error","This word is not present in our lexicon showing results for %s instead"% get_close_matches(w,data.keys())[0])
        for i in range(len(data[get_close_matches(w,data.keys())[0]])):
            text1.insert(END,str(get_close_matches(w,data.keys())[0])+" : "+str(data[get_close_matches(w,data.keys())[0]][i])+"\n")
    else:
        tkinter.messagebox.showinfo("Error","This word is not present in our lexicon\nDouble check it.")

#-----------------------Defining the User-Interface for the Application-----------------------

l1=Label(text='Simple Word Dictionary',bg='green',fg='white',font=('Times',20))
l1.pack(fill=X)
l2=Label(text='Enter the Word',fg='blue',font=('Times',12))
l2.pack()
e1=Entry()
e1.pack()
b1=Button(text='Enter',bg='black',fg='white',command=lambda :findMeaning())
b1.pack()
b2=Button(text='Speak',bg='black',fg='white',command=lambda: speakWord())
b2.pack()
text1=Text(font=('Times',20),height=10)
text1.pack()
l3=Label(text='Created by Harsh Bardhan Mishra',font=('Times',22),fg='brown')
l3.pack()
window.geometry('500x500')
window.mainloop()



#-----------------------Program Ends-----------------------
