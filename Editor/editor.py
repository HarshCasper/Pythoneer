from tkinter import * 
from tkinter import filedialog
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter import colorchooser

###########################################################################################################

root = Tk()
root.geometry('700x500')

###########################################################################################################
class text_editor:
    current_file = 'no_file'
    def tsize(self):
        t = Tk()
        Label(t, text='Select Text Size',font=('arial black',10),width=20,bg='light grey').pack()

        s =Scale(t, from_=0,to=100,orient=HORIZONTAL, length=100,width=10,sliderlength=20)
        
        try:
            s.set(size_set)
        except:
            s.set(15)
            
        s.pack()

        def change_size():
            si = s.get()
            self.text_box.configure(font=('',si))
            global size_set
            size_set = si
            t.destroy()

        Label(t,text='').pack()

        Button(t, text='Apply Changes',font=('arial black',10),command=change_size).pack()
        
###########################################################################################################

    def tcolor(self):

        clr = colorchooser.askcolor(title='Select Color')
        co = clr[1]
    
        self.text_box.configure(fg=co)
        
###########################################################################################################

    def open_func(self):
        returned = filedialog.askopenfile(initialdir='E:\\', title='Select file to open')
        if returned != None:
            self.text_box.delete(1.0, END)
        for line in returned:
            self.text_box.insert(END, line)
            self.current_file = returned.name
            root.title('Text Editor - ' + self.current_file)
        returned.close()

    def new(self):
        msg = messagebox.askyesnocancel('title','All the Progress will be not saved.\n Do you want to save.')
        if msg == True:
            self.save_func()
            self.text_box.delete(1.0, END)
            self.current_file = 'no_file'
            root.title('Text Editor')
            
            

        elif msg == None:
            print('')
        
        else:
            self.text_box.delete(1.0, END)
            self.current_file = 'no_file'
            root.title('Text Editor')

###########################################################################################################

    def saveas_func(self):
        f = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
        if f is None:
            return
        text2save = self.text_box.get(1.0, END)
        self.current_file = f.name
        f.write(text2save)
        f.close

    def save_func(self):
        if self.current_file == 'no_file':
            self.saveas_func()
        
        else:
            f = open(self.current_file, 'w+')
            f.write(self.text_box.get(1.0, END))


    def exit(self):
        msg = messagebox.askyesnocancel('title','All the Progress will be not saved.\n Do you want to save.')
        if msg == True:
            self.save_func()
            root.destroy()

        elif msg == None:
            print('')
        else:
            root.destroy()

    def copy(self):
        self.text_box.clipboard_clear()
        self.text_box.clipboard_append(self.text_box.selection_get())

    def cut(self):
        self.copy()
        self.text_box.delete('sel.first','sel.last')

    def paste(self):
        self.text_box.insert(INSERT, self.text_box.clipboard_get())

    def more(self):
        more = Tk()
        more.configure(bg='powder blue')
        more.geometry('400x200+300+450')


        Label(more, text='Text Editor',bg='powder blue',font=('Arial Black',10,'bold')).pack()

        Label(more, text='By: Harsh Bardhan Mishra',bg='powder blue',font=('Arial Black',10,'bold')).pack()

        Label(more, text='This Text Editor was created as a hobby project just for time-pass.',bg='powder blue',font=('Arial Black',10,'bold')).pack()

        Label(more, text='Contact us at:\nhbmcasper@gmail.com',bg='powder blue',font=('Arial Black',10,'bold')).pack(side=LEFT)
 

        
###########################################################################################################
        
    
    def __init__(self, master):
        master.title('TEXT EDITOR')

        self.scroll = Scrollbar(root)
        self.scroll.pack(side=RIGHT,fill=Y)
        self.text_box = Text(yscrollcommand = self.scroll.set,font=('',15),undo=True)
        self.text_box.pack(fill=BOTH, expand = 1)

        self.scroll.configure(command = self.text_box.yview)

        self.main_menu = Menu()
        master.configure(menu=self.main_menu)

        self.file = Menu(self.main_menu, tearoff = False)
        self.main_menu.add_cascade(label='File', menu=self.file)

        self.edit = Menu(self.main_menu, tearoff = False)
        self.main_menu.add_cascade(label='Edit', menu=self.edit)

        self.format = Menu(self.main_menu, tearoff = False)
        self.main_menu.add_cascade(label='Format',menu=self.format)
        
        self.about = Menu(self.main_menu, tearoff = False)
        self.main_menu.add_cascade(label='About', menu = self.about)
        

        self.file.add_command(label='New file', command=self.new)
        self.file.add_separator()
        self.file.add_command(label='Open', command = self.open_func)
        self.file.add_command(label='Save', command=self.save_func)
        self.file.add_command(label='Save As', command=self.saveas_func)
        self.file.add_separator()
        self.file.add_command(label='Exit', command=self.exit)

        self.edit.add_command(label='Redo',command=self.text_box.edit_redo)
        self.edit.add_command(label='Undo',command=self.text_box.edit_undo)
        self.edit.add_separator()
        self.edit.add_command(label='Copy', command=self.copy)
        self.edit.add_command(label='Cut', command=self.cut)
        self.edit.add_command(label='Paste', command=self.paste)


        self.about.add_command(label='About Us', command = self.more)

        self.format.add_command(label='Change Text Size', command = self.tsize)
        self.format.add_command(label='Change Text Color', command = self.tcolor)
        

###########################################################################################################

te = text_editor(root)

root.mainloop()
