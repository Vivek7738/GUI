#Python Use
import tkinter as tk

win=tk.Tk()
win.config(bg="light blue")
     #title
win.title("TkinterLibrary.com")
win.maxsize(450,300)
    #iconimage
photo = tk.PhotoImage(file = 'AI.png')
win.iconphoto(False, photo)
def close():
    win.destroy()
def sel():
    if (e1.get() == "print"):
        T.config(text='he print() function prints the specified message to the screen, or other standard output device.')
    elif (e1.get() == "int"):
        T.config(text='The int() function converts the specified value into an integer number.')
    elif (e1.get() == "tkinter"):
        T.config(text='It is a standard Python interface to the Tk GUI toolkit shipped with Python.')
    elif (e1.get() == "Label"):
        T.config(text='The Label is used to specify the container box where we can place the text or images.')
    elif (e1.get() == "Entry"):
        T.config(text='The Entry widget is used to provde the single line text-box to the user to accept a value from the user.')
    elif (e1.get() == "Messagebox"):
        T.config(text='The tkMessageBox module is used to display message boxes in your application,that you can use to display an appropriate message.')
    elif (e1.get() == "Spinbox"):
        T.config(text='It provides the range of values to the user, out of which, the user can select the one value.')
    elif (e1.get() == "Combobox"):
        T.config(text='It is used for to select the values in the drop-down list column.')
    elif (e1.get() == "Listbox"):
        T.config(text='The Listbox widget is used to display the list items to the user.')
    elif (e1.get() == "Radiobutton"):
        T.config(text='This widget implements a multiple-choice button.')
    elif (e1.get() == "Checkbutton"):
        T.config(text='The Checkbutton widget is used to display a number of options to a user as toggle buttons.')
    elif (e1.get() == "Message"):
        T.config(text='The Message widget is used to show the message to the user regarding the behaviour of the python application.')
    elif (e1.get() == "Frame"):
        T.config(text='Frame widget is used to organize the group of widgets.')
    elif (e1.get() == "get"):
        T.config(text='To return the data entered in an Entry widget.')
    elif (e1.get() == "config"):
        T.config(text='Config() in Python Tkinter are used to change property of the widget.')
    elif (e1.get() == "insert"):
        T.config(text='To insert text in the widget, you need to use insert().')
    elif (e1.get() == "Button"):
        T.config(text='The Button widget is used to add buttons in a Python application.')
    elif (e1.get() == "minsize"):
        T.config(text='minsize() method is used to set the minimum size of the Tkinter window.')
    elif (e1.get() == "maxsize"):
        T.config(text='This method is used to set the maximum size of the Tkinter window.')
    elif (e1.get() == "iconphoto"):
        T.config(text='iconphoto() method is used to set the titlebar icon of any tkinter/toplevel window.')
    elif (e1.get() == "title"):
        T.config(text='sets the title of that window.')
    elif (e1.get() == "grid"):
        T.config(text='This geometry manager organizes widgets in a table-like structure in the parent widget.')
    elif (e1.get() == "place"):
        T.config(text='This geometry manager organizes widgets by placing them in a specific position in the parent widget.')
    elif (e1.get() == "pack"):
        T.config(text='This geometry manager organizes widgets in blocks before placing them in the parent widget.')
    elif (e1.get() == "resizeable"):
        T.config(text='used to allow Tkinter root window to change its size according to the users need as well we can prohibit resizing of the Tkinter window.')
    elif (e1.get() == "mainloop"):
        T.config(text='window.mainloop() tells Python to run the Tkinter event loop.')
    elif (e1.get() == "def"):
        T.config(text='Python def keyword is used to define a function, it is placed before a function name that is provided by the user to create a user-defined function.')
    elif (e1.get() == ""):
        T.config(text='')
    elif (e1.get() == ""):
        T.config(text='')
    else:
        T.config(text='OOPs!! Not studed yet')
  #bgimage
label1 = tk.Label(win)
label1.place(x = 0, y = 0)
#searching
l1 = tk.Label( win,text="Search",font=('Calibri',17,'bold'),bg="light blue")
l1.grid(row=2,column=1)
e1=tk.Entry(win,bd=10)
e1.grid(row=2,column=2)
#Button
ph = tk.PhotoImage(file = 'py1.png')
b1=tk.Button(win,text="Search",image=ph,height=75,width=75,activebackground="red",cursor="cross",command=sel)
b1.grid(row=4,column=2)
b2=tk.Button(win,text="Quit",bg="red",height=5,width=5,command=close)
b2.grid(row=4,column=1)
#message
m1=tk.Message(win,text="Hello Developer's have any query?",font="5",bg="light blue",width=500)
m1.grid(row=1,column=2)
#textbox AREA
T = tk.Message(win,text="hello",bg="pink")
T.grid(row=7,column=2)

win.mainloop()
