import tkinter as tk


def printer():
    print("Hello world!")


root = tk.Tk()

frame = tk.Frame(root)
frame.pack()

quit_btn = tk.Button(frame, text='Quit', fg='red',command=quit).pack(side=tk.LEFT)

print_btn = tk.Button(frame, text='press me', fg='blue',  command=printer).pack(side=tk.LEFT)

root.mainloop()
