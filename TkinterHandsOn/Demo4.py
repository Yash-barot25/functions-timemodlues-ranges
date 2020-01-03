import tkinter as tk

root = tk.Tk()
root.title('Color Effect')
root.geometry('500x300')
tk.Label(root,
         text='Hey i\'m in red color with blue background',
         bg='blue',
         fg='red',
         font='Times').pack()
tk.Label(root,
         text='Hey i\'m in Bold purple color',
         bg='yellow',
         fg='purple',
         font='Verdana 20 bold').pack()
tk.Label(root,
         text='Hey i\'m in green color in italic',
         fg='green',
         font='Helvetica 25 italic').pack()

root.mainloop()
