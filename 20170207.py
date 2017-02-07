from Tkinter import *  
  
class App(object):
    def __init__(self,master):
       
	self.com3= Canvas(master,bg="white",width=200,height=200)
        self.com3.create_oval(50,50,150,150,tags="oval")
        self.com3.pack(side=BOTTOM)
        #self.com3.focus_set()
	self.com2=Label(master,text="NicoNico")
        self.com2.pack(side = BOTTOM)
	self.com=Button(master,text='create a circle', command=self.sayHi())
        self.com.pack(side=BOTTOM)
    def sayHi(self):
	pass

root=Tk()
root.title('window with command')
app=App(root)
root.mainloop()
