import keyboard
import os
from pynput.keyboard import Key, Controller, Listener
from google_trans_new import google_translator
from pprint import pprint
import time
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter.constants import *
from PIL import ImageTk, Image

window= Tk()
newWindow = tk.Toplevel(window)
controller = Controller()
translator = google_translator()

width = int(window.winfo_screenwidth()/7)+20
height = int(window.winfo_screenheight()/3+40)

toggletrans='Insert'
transoffi='Delete'
exists=[0,True,0,'es', 0]
sentence=[]


def translate():
    exists[1] = False
    tempsentence = ''
    for x in sentence:
        tempsentence+=str(x)
		#print(sentance)
        controller.press(Key.backspace)
        controller.release(Key.backspace)

    tempsentence = tempsentence.replace("'", "")
    translation = translator.translate(tempsentence, lang_tgt=exists[3])   
    sentenceoutput=translation

    controller.type(sentenceoutput)
    sentence.clear()
    tempsentence=''
    exists[2] = 0

    lbl.place(x=2,y=7)
    lbl.config(text = "Toggled Off")

    #os.system('cls')
    for x in range(0,124):
        newWindow.geometry(f"{116}x{46}+{-120+x}+{8}") 
    time.sleep(1)
    for x in range(0,124):
        newWindow.geometry(f"{116}x{46}+{4-x}+{8}") 
def Print():
    print(sentence)
    print(exists[2])
    print(exists[1])

def on_press(key):
    #print(f"Key.{transoffi.lower()} ", str(key))
    global exists
    global toggletrans
    global transoffi

    if key==Key.f4:
        if exists[0] == 1:
            window.deiconify()
            for x in range(0,300):
                window.geometry(f"{239}x{328}+{window.winfo_screenwidth()+46-x}+{10}")
            exists[0] = 0
        else:
            for x in range(0,300):
                window.geometry(f"{239}x{328}+{window.winfo_screenwidth()-254+x}+{10}")
            window.withdraw()
            exists[0] = 1
    elif str(key) == f"Key.{transoffi.lower()}" and exists[1] == True: #Translate Key
        translate()
    elif str(key) == f"Key.{toggletrans.lower()}": #Toggle Translate function
        if exists[1] == False: 
            lbl.place(x=4,y=7)
            lbl.config(text = "Toggled On")
            for x in range(0,124):
                newWindow.geometry(f"{116}x{46}+{-120+x}+{8}") 
            time.sleep(1)
            for x in range(0,124):
                newWindow.geometry(f"{116}x{46}+{4-x}+{8}") 
            exists[1] = True
        else:
            lbl.place(x=2,y=7)
            lbl.config(text = "Toggled Off")
            for x in range(0,124):
                newWindow.geometry(f"{116}x{46}+{-120+x}+{8}") 
            time.sleep(1)
            for x in range(0,124):
                newWindow.geometry(f"{116}x{46}+{4-x}+{8}") 
            exists[1] = False
        
    elif exists[1] == True:
        if key == Key.space:
            sentence.insert(exists[2]+exists[4], " ")
            exists[2] += 1
            Print()
        elif key==Key.backspace:
            if exists[2]-1 >=0:
                del sentence[(exists[2]+exists[4])-1]
                exists[2] -= 1
                Print()
        elif key==Key.home or key==Key.enter or key==Key.end or key==Key.print_screen or key==Key.esc or key==Key.scroll_lock or key==Key.insert or key==Key.delete or key==Key.pause or key==Key.caps_lock or key==Key.shift or key==Key.ctrl_l or key==Key.alt_l or key==Key.tab or key==Key.up or key==Key.down or key==Key.page_up or key==Key.page_down or key==Key.num_lock or key==Key.shift_r or key==Key.ctrl_r or key==Key.alt_gr or key==Key.cmd or key==Key.cmd_r or key==Key.menu or key==Key.f1 or key==Key.f2 or key==Key.f3 or key==Key.f4 or key==Key.f5 or key==Key.f6 or key==Key.f7 or key==Key.f8 or key==Key.f9 or key==Key.f10 or key==Key.f11 or key==Key.f12:
            non=0
        elif key==Key.left:
            exists[4]-=1
        elif key==Key.right:
            exists[4]+=1
        else:
            sentence.insert(exists[2]+exists[4], key)
            exists[2] += 1
            Print()

def on_release(key):
    non=0




