import tkinter as tk
#
#
#
win = tk.Tk()
canvas = tk.Canvas(width = 1000, height= 1000, background='green')
canvas.pack()
def troj (a,x,y):
    if a > 10:
        canvas.create_line(x,y, x+a, y, fill='yellow')
        canvas.create_line(x,y, x+a//2, y-(a**2 - (a**2) // 4)**0.5, fill='yellow')
        canvas.create_line(x+a, y, x+a//2, y-(a**2 - (a**2) // 4)**0.5, fill='yellow')
        troj(a//2, x, y)
        troj(a//2, x+a//2, y)
        troj(a//2, x+a//4, y-((a//2)**2 - ((a//2)**2) // 4)**0.5)
#
#
#
troj(1000,0,900)
win.mainloop()