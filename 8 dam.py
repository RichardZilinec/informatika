import os
import PIL
from PIL import Image, ImageDraw

OUTPUT_DIR = 'vystup_obrazky'
os.makedirs(OUTPUT_DIR, exist_ok=True)

chessboard = []
counter = 0
size_sq = 50
number = 8
width = size_sq * number
height = size_sq * number
col_b = (0, 0, 0)
col_w = (255, 255, 255)
col_queen = (255, 0, 0)

def draw_and_save_board(board_state, solution_number):
    """Vykreslí šachovnicu aj s dámami pre dané riešenie a uloží obrázok."""
    image = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(image)
    
    for riadok in range(number):
        for stlpec in range(number):
            x1 = size_sq * stlpec
            y1 = size_sq * riadok
            x2 = x1 + size_sq
            y2 = y1 + size_sq
            
            if (riadok + stlpec) % 2 == 1:
                color = col_w
            else:
                color = col_b
            draw.rectangle([x1, y1, x2, y2], fill=color)
            if board_state[riadok][stlpec] == 1:
                padding = 8  
                draw.ellipse([x1 + padding, y1 + padding, x2 - padding, y2 - padding],fill=col_queen)

    filename = f"riesenie_{solution_number}.png"
    filepath = os.path.join(OUTPUT_DIR, filename)
    image.save(filepath)
    print(f"Uložené riešenie {solution_number}: {filepath}")

def create_board():
    global chessboard
    chessboard = []
    for i in range(8):
        row = [0] * 8
        chessboard.append(row)

def check_it(x, y):
    for i in range(0, 8):
        if chessboard[y][i] == 1:
            return False
        if chessboard[i][x] == 1:
            return False
    for i in range(0, 8):      # y
        for o in range(0, 8):  # x
            if i + o == x + y:
                if chessboard[i][o] == 1:
                    return False
            if i - o == y - x:
                if chessboard[i][o] == 1:
                    return False
    return True

def queens(n):
    global chessboard, counter
    if n == 8:
        counter += 1
        print(f"Riešenie č. {counter}:")
        for row in chessboard:
            print(row)
        print('-----------------------------')
        draw_and_save_board(chessboard, counter)
    else:
        for i in range(8):
            if check_it(i, n):
                chessboard[n][i] = 1
                queens(n + 1)
                chessboard[n][i] = 0

create_board()
queens(0)
print(f"\nHotovo! Všetkých {counter} obrázkov bolo uložených do priečinka '{OUTPUT_DIR}'.")
