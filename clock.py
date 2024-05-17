#importing whole module
from tkinter import *
from tkinter.ttk import*
#importing stftime function to
#retrieve system's time
from time import strftime
#creatig tkinter window
root = Tk()
root.title('clock')
#This function is used to
#display time on the label
def time():
    string = strftime('%H:%M:%S%p')
    lbl.config(text = string)
    lbl.after(1000, time)
    #styling the label widget so that clock
    #will look more attractive
    lbl = Label(root, font = ('calibri', 40,'bold'),
                background = 'black',
                foreground='white')
    #Placing clock at the centre
    # of the tkinter window
    lbl.pack(anchor='center')
    time()
    mainloop()