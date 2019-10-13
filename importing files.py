
import tkinter as tk
from tkinter import filedialog
import pandas as pd

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'lightsteelblue2', relief = 'raised')
canvas1.pack()

def getfile ():
    global df
    
    import_file_path = filedialog.askopenfilename()
    with open (import_file_path,'r') as df:
        for i in df:
            print(i)
    
browseButton = tk.Button(text="      Import File     ", command=getfile, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 150, window=browseButton)

root.mainloop()
