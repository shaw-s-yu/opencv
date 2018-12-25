from Tkinter import *

class App:
    def __init__(self):
        self.root=Tk()
        self.root.title('232')
        self.pressed={}
        self.key=[False,False,False,False]
        self.canvas=Canvas(self.root,width=500,height=500)
        self.canvas.pack()
        self.point=Point(self.canvas,color="red",x=30,y=30)
        for key in ["Up","Down","Left","Right"]:
            self.root.bind("<KeyPress-%s>" % key, self._pressed)
            self.root.bind("<KeyRelease-%s>" % key, self._released)
            self.pressed[key.lower()]=False
        self.animate()
        self.root.mainloop()

    def animate(self):
        if self.pressed['up']: self.point.move_up()
        if self.pressed['left']: self.point.move_left()
        if self.pressed['right']: self.point.move_right()
        if self.pressed['down']: self.point.move_down()            
        self.point.move()
        self.root.after(10,self.animate)

    def _pressed(self,event):
        k=event.keysym.lower()
        self.pressed[k]=True
    def _released(self,event):
        k=event.keysym.lower()
        self.pressed[k]=False
        
class Point:
    def __init__(self, canvas, color='red',x=30,y=30):
        self.canvas=canvas
        self.x=x
        self.y=y
        self.color=color
        self.circles=[]
    def move_up(self):
        self.y=max(self.y-2,0)
    def move_left(self):
        self.x=max(self.x-2,0)
    def move_down(self):
        self.y=min(self.y+2,500)
    def move_right(self):
        self.x=min(self.x+2,500)
    def move(self):    
        x0 = self.x - 10
        x1 = self.x + 10
        y0 = self.y - 10
        y1 = self.y + 10
        p=self.canvas.create_oval(x0,y0,x1,y1, fill=self.color)
        self.circles.append(p)                        
        if len(self.circles)>100:
            self.canvas.delete(self.circles[0])
            self.circles.pop(0)
        
        
App()
