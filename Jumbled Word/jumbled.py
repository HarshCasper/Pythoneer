import os
import sys
from collections import defaultdict
from tkinter import *

master = Tk()



def callback2():
            #scrollbar = Scrollbar(master)
            #scrollbar.pack( side = RIGHT, fill=Y )
            #mylist = Listbox(master, yscrollcommand = scrollbar.set )
            pad=3
            master.geometry("{0}x{1}+0+0".format(master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
            text = Text(master)
            text.delete('1.0', END)
            master.title("Jumbled")
            word=ent.get()

         
            text.pack()
            text.delete('1.0', END)
            #print word
            word = word.lower()
            word = sorted(word)

            #sotred function changes variable into a list.
            #below operating changes it  back to string
            word = ''.join(word)

            #removing any unwanted whitespaces
            word = word.strip()


            ## Open the file with read only permit
            f = open('Dictionary.txt', "r")

            ## Read the first line
            line = f.readline()

            #variables for handling display of more than one combiantions
            flag=0
            found=[]


            ## If the file is not empty keep reading line one at a time
            ## till the file is empty
            while line:
                line = f.readline()
                line1 = line
                line = line.lower()
                line = sorted(line)
                line = ''.join(line)
                #print type(line)
                #print type(word1)
                line = line.strip()
                #print line+" : "+word
                if(line == word):
                    if(flag==0):
                        text.insert(END,"Is the word: "+line1+"\n")
                        flag=1
                    elif(flag==1):
                        found.append(line1)

            f.close()
            if(flag==1):
                other = len(found)
                if(other==1):
                    text.insert(INSERT,"1 other possibility found: "+' '.join(found))
                else:
                    text.insert(INSERT,str(other)+" other possibilities found: "+'\n '.join(found))
            #mylist.pack( side = LEFT, fill = BOTH )
            #scrollbar.config( command = mylist.yview )
            text.tag_add("here", "1.0", "1.4")
            text.tag_add("start", "1.8", "1.13")



master.title("MovieSort")
master.geometry("500x500")

lab = Label(master,text=" Welcome to Jumbled", anchor='w',font=("Helvetica",20))
lab.pack()


lab = Label(master,text="\n Unravel the Jumbled word conundrum", anchor='w',font=("Helvetica",15))
lab.pack()


lab = Label(master,text="\n Enter the word", anchor='w',font=("Helvetica",15))
lab.pack()

row = Frame(master)
lab = Label(row,width=26,  text="Enter Movie Name", anchor='w',font=("Helvetica",12))
ent = Entry(row, bd=5, highlightcolor="#00ffff",width=40)
row.pack(side=TOP, fill=X, padx=5, pady=5)
lab.pack(side=LEFT)
ent.pack(side=RIGHT, expand=YES, fill=X,ipady=5)
b = Button(master, text="Get Details",command=callback2,activebackground='red',activeforeground='white',bg='orange',fg='white',relief=RAISED,cursor="hand1")
b.pack(ipady=7)

mainloop()
