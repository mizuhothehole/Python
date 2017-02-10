#coding:utf-8

from Tkinter import *  

def callback(event):
	print "clicked at", event.x, event.y

def handler(event, a, b, c, ob): 
    '''''事件处理函数''' 
    print "clicked at", event.x, event.y
    print ("handler", a, b, c )
    points = [0,0,event.x,event.y, 0, 500]
    color= "#476042"
    ob.create_polygon(points, outline=color, 
            fill='yellow', width=3)
 
def handleradaptor(fun, **kwds): 
    '''''事件处理函数的适配器，相当于中介''' 
    return lambda event,fun=fun,kwds=kwds: fun(event, **kwds)  	

class App(object):

    def __init__(self,master):
	self.com3= Canvas(master,bg="white",width=500,height=500)
	self.com3.bind("<Button-1>", handleradaptor(handler, a=1, b=2, c=3, ob=self.com3))
        self.com3.pack(side=BOTTOM)
        self.com3.focus_set()
	self.com2=Label(master,text="Life Game")
        self.com2.pack(side = BOTTOM)
        self.wd=200	
root=Tk()
root.title('life game')
app=App(root)
root.mainloop()
