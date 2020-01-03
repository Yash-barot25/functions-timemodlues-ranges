import tkinter as tk

root = tk.Tk()
root.title('Pack geometry manager')
root.geometry('600x450')

label = tk.Label(root, text='Practice')
label.pack(side='top')

leftFrame = tk.Frame(root)
leftFrame.pack(side='left', fill=tk.Y, anchor='n')

canvas = tk.Canvas(leftFrame, relief='raised', borderwidth=1)
canvas.pack(side='left', anchor='n')

rightFrame = tk.Frame(root)
rightFrame.pack(side=tk.RIGHT, expand=True, anchor='n')

button1 = tk.Button(rightFrame, text='Button1')
button2 = tk.Button(rightFrame, text='Button2')
button3 = tk.Button(rightFrame, text='Button3')
button4 = tk.Button(rightFrame, text='Button4')

button1.pack(side='top')
button2.pack(side='top')
button3.pack(side='top')
button4.pack(side='top')

root.mainloop()
