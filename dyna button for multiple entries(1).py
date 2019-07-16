import tkinter as tk
class mapp(tk.Tk):
	def __init__(self):
    	
		super().__init__()
                
		self.var1=tk.StringVar()
		self.var2=tk.StringVar()
		self.var=tk.StringVar()
		self.var.trace("w",self.func) and self.var1.trace("w",self.func) and self.var2.trace("w",self.func)
		
		self.a=tk.Button(self,text="hi",state=tk.DISABLED)
		self.b=tk.Entry(text="elect",textvariable=self.var).pack()
		self.b=tk.Entry(text="elect",textvariable=self.var2).pack()
		self.b=tk.Entry(text="elect",textvariable=self.var1).pack()
		self.a.pack()
	def func(self,*args):
		ctr=0
		if(self.var.get()!="" and self.var1.get()!=""):
			ctr+=1
		if ctr==1:
			self.a.pack_forget()
			self.a.config(state=tk.NORMAL)
			self.a.pack()
            
		else:
			self.a.pack_forget()
			self.a.config(state=tk.DISABLED)
			self.a.pack()
        
app=mapp()
app.mainloop()
