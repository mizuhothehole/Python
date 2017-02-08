#coding:utf-8
from Tkinter import *  

class App(object):

    def __init__(self,master):
        self.canvas_width=200
	self.canvas_height=200
	self.python_green = "#476042"
	self.name1 = 'create a mass'
	self.name2 = 'create a polygon'
	self.name3 = 'create bitmap group'
	self.name4 = 'create a star'
	self.name5 = 'create a img'
	self.com3= Canvas(master,bg="white",width=200,height=200)
        self.com3.create_oval(50,50,150,150,tags="oval")
	#self.com3.create_rectangle(10,10,30,30,fill="#234134")
        self.com3.pack(side=BOTTOM)
        self.com3.focus_set()
	self.com2=Label(master,text="NicoNico")
        self.com2.pack(side = BOTTOM)
	self.com=Button(master,text=self.name1, command=self.sayHi)
        self.com.pack(side=BOTTOM)
	self.com4=Button(master,text=self.name2, command=self.makepolygon)
	self.com4.pack(side=BOTTOM)
	self.com5=Button(master,text=self.name3, command=self.createBitmapgroup)
	self.com5.pack(side=BOTTOM)
	self.com6=Button(master,text=self.name4, command=self.createStar)
	self.com6.pack(side=BOTTOM)
	self.com7=Button(master,text=self.name5, command=self.createImg)
	self.com7.pack(side=BOTTOM)
        self.wd=200
    def sayHi(self):
	self.com3.create_rectangle(11,11,40,40,fill="#674567")
	self.com3.create_line(1,1,15,15)
    def makepolygon(self):
	width = 200
	height = 200
	color= "#476042"
	points = [0,0,width,width/2, 0, height]
	self.com3.create_polygon(points, outline=color, 
            fill='yellow', width=3)
    def createBitmapgroup(self):
	#create bitmap in canvas,listting all the bitmaps
	bitmaps = ["error", "gray75", "gray50", "gray25", "gray12", "hourglass", "info", "questhead", "question", "warning"]
	nsteps = len(bitmaps)
	step_x = int(200 / nsteps)
	for i in range(0, nsteps):
		self.com3.create_bitmap((i+1)*step_x - step_x/2,50, bitmap=bitmaps[i])
    def createStar(self):
	color= "#476042"
	points = [100, 140, 110, 110, 140, 100, 110, 90, 100, 60, 90, 90, 60, 100, 90, 110]
	self.com3.create_polygon(points, outline=color, 
            fill='yellow', width=3)
    def createImg(self):
	photo = PhotoImage(file = '/home/shin/デスクトップ/32847b7bd7a1adbdf1e72e41784b6427(1).gif')
        self.com3.create_image(100,100, image=photo)

	
root=Tk()
root.title('window with command')
app=App(root)
root.mainloop()
