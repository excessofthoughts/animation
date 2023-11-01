#В обработчике start_draw сохраняем начальные координаты,
# а в обработчике draw рисуем линию от предыдущих координат до новых.


from tkinter import *

def start_draw(event):
    global x, y   # глобальные переменные для сохранения предыдущих координат
    x = event.x
    y = event.y

def draw(event):
    global x, y, canvas_line
    new_x = event.x
    new_y = event.y

    canvas.create_line(x, y, new_x, new_y, width=2)   # рисуем линию на холсте
    x = new_x
    y = new_y

win = Tk()
win.title("Рисование на холсте")

canvas = Canvas(win, width=500, height=500)
canvas.pack()

canvas.bind('<Button-1>', start_draw)   # обработчик нажатия левой кнопки мыши
canvas.bind('<B1-Motion>', draw)        # обработчик перемещения мыши с нажатой левой кнопкой

win.mainloop()

#------------------------------------------------------------------------------



