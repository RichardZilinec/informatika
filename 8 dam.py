from PIL import Image, ImageDraw
from pathlib import Path
chessboard = []
#
#
#
counter = 0
def create_board ():
    global chessboard
    #chessboard = [row] * 8  # mega pruser takto to nikdy nerob !!!!!
    for i in range (8):
        row = [0] * 8
        chessboard.append(row)
#
#
#
def check_it (x, y):
    for i in range (0, 8):
        if chessboard[y][i] == 1:
            return False
        if chessboard[i][x] == 1:
            return False
    for i in range(0,8):    #y
        for o in range(0,8):    #x
            if i+o == x+y:
                if chessboard[i][o] == 1:
                    return False
            if i-o == y-x:
                if chessboard[i][o] == 1:
                    return False
    return True
#
#
#
def createImage(counter=0):
    size = 80
    boardsize = 8 * size
    img = Image.new("RGB", (boardsize, boardsize), "white")
    draw = ImageDraw.Draw(img)
    for y in range(8):
        for x in range(8):
            color = "black" if (x + y) % 2 == 0 else "white"
            draw.rectangle(
                [x * size, y * size, (x + 1) * size, (y + 1) * size],
                fill=color,
            )
    for y in range(8):
        for x in range(8):
            if chessboard[y][x] == 1:
                draw.ellipse(
                    [
                        x * size + 10,
                        y * size + 10,
                        (x + 1) * size - 10,
                        (y + 1) * size - 10,
                    ],
                    fill="green",
                )
    img.show()
#
#
#
def queens(n):
    global chessboard
    global counter
    if n==8:
        counter+=1
        print (f'Riesenie c. {counter}')
        createImage(counter)
        print("---------------------------------------------")
        print(counter)
    else :
        for i in range(0,8):
            if check_it(i,n):
                chessboard[n][i]=1
                queens(n+1)
                chessboard[n][i]=0

create_board()
#
queens(0)

