"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None
counter = 0


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
    Empty = True
    if (terminal(board)):
        return
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if (board[i][j] != EMPTY):
                Empty = False
                break
    if (Empty):
        return X
    countX = 0
    countO = 0
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if (board[i][j] == X):
                countX = countX + 1
            elif (board[i][j] == O):
                countO = countO + 1
    if (countX > countO):
        return O
    else:
        return X

    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    mySet = set()
    for i in range(3):
        for j in range(3):
            if (board[i][j] == EMPTY):
                mySet.add((i, j))
    return mySet
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board2 = copy.deepcopy(board)
    if (terminal(board)):
        return
    i = action[0]
    j = action[1]
    if (i > 2 or i < 0) or (j > 2 or j < 0) or board2[i][j]:
        raise Exception

    if (player(board2) == X):
        board2[i][j] = X
    else:
        board2[i][j] = O
    return board2
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    stringX = ""
    stringO = ""

    # check for rows
    for i in range(3):
        for j in range(3):
            if (board[i][j] == X):
                stringX += X
            elif (board[i][j] == O):
                stringO += O
        if (stringX == "XXX"):
            return X
        elif (stringO == "OOO"):
            return O
        else:
            stringX = ""
            stringO = ""

    stringX = ""
    stringO = ""

    # check for columns
    for j in range(3):
        for i in range(3):
            if (board[i][j] == X):
                stringX += X
            elif (board[i][j] == O):
                stringO += O
        if (stringX == "XXX"):
            return X
        elif (stringO == "OOO"):
            return O
        else:
            stringX = ""
            stringO = ""

    stringX = ""
    stringO = ""

    # check for diagonal
    for i in range(3):
        if (board[i][i] == X):
            stringX += X
        elif (board[i][i] == O):
            stringO += O
    if (stringX == "XXX"):
        return X
    elif (stringO == "OOO"):
        return O

    stringX = ""
    stringO = ""

    # check for anti-diagonal
    for i in range(3):
        if (board[i][2 - i] == X):
            stringX += X
        elif (board[i][2 - i] == O):
            stringO += O
    if (stringX == "XXX"):
        return X
    elif (stringO == "OOO"):
        return O

    return None
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if (winner(board) != None):
        return True
    for i in range(3):
        for j in range(3):
            if (board[i][j] == EMPTY):
                return False
    return True

    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if (terminal(board)):
        win = winner(board)
        if (win == X):
            return 1
        elif (win == O):
            return -1
        else:
            return 0

    raise NotImplementedError


def AlphaBeta(board, depth, alpha, beta, maximazinPlayer):
    if depth == 0 or terminal(board):
        return utility(board)

    if maximazinPlayer:
        bestScore = -math.inf
        for child in actions(board):
            board[child[0]][child[1]] = X
            evaluate = AlphaBeta(board, depth - 1, alpha, beta, False)
            board[child[0]][child[1]] = EMPTY
            bestScore = max(bestScore, evaluate)
            alpha = max(alpha, bestScore)
            if (beta <= alpha):
                break
        return bestScore


    else:
        bestScore = math.inf
        for child in actions(board):
            board[child[0]][child[1]] = O
            evaluate = AlphaBeta(board, depth - 1, alpha, beta, True)
            board[child[0]][child[1]] = EMPTY
            bestScore = min(bestScore, evaluate)
            beta = min(beta, bestScore)
            if (beta <= alpha):
                break
        return bestScore


def minimax(board):
    eligiblePairs = actions(board)
    if (terminal(board)):
        return None
    i = -1
    j = -1
    if player(board) == X:
        BestScore = -math.inf
        for child in eligiblePairs:
            board[child[0]][child[1]] = X
            Score = AlphaBeta(board, len(eligiblePairs), -math.inf, math.inf, False)
            board[child[0]][child[1]] = EMPTY
            if (Score > BestScore):
                BestScore = Score
                i = child[0]
                j = child[1]
    else:
        BestScore = math.inf
        for child in eligiblePairs:
            board[child[0]][child[1]] = O
            Score = AlphaBeta(board, len(eligiblePairs), -math.inf, math.inf, True)
            board[child[0]][child[1]] = EMPTY
            if Score < BestScore:
                BestScore = Score
                i = child[0]
                j = child[1]

    return (i, j)
