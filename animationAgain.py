import tkinter as tk
import random


class Bubble:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.item = canvas.create_oval(x, y, x+20, y+20, outline='gray')
        self.speed = random.randint(1, 3)
    def update(self):
        self.canvas.move(self.item, 0, -self.speed)


class MainClass:
    def start(self, event):
        if not self.is_animating:
            self.is_animating = True
            self.animate()
    def end(self, event):
        self.is_animating = False
    def animate(self):
        if not self.is_animating:
            return
        for everything in self.bubbles:
            everything.update()
        self.win.after(30, self.animate)
    def __init__(self, win):
        self.win = win
        self.canvas = tk.Canvas(self.win, width=600, height=600, bg='white')
        self.canvas.pack()
        self.bubbles = []

        for _ in range(20):
            x = random.randint(0, 580)
            y = random.randint(0, 580)
            everything = Bubble(self.canvas, x, y)
            self.bubbles.append(everything)
            self.is_animating = False
            self.canvas.bind('<Button-1>', self.start)
            self.canvas.bind('<Button-3>', self.end)


        #self.animate()
    '''def animate(self):
        for everything in self.bubbles:
            everything.update()
        self.win.after(30, self.animate)'''

if __name__ == '__main__':
    win = tk.Tk()
    win.title('animation')
    MainClass(win)
    win.mainloop()