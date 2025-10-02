from tkinter import Button
"""This module implements Tic-Tac-Toe playing AI which has leverages the minimax algorithm """
# convert the 2d list containing buttons into the 2d list of char
# reason being that we are going to use recursion and list of button is memory consuming
def convert_state(grid: list[list[Button]])-> list[list[str]]:
    """Returns a 3x3 list of char - 
     '' means empty
      'O' means marked by ai 
       'X' means marked by human"""
    return [[grid[row][column]["text"] for column in range(3)] for row in range(3)]

def players(state:list[list[str]]) -> str:
    """Returns the whose turn it is
     'X' means human turn/ maximizing's turn
      'O' maeans ai turn/ minimizing's turn
       '' means game over"""
    # if all cells are empty
    if all(state[i][j] == "" for i in range(3) for j in range(3)):
        # X's turn
        return "X"
    # if any cell is non-empty then the player having least no of marked cells gets the turn otherwise x's gets turn
    if any(state[i][j] == "" for i in range(3) for j in range(3)):
        # tracks how many x's and o's are played
        x = 0
        o = 0
        for inner_list in state:
            x+= inner_list.count("X")
            o+= inner_list.count("O")
        return "X" if x <= o else "O"
    # game is over
    return ""

def actions(state: list[list[str]]) -> list[tuple[int,int]]:
    """Returns the coordinates of unoccupied cells
    ie where the cell is available for marking with o or x"""
    return [(i,j) for i in range(3) for j in range(3) if state[i][j] == ""]

def result(state: list[list[str]],action: tuple[tuple[int,int],str]) -> list[list[str]]:
    """Returns new 2d list representing the state after move at given cell is made by x or o
     state -> current state 
      action -> a tuple contains the coordinate (x,y) and string 'X' or "O" """
    return [[ action[1] if (i,j) == action[0] else state[i][j] for j in range(3)] for i in range(3)]

def terminal(state: list[list[str]]) -> bool:
    """ Returns true if game has ended or false otherwise
    game has ended when someone has won or its a tie"""
    # check horizontally for consecutive O's or X's
    for row in range(3):
        if state[row][0] == state[row][1]  == state[row][2]  != "":
            return True
    # check verically
    for column in range(3):
        if state[0][column]  == state[1][column]  == state[2][column]  != "":
            return True
    # check main diagonal
    if state[0][0]  == state[1][1]  == state[2][2]  != "":
        return True
    # check other diagonal
    elif state[0][2]  == state[1][1]  == state[2][0]  != "":
        return True
    #if no winner is found
    elif all(state[i][j] != "" for i in range(3) for j in range(3)):
        return True
    return False

def utility(state: list[list[str]]) -> int:
    """Returns 
    0 if the game was tie
    1 if X won
    -1 if O won"""
    # check horizontally for consecutive O's or X's
    for row in range(3):
        if state[row][0] == state[row][1]  == state[row][2]  != "":
            return 1 if state[row][0] == "X" else -1
    # check verically
    for column in range(3):
        if state[0][column]  == state[1][column]  == state[2][column]  != "":
            return 1 if state[0][column] == "X" else -1
    # check main diagonal
    if state[0][0]  == state[1][1]  == state[2][2]  != "":
        return 1 if state[1][1] == "X" else -1
    # check other diagonal
    elif state[0][2]  == state[1][1]  == state[2][0]  != "":
        return 1 if state[1][1] == "X" else -1
    #if no winner is found it must be tie
    return 0

# this acts layer between real game
# this function will used in tictactoe.py
def ai_move(grid: list[list[Button]]) -> tuple[int,int]:
    current_state = convert_state(grid)

    def max_value(state: list[list[str]]) -> float:
        v: float = float("-inf")
        if terminal(state):
            return utility(state)
        for action in actions(state):
            v = max(v,min_value(result(state,(action,"X"))))
        return v
    
    def min_value(state: list[list[str]]) -> float:
        v: float = float("inf")
        if terminal(state):
            return utility(state)
        for action in actions(state):
            v = min(v,max_value(result(state,(action,"O"))))
        return v
    # find out best move for minimizing player or 'O'
    possible_actions:list[tuple[int,int]] = actions(current_state)
    possible_val: list[float] = list(map(lambda xy: max_value(result(current_state,(xy,"O"))),possible_actions))
    # The minimizing player picks action a in actions(s) that produces the lowest value of max_value(result(s, a))
    return possible_actions[possible_val.index(min(possible_val))]