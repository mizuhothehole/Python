#coding:utf-8
import time
from Tkinter import *  

def callback(event):
	print "clicked at", event.x, event.y

def handler(event, a, b, c, ob): 
    '''''事件处理函数''' 
    print "clicked at", event.x, event.y
    print ("creatBox")
    points = [event.x - 2.5,event.y - 5,event.x + 2.5,event.y - 5,event.x - 2.5,event.y + 5,event.x + 2.5,event.y + 5]
    color= "#476042"
    ob.create_polygon(points, outline=color, 
            fill='yellow', width=3)

def creatBox(event, ob): 
    '''''事件处理函数''' 
    print "clicked at", event.x, event.y
    print ("creatBox")
    points = [event.x - 2.5,event.y - 2.5,event.x + 2.5,event.y - 2.5,event.x - 2.5,event.y + 2.5,event.x + 2.5,event.y + 2.5]
    ob.update()
    color= "#476042"
    ob.create_polygon(points, outline=color, 
            fill='yellow', width=3)
    
# it seems that this function does not work very well without any reason
def dance(event, ob): 
    '''''事件处理函数'''
    xPosition = 0
    yPosition = 0
    #img = PhotoImage(file="/home/shin/デスクトップ/rocks.ppm")
    #canvas.create_image(20,20, anchor=NW, image=img)
    filename = PhotoImage(file = "C:\Users\user\Desktop\lll.gif")
    #while(True):
    time.sleep(3)
    image = ob.create_image(xPosition, yPosition, anchor=NW, image=filename)
            #xPosition += 10
            #yPosition += 10

def clr(event, ob): 
    '''''事件处理函数''' 
    ob.delete("all")
 
def handleradaptor(fun, **kwds): 
    '''''事件处理函数的适配器，相当于中介'''
    return lambda event,fun=fun,kwds=kwds: fun(event, **kwds)

def myship(event, ob):
    ob.delete("all")
    '''''事件处理函数'''
    points = [event.x - 2.5,event.y - 2.5,event.x + 2.5,event.y - 2.5,event.x - 2.5,event.y + 2.5,event.x + 2.5,event.y + 2.5]
    color= "#476042"
    ob.create_polygon(points, outline=color, 
            fill='yellow', width=3, tag="ship")

def leftmoving(event, ob):
    ob.delete("ship")
    '''''事件处理函数'''
    points = [event.x - 3.5,event.y - 3.5,event.x + 1.5,event.y - 3.5,event.x - 3.5,event.y + 1.5,event.x + 1.5,event.y + 1.5]
    ob.update()
    color= "#476042"
    ob.create_polygon(points, outline=color, 
            fill='yellow', width=3, tag="ship")

class App(object):

    def __init__(self,master):
        self.com3= Canvas(master,bg="white",width=500,height=500)
	#self.com3.bind("<Button-1>", handleradaptor(handler, a=1, b=2, c=3, ob=self.com3))
	#self.com3.bind("<Button-3>", handleradaptor(creatBox, ob=self.com3))
	self.com3.bind("<Button-1>", handleradaptor(myship, ob=self.com3))
	#self.com3.bind("<a>", handleradaptor(clr, ob=self.com3))
	self.com3.bind("<a>", handleradaptor(leftmoving, ob=self.com3))
	self.com3.pack(side=BOTTOM)
	self.com3.focus_set()
	self.com2=Label(master,text="Life Game")
	self.com2.pack(side = BOTTOM)
	self.wd=200	
root=Tk()
root.title('life game')
app=App(root)
root.mainloop()
