# cria uma lista [0, 0, 0, 0, 0, 0, 0, 0]
board = [0] * 8
for i in range(len(board)):
    board[i] = [0] * 8

def printboard():
    letras = ["a", "b", "c", "d", "e", "f", "g", "h"]
    a = 0
    for row in board:
        a += 1
        for col in row:
            print(col, end = " ")
        print (f"| {a}")

    for i in range(len(board)):
        print("-" , end = " ")
    print("")
    for i in range(len(board)):
        print(letras[i] , end = " ")

white_pieces_map =  {
    "wP": [(6,0),(6,1),(6,2),(6,3),(6,4),(6,5),(6,6),(6,7)],
    "wN": [(7,1),(7,6)],
    "wB": [(7,2),(7,5)],
    "wR": [(7,0),(7,7)],
    "wQ": [(7,3)],
    "wK": [(7,4)]
}

black_pieces_map =  {
    "wP": [(1,0),(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7)],
    "wN": [(0,1),(0,6)],
    "wB": [(0,2),(0,5)],
    "wR": [(0,0),(0,7)],
    "wQ": [(0,3)],
    "wK": [(0,4)]
}
