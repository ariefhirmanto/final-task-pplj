# #!/usr/bin/env python3

# """
# ZetCode Tkinter tutorial

# In this script, we lay out images
# using absolute positioning.

# Author: Jan Bodnar
# Website: www.zetcode.com
# """

# from PIL import Image, ImageTk
# from tkinter import Tk, BOTH
# from tkinter.ttk import Frame, Label, Style

# class Example(Frame):

#     def __init__(self):
#         super().__init__()

#         self.initUI()


#     def initUI(self):

#         self.master.title("Absolute positioning")
#         self.pack(fill=BOTH, expand=1)

#         Style().configure("TFrame", background="#333")

#         bard = Image.open("crab.png")
#         bardejov = ImageTk.PhotoImage(bard)
#         label1 = Label(self, image=bardejov)
#         label1.image = bardejov
#         label1.place(x=20, y=20)

#         rot = Image.open("crab.png")
#         rotunda = ImageTk.PhotoImage(rot)
#         label2 = Label(self, image=rotunda)
#         label2.image = rotunda
#         label2.place(x=40, y=160)

#         minc = Image.open("crab.png")
#         mincol = ImageTk.PhotoImage(minc)
#         label3 = Label(self, image=mincol)
#         label3.image = mincol
#         label3.place(x=170, y=50)


# def main():

#     root = Tk()
#     root.geometry("300x280+300+300")
#     app = Example()
#     root.mainloop()


# if __name__ == '__main__':
#     main()

# from tkinter import *
# root=Tk()

# def changeLabel():
#     myString.set("I'm, a-fraid we're fresh out of red Leicester, sir. ")
    
# myString=StringVar()
# Label(root,textvariable=myString).pack()
# myString.set("Well, eh, how about a little red Leicester.")
# Button(root,text='Click Me',command=changeLabel).pack()
# root.mainloop()


# import tkinter as tk

# You will need the ttk module for this
# from tkinter import ttk

# def update_status(step):

#     # Step here is how much to increment the progressbar by.
#     # It is in relation to the progressbar's length.
#     # Since I made the length 100 and I am increasing by 10 each time,
#     # there will be 10 times it increases before it restarts
#     progress.step(step)

#     # You can call 'update_status' whenever you want in your script
#     # to increase the progressbar by whatever amount you want.
#     root.after(1000, lambda: update_status(10))

# root = tk.Tk()

# progress = ttk.Progressbar(root, length=100)
# progress.pack()

# progress.after(1, lambda: update_status(10))

# root.mainloop()

# import tkinter as tk

# root = tk.Tk()

# status = tk.Label(root, text="Working")
# status.grid()

# def update_status():

#     # Get the current message
#     current_status = status["text"]

#     # If the message is "Working...", start over with "Working"
#     if current_status.endswith("..."): current_status = "Working"

#     # If not, then just add a "." on the end
#     else: current_status += "."

#     # Update the message
#     status["text"] = current_status

#     # After 1 second, update the status
#     root.after(1000, update_status)

# # Launch the status message after 1 millisecond (when the window is loaded)
# root.after(1, update_status)

# root.mainloop()


from tkinter import *

root = Tk()
var = StringVar()
var.set('hello')

l = Label(root, textvariable = var)
l.pack()

t = Entry(root, textvariable = var)
t.pack()

root.mainloop() # the window is now displayed