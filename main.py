import subprocess
import tkinter as tk
import os
directory_path = os.getcwd() + "GoogleAssitant.Bat"


root= tk.Tk() 
   
canvas1 = tk.Canvas(root, width = 350, height = 250) 
canvas1.pack()

def start_batch(): 
       #print(r'{}'.format(directory_path))
       subprocess.call([r'{}'.format(directory_path)])
           
button1 = tk.Button (root, text='Start Google Assistant',command=start_batch,bg='green',fg='white')
canvas1.create_window(170, 130, window=button1)

root.mainloop()
