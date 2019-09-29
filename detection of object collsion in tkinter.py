#Caution:------move image slowly to get the desired result because python is slow
import tkinter as tk

import time
class mapp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.minsize("1200","600")
        self.maxsize("1200","600")
        self.configure(bg="blue")
        #self.img=tk.PhotoImage(file="ukm.png")
        #self.i=tk.Label(self,image=self.img)
        #self.i.place(x=0,y=0)
        self.f=tk.Frame(self)
        self.f.place(x=0,y=20)
        
        #self.img1=tk.PhotoImage(file="kp.png")
        #self.img2=tk.PhotoImage(file="kp1.png")
        #self.i=tk.Label(self.f,image=self.img1)
        #self.i.pack()
        #self.bt=tk.Button(self.f,text="about us",bg="white",bd=0,image=self.img2,compound=tk.CENTER,highlightthickness=0,relief=tk.FLAT,font=("garamond", "15","bold"),height=40,anchor="n")
        #self.bt.place(x=50,y=0)
        
        #self.pauseb=tk.Button(self.f,text="pause",bg="white",bd=0,image=self.img2,compound=tk.CENTER,highlightthickness=0,relief=tk.FLAT,font=("garamond", "15","bold"),height=40,anchor="n")
        #self.pauseb.place(x=850,y=0)
        #self.playb=tk.Button(self.f,text="play",bd=0,image=self.img2,compound=tk.CENTER,highlightthickness=0,relief=tk.FLAT,font=("garamond", "15","bold"),height=40,anchor="n")
        #self.playb.place(x=950,y=0)
        #self.ent=tk.Entry(self.f,bd=0,font=("garamond", "15","bold"),width=50)
        #self.ent.place(x=220,y=8)
        #self.ent1=tk.Entry(self,bd=0,font=("garamond", "15","bold"),width=40)
        #self.ent1.place(x=380,y=350)
        #self.f1=tk.Frame(self)
        #self.f1.place(x=0,y=515)
        self.mon=tk.PhotoImage(file="mn.png")
        #self.i=tk.Label(self.f1,image=self.img3)
        #self.i.pack()
        #self.f.wm_attributes('-transparentcolor', self.f['bg'])
        self.can=tk.Canvas(self,width=1000,height=450)
        self.xcor=350
        self.ycor=300
        self.can.place(x=100,y=100)
        self.img1=self.can.create_image(10, 50, anchor=tk.NW, image=self.mon)
        self.can.create_image(self.xcor, self.ycor, anchor=tk.NW, image=self.mon)
        self.main()
    def main(self):
        self.can.bind("<B1-Motion>", self.monster1)
    def monster1(self,event):
        
            try:
                x=int(event.x)
                #print("x coor"+str(x)+"xcor"+str(self.xcor))
                self.can.coords(self.img1 ,int(str(x)),300)
                
                time.sleep(0.001)
                self.update()
                if abs(self.xcor - x) == 67:
                    print("collision!")
                
                
            except:
                pass
    def monster2(self):
        thread1 = threading.Thread(target = self.monster1, args=(event))      #game starts from here
        thread1.start()
        
if __name__ == "__main__":
    app=mapp()
    app.mainloop()


    
