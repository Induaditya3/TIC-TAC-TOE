"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # in initial state - X player's turn
    if all(cell == EMPTY for row in board for cell in row):
        return X
    # count no of turns each player had
    # track X's turn
    x = 0
    # track O's turn 
    o = 0
    
    for row in board:
        x += row.count(X)
        o += row.count(O)

    # when o is played less than x - it's o's turn 
    # otherwise x's turn
    return O if o < x else X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # find out all coordinates of all the cells which are empty
    return set((i,j) for i in range(3) for j in range(3) if board[i][j] == EMPTY)


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # raise exception for wrong move
    if not (0 <= action[0] < 3) or not (0 <= action[1] < 3) or board[action[0]][action[1]] != EMPTY:
        raise Exception("invalid move")
    # find out whose turn it is
    turn = player(board)
    # create same board but also assign player move at (i,j) position
    return [[turn if action == (i,j) else board[i][j] for j in range(3)] for i in range(3) ]


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # check horizontally if there is any winner
    for row in board:
        if row[0] == row[1] == row[2] != EMPTY:
            return row[0]
    
    # check if vertically 
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            return board[0][col]
        
    # check main diagonal 
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    
    # check other diagonal
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    
    # No winner
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # check if tie 
    if all(board[i][j] != EMPTY for i in range(3) for j in range(3)):
        return True
    # if there is any winner then game over 
    if winner(board) != None:
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winfor = winner(board)
    if winfor == X:
        return 1
    elif winfor == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def max_value(s,a=None,b=None):
        if terminal(s):
            return utility(s)
        v = float("-inf")
        for action in actions(s):
            vp = min_value(result(s,action),a,b)
            if vp > v:
                v = vp
            if b is not None and vp >= b:
                return v
            if a is not None and vp > a:
                a = vp
        return v
    
    def min_value(s,a=None,b=None):
        if terminal(s):
            return utility(s)
        v = float("inf")
        for action in actions(s):
            vp = max_value(result(s,action),a,b)
            if vp < v:
                v = vp
            if a is not None and vp <= a:
                return v
            if b is not None and vp < b:
                b = vp
        return v
    
    # check if game is over 
    if terminal(board):
        return None
    
    a = float("-inf")
    b = float("inf")
    # which player's turn
    current_player = player(board)

    # when X or maximizing player's turn
    if current_player == X:
        possible_actions = list(actions(board))
        possible_val = list(map(lambda xy: min_value(result(board,xy),a,b),possible_actions))
        return possible_actions[possible_val.index(max(possible_val))]
    else: # O or minimizing player's turn
        possible_actions = list(actions(board))
        possible_val = list(map(lambda xy: max_value(result(board,xy),a,b),possible_actions))
        return possible_actions[possible_val.index(min(possible_val))]