from tkinter import *
#####Initialising a window
window = Tk() # initiates the window
window.geometry("420x420")
window.title("hello GUI")
icon= PhotoImage(file='C:\\Users\\Dell\\Desktop\\python\\GUI\\logo.png')
window.iconphoto(True,icon)
window.config(background="#631956")
########### labels
lbl = Label(window,
            text ="WELCOME",
            font=('Times new roman',20,'italic','bold'),
            fg="#3A688D",
            bg="#964C40",
            relief=RAISED,
            bd=5,
            padx=10,
            pady=10,
            )
###########BUTTONS
count = 0
def click():
    global count
    print("you clicked it")
    count+=1
    print(count)
"""buttonphoto = PhotoImage(file = 'C:\\Users\\Dell\\Downloads\\Copilot_20250716_221225.png')
button = Button(window,
                text="click me!",
                font =('Arial',20,'bold'),
                command=click,
                fg="#1AC28A",
                bg="#000000",
                image=buttonphoto,
                compound='top'
                )"""
frame= Frame(window,bg="#7D881F",bd=5,relief=SUNKEN)
frame.pack()
Button(frame,text="W",font=('arial',20),width=3).pack(side=TOP)
Button(frame,text="A",font=('arial',20),width=3).pack(side=LEFT)
Button(frame,text="S",font=('arial',20),width=3).pack(side=LEFT)
Button(frame,text="D",font=('arial',20),width=3).pack(side=LEFT)

# FRAME = rectangular container to group and hold widgets
            
lbl.pack()
#button.place(x=540,y=200)
window.mainloop() # places a window on computer screen



