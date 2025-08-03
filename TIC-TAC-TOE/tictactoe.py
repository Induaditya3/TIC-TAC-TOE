#FUNCTION DEFINITIONS
from tkinter import *
import random 
def check_winner():
    #winning combinations
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True
    #if no winner is found
    elif empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="#FFFD37")
        return "Tie!"
    else:
        return False
    

def next_turn(row,column):
    global player
    
    if buttons[row][column]['text'] == "" and check_winner()is False:
        if player == players[0]:
            # here the input is being taken
            buttons[row][column]['text']= player
            if check_winner() is False:
                player = players[1]
                label.config(text =(players[1]+"-turn"))
            
            elif check_winner() is True:
                label.config(text=(players[0]+" -wins"))

            elif check_winner() == "Tie!":
                label.config(text="Tie!")

        else:
            buttons[row][column]['text']= player   
            
            # here the input is being taken
                
            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0] +"-turn"))
            
            elif check_winner() is True:
                label.config(text=(players[1] +" wins"))

            elif check_winner() == "Tie!":
                label.config(text="Tie!")


def empty_spaces():
    
    spaces = 9
    for row in range (3):
        for column in range (3):
            if buttons[row][column]['text'] !="":
                spaces -= 1
    if spaces == 0 :
        return False
    else:
        return True

def rematch():
    global player
    
    player=random.choice(players)
    
    label.config(text = player+"-turn")
   
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="",bg="#F0F0F0")

#CONSTRUCTION THE game frame (grid)
window = Tk()
window.title("TIC-TAC-TOE")
players=["X","O"]
#selecting a random player's turn
player = random.choice(players)
#creating a double array to create the game area
buttons=[[0,0,0],
         [0,0,0],
         [0,0,0]]
#adding a label to show turn
label= Label(text=player + "-turn",font=('comic sans',30))
label.pack(side="top")
#creating a NEWGAME button
newgame_button = Button(text="NEW GAME",font=('Arial',30), command=rematch)
newgame_button.pack(side="bottom")
# putting all the widgets in the frame
frame= Frame(window)
frame.pack()
#using double forloops to create the 2-d array like buttons where inputs can be taken
for row in range(3):
    for column in range(3):
        buttons[row][column] = Button( frame,text="",font=('consolas',40),width=5, height=2,
                                      command = lambda  row=row , column=column: next_turn(row,column))
        buttons[row][column].grid(row=row,column=column)
window.mainloop()


