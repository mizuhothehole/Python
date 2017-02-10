#coding:utf-8
from Tkinter import *

root = Tk()
c0 = Canvas(root, width = 200, height = 150)
c0.pack()
id = c0.create_rectangle(10, 10, 20, 20, fill = 'brown')

def move_rect(event):
    x = event.x
    y = event.y
    c0.coords(id, x - 5, y - 5, x + 5, y + 5)

c0.tag_bind(id, '<Button1-Motion>', move_rect)

root.mainloop()
