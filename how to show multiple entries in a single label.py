import tkinter as tk
class mapp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.a=tk.StringVar()
        self.v=tk.Entry(self,textvariable=self.a).pack()
        self.a.trace("w",self.show)
        self.bt5=tk.Label(self,relief=tk.SUNKEN)
        self.bt=tk.Button(self,command=self.show1,text='show').pack()
    def show1(self):
        self.bt5.pack()
        
    def show(self,*args):
        self.bt5.pack_forget()
        value=self.a.get()
        self.bt5.config(text=value)
    
    
if __name__ == "__main__": 
    app=mapp()
    app.mainloop()