#----------------------------------------------------------#
# GUI #
#----------------------------------------------------------#




def exitk():
    for i in range(0,300):
        window.geometry(f"{239}x{328}+{window.winfo_screenwidth()-254+i}+{10}")
        window.update()
    window.destroy()
    listener.stop()

def samekeybind():
    if not toggletrans == transoffi:
        normalmenu()
    else:
        keybind()
        tk.Label(window, text= "Cannot have identical bindings",bg='#1B1B1B', fg='#FF0000',font=('rockwell bold', 9)).place(x=25, y=75)


def deftogg(var1, var2):
    global transoffi
    global toggletrans
    toggletrans=var1
    transoffi=var2

def keybind():
    tk.Label(window, text= ("_"*100+"\n")*100,bg='#72bcd4', fg='#72bcd4',font=('calibri', 15)).place(x=0, y=0)
    tk.Label(window, text= ("_"*23+"\n")*100,bg='#1B1B1B', fg='#1B1B1B',font=('calibri', 15)).place(x=1, y=1)
    

    border_color1 = tk.Frame(window, background="#72bcd4")
    exit = tk.Label(border_color1, text="Exit", fg='#72bcd4', bg='#1B1B1B',bd=0,font=('rockwell bold', 15))
    exit.pack(ipadx=101,ipady=2, pady=2,side=TOP)
    border_color1.pack(ipadx=1, ipady=0.35, pady=0, side=TOP)
    exit.bind("<Button-1>", lambda e:exitk())


    variable = tk.StringVar(window)
    variable.set(toggletrans) # default value

    variable2 = tk.StringVar(window)
    variable2.set(transoffi) # default value

    w = tk.OptionMenu(window, variable,'F1','F2','F3','F4','F5','F6','F7','F8','F9','F10','F11','F12', 'Delete', 'Insert','End','Home','Page Up','Page Down','Scroll Lock','Pause','Break')
    w.place(x=15,y=106)
    tk.Label(window, text= "Start/Stop", fg='#ffffff', bg='#1B1B1B',font=('rockwell bold', 15)).place(x=120, y=106)

    w2 = tk.OptionMenu(window, variable2,'F1','F2','F3','F4','F5','F6','F7','F8','F9','F10','F11','F12', 'Delete', 'Insert','End','Home','Page Up','Page Down','Scroll Lock','Pause','Break')
    w2.place(x=15,y=142)
    tk.Label(window, text= "Translate", fg='#ffffff', bg='#1B1B1B',font=('rockwell bold', 15)).place(x=120, y=142)
    
    
    border_color = tk.Frame(window, background="#72bcd4")
    button1 = tk.Label(border_color, text="Save & Exit", fg='#72bcd4', bg='#1B1B1B',bd=0,font=('rockwell bold', 15))
    button1.pack(ipadx=66,ipady=2, pady=2,side=BOTTOM)
    border_color.pack(ipadx=1, ipady=0.35, pady=0, side=BOTTOM)
    def destroy():
        button1.after(0 , lambda: button1.destroy())
        border_color.after(0 , lambda: border_color.destroy())
        exit.after(0 , lambda: exit.destroy())
        border_color1.after(0 , lambda: border_color1.destroy())
    button1.bind("<Button-1>", lambda e:[deftogg(variable.get(), variable2.get()), samekeybind(), destroy()])

