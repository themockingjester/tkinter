import tkinter as tk
class mapp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.a=tk.IntVar()
        
        self.spin=tk.Spinbox(self,from_=0,to=5,textvariable=self.a).pack()
        
        self.btn=tk.Button(self,text=" values",command= self.print_).pack()
    def print_(self):
    	self.b2=tk.Label(self,text=self.a.get()).pack()
    	
if __name__ == "__main__": 
    app=mapp()
    app.mainloop()
