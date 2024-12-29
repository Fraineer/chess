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

printboard()