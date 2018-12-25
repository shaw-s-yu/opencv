from Tkinter import *

class App:
    def __init__(self):
        self.x=None
        self.y=None
        self.press=False

        
        self.root=Tk()
        self.root.title('painter')
        self.canvas=Canvas(self.root,width=500,height=500)
        self.canvas.pack()
        self.canvas.bind("<Motion>",self.draw)
        self.canvas.bind("<ButtonPress-1>",self._press)
        self.canvas.bind("<ButtonRelease-1>",self._release)
        self.root.bind("<Escape>",self.destroy)
        self.root.mainloop()

    def _press(self,event):
        self.press=True

    def _release(self,event):
        self.press=False
        self.x=None
        self.y=None
        
    def draw(self,event):
        if self.press:
            if self.x is not None and self.y is not None:
                event.widget.create_line(self.x,self.y,event.x,event.y,smooth=TRUE)
            self.x=event.x
            self.y=event.y
    def destroy(self,event):
        self.root.destroy()
App()
