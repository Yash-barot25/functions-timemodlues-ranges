import tkinter as tk

root = tk.Tk()

root.title("Hello Tkinter!")
# root.geometry('640x400')

label = tk.Label(root, text='Hey i\'m label')
label.pack()

root.mainloop()
