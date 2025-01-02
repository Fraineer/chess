# cria uma lista [0, 0, 0, 0, 0, 0, 0, 0]
board = [0] * 8
for i in range(len(board)):
    board[i] = [0] * 8

def printboard():
    for row in board:
        for col in row:
            print(col, end = " ")
        print ("")

    for i in range(len(board)):
        print("" , end = " ")
    print("")

white_pieces_map =  {
    "wP": [(6,0),(6,1),(6,2),(6,3),(6,4),(6,5),(6,6),(6,7)],
    "wN": [(7,1),(7,6)],
    "wB": [(7,2),(7,5)],
    "wR": [(7,0),(7,7)],
    "wQ": [(7,3)],
    "wK": [(7,4)]
}

black_pieces_map =  {
    "bP": [(1,0),(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7)],
    "bN": [(0,1),(0,6)],
    "bB": [(0,2),(0,5)],
    "bR": [(0,0),(0,7)],
    "bQ": [(0,3)],
    "bK": [(0,4)]
}

def put_pieces(board):
    #white pieces
    for piece,squares in white_pieces_map.items():
        for square in squares:
            x,y = square[0] , square[1]
            board[x][y] = piece


    for piece, squares in black_pieces_map.items():
        for square in squares:
            x, y = square[0], square[1]
            board[x][y] = piece

put_pieces(board)

curr_turn = 1
while(True):
    printboard()
    print(" ")
    curr_player = " "
    if curr_turn % 2 == 1:
        curr_player = "white"
    if curr_turn % 2 == 0:
        curr_player = "black"
    curr_turn += 1
    print(curr_player)
    break

if __name__ == "__main__":
    main()