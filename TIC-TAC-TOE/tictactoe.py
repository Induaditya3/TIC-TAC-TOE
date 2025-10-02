#FUNCTION DEFINITIONS
from tkinter import Button, Frame, Label, Tk
# checks if game has ended or not 
# returns False if not ended
# returns True if someone won the game
# returns "Tie" if game is tie
# additionally colours the grid green if someone won
# and yellows all the grid if it is a tie

# need to make one variable global- current player
current_player = ""

def check_winner(buttons): # buttons as a parameter intead of global
    #winning combinations
    # check horizontally for consecutive O's or X's
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True
    # check verically
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True
    # check main diagonal
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True
    # check other diagonal
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True
    #if no winner is found
    elif empty_spaces(buttons=buttons) is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="#FFFD37")
        return "Tie!"
    else:
        return False
    

def next_turn(row,column, buttons,players,label): # buttons, player, players, label as parameters
    global current_player
    if buttons[row][column]['text'] == "" and check_winner(buttons) is False:
        if current_player == players[0]: # human turn
            # here the input is being taken
            buttons[row][column]['text']= current_player
            if check_winner(buttons) is False:
                current_player = players[1] # set ai's turn
                label.config(text =(players[1]+"-turn"))
            
            elif check_winner(buttons) is True:
                label.config(text=(players[0]+" -wins"))

            elif check_winner(buttons) == "Tie!":
                label.config(text="Tie!")

        else:
            # ai's turn
            # get optimal move
            # row,column = ai_move(buttons)
            buttons[row][column]['text']= current_player
            
            # here the input is being taken
                
            if check_winner(buttons) is False:
                current_player = players[0]
                label.config(text=(players[0] +"-turn"))
            
            elif check_winner(buttons) is True:
                label.config(text=(players[1] +" wins"))

            elif check_winner(buttons) == "Tie!":
                label.config(text="Tie!")

# checking if there is any spots available for playing game further
# if even single spot is available for playing - it returns True
def empty_spaces(buttons): # defined buttons as a parameter instead of global
    '''ALTERNATIVE IMPLEMENTATION
    
    return any(buttons[i][j]['text'] == "" for i in range(3) for j in range(3))
    '''
    
    spaces = 9
    for row in range (3):
        for column in range (3):
            if buttons[row][column]['text'] !="":
                spaces -= 1
    if spaces == 0 :
        return False
    else:
        return True
# for starting a new game
def rematch(label,buttons): # add the label and buttons as parameter intead of relying on globals
    global current_player
    # Selecting the X as the first player
    current_player = "X"
    
    label.config(text = current_player +"-turn")
   
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="",bg="#F0F0F0")
def main():
    global current_player
    #CONSTRUCTION THE game frame (grid)
    window = Tk()
    window.title("TIC-TAC-TOE")
    players=["X","O"]
    # Selecting the X as the first player and a human player
    current_player = "X"
    #creating a double array to create the game area
    # use list comprehension to initialize 3x3 grid
    # use actual buttons instead of 0 int as dummy values
    buttons= [[Button() for _ in range(3) ] for _ in range(3)]
    # buttons = [
    #     [0,0,0],
    #     [0,0,0],
    #     [0,0,0]
    # ]
    #adding a label to show turn
    label= Label(text= current_player + "-turn",font=('comic sans',30))
    label.pack(side="top")
    #creating a NEWGAME button
    newgame_button = Button(text="NEW GAME",font=('Arial',30), command= lambda : rematch(label=label,buttons=buttons)) # passing rematch as lambda function
    newgame_button.pack(side="bottom")
    # putting all the widgets in the frame
    frame= Frame(window)
    frame.pack()
    #using double forloops to create the 2-d array like buttons where inputs can be taken
    for row in range(3):
        for column in range(3):
            buttons[row][column] = Button( frame,text="",font=('consolas',40),width=5, height=2,
                                        command = lambda row=row, column=column: next_turn(row,column, buttons,players,label))
            buttons[row][column].grid(row=row,column=column)
    window.mainloop()


if __name__ == "__main__":
    main()