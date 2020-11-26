from valid_sudoku import valid

ROWS =9
COLUMNS =9

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def solve (board):
    empty = find_empty (board)
    if not empty:
        return True
    row, col = empty

    for num in range (1,10):
        if valid (board, num, empty):
            board[row][col] = num

            if solve (board):
                return True

            board[row][col] = 0

    return False

def find_empty (board):
    for row in range (ROWS):
        for col in range (COLUMNS):
            if board[row][col] == 0:
                return (row, col)
    return None

def print_board (board):

    for row in range (ROWS):
        if row % 3 == 0 and row != 0:
            print ("- - - - - - - - - - - - - -")

        for col in range (COLUMNS):
            if col % 3 == 0 and col != 0:
                print (" | ", end = " ")

            if col == 8:
                print (board[row][col])

            else:
                print (str (board[row][col]) + " ", end = "")

print_board (board)
solve (board)
print ("\n--------------------------------\n")
print_board (board)