def normalmenu():
    spacrup=0
    spacrdwn=0
    spacrup2=0
    spacrdwn2=0
    if toggletrans=='F1' or toggletrans=='F2' or toggletrans=='F3'or toggletrans=='F4'or toggletrans=='F5'or toggletrans=='F6'or toggletrans=='F7'or toggletrans=='F8'or toggletrans=='F9'or toggletrans=='F10'or toggletrans=='F11'or toggletrans=='F12':
        spacr=17
    elif toggletrans=='Insert':
        spacr=2
    elif toggletrans=="Page Up":
        spacr=-8
        spacrup=7
    elif toggletrans=='Page Down':
        spacr=-13
        spacrdwn=25
    elif toggletrans=='Scroll Lock':
        spacr=-13
        spacrdwn=25
    else:
        spacr=0
        spacrup=0
        spacrdwn=0
    
    if transoffi=='F1' or transoffi=='F2' or transoffi=='F3'or transoffi=='F4'or transoffi=='F5'or transoffi=='F6'or transoffi=='F7'or transoffi=='F8'or transoffi=='F9'or transoffi=='F10'or transoffi=='F11'or transoffi=='F12':
        spacr2=17
    elif transoffi=='Insert':
        spacr2=2
    elif transoffi=="Page Up":
        spacr2=-8
        spacrup2=7
    elif transoffi=='Page Down':
        spacr2=-13
        spacrdwn2=25
    elif transoffi=='Scroll Lock':
        spacr2=-13
        spacrdwn2=25
    else:
        spacr2=0
        spacrup2=0
        spacrdwn2=0

    tk.Label(window, text= ("_"*100+"\n")*100,bg='#72bcd4', fg='#72bcd4',font=('rockwell bold', 15)).place(x=0, y=0)
    tk.Label(window, text= ("_"*21+"\n")*100,bg='#1B1B1B', fg='#1B1B1B',font=('rockwell bold', 15)).place(x=1, y=1)

    tk.Label(window, text= toggletrans, fg='#72bcd4', bg='#1B1B1B',font=('rockwell bold', 15)).place(x=26+spacr, y=85)
    tk.Label(window, text= "Start/Stop", fg='#ffffff', bg='#1B1B1B',font=('rockwell bold', 15)).place(x=108+spacrup+spacrdwn, y=85)

    tk.Label(window, text= transoffi, fg='#72bcd4', bg='#1B1B1B',font=('rockwell bold', 15)).place(x=28+spacr2, y=122)
    tk.Label(window, text= "Translate", fg='#ffffff', bg='#1B1B1B',font=('rockwell bold', 15)).place(x=110+(spacrup2+spacrdwn2), y=122)

    tk.Label(window, text= "F4", fg='#72bcd4', bg='#1B1B1B',font=('rockwell bold', 15)).place(x=39, y=157.5)
    tk.Label(window, text= "Hide Menu", fg='#ffffff', bg='#1B1B1B',font=('rockwell bold', 15)).place(x=108, y=157.5)


    #test --- light = tk.Label(window, text=" ", bg="#7FFF00",font=('rockwell bold', 15)).place(x=0,y=100)


    border_color1 = tk.Frame(window, background="#72bcd4")
    exit = tk.Label(border_color1, text="Exit", fg='#72bcd4', bg='#1B1B1B',bd=0,font=('rockwell bold', 15))
    exit.pack(ipadx=101,ipady=2, pady=2,side=TOP)
    border_color1.pack(ipadx=1, ipady=0.35, pady=0, side=TOP)
    exit.bind("<Button-1>", lambda e:exitk())


    border_color = tk.Frame(window, background="#72bcd4")
    button1 = tk.Label(border_color, text="Keybinds", fg='#72bcd4', bg='#1B1B1B',bd=0,font=('rockwell bold', 15))
    button1.pack(ipadx=77,ipady=2, pady=2,side=BOTTOM)
    border_color.pack(ipadx=1, ipady=0.35, pady=0, side=BOTTOM)
    def destroy():
        button1.after(0 , lambda: button1.destroy())
        border_color.after(0 , lambda: border_color.destroy())
        exit.after(0 , lambda: exit.destroy())
        border_color1.after(0 , lambda: border_color1.destroy())
    button1.bind("<Button-1>", lambda e:[deftogg(keybind(), destroy())])



print(window.winfo_screenwidth(), width, window.winfo_screenheight(), height)

normalmenu()

window.overrideredirect(True)
window.resizable(False, False)
window.geometry(f"{239}x{328}+{window.winfo_screenwidth()-254}+{10}")
window.attributes('-topmost',True)
window.attributes('-alpha',0.99999)

newWindow.overrideredirect(True)
newWindow.resizable(False, False)
newWindow.geometry(f"{116}x{46}+{-120}+{8}") 
newWindow.attributes('-topmost',True)
newWindow.attributes('-alpha',0.99999)
tk.Label(newWindow, text= ("_"*100+"\n")*100,bg='#72bcd4', fg='#72bcd4',font=('rockwell bold', 15)).place(x=0, y=0)
tk.Label(newWindow, text= ("_"*12+"\n"),bg='#1B1B1B', fg='#1B1B1B',font=('rockwell bold', 13)).place(x=1, y=1)
lbl = tk.Label(newWindow, text = "",bg='#1B1B1B', fg='#72bcd4',font=('rockwell bold', 15))

with Listener(on_press=on_press, on_release=on_release) as listener:

    window.mainloop()
    #listener.stop()
    listener.join()