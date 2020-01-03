import tkinter as tk

master = tk.Tk()
master.title('Quote')

whatever_you_do = """Whatever you do will be insignificant, But it
is very important that you do it.
-Mahatma Gandhi"""

message = tk.Message(master, text=whatever_you_do)
message.config(bg='lightblue', fg='red', font=('Times', 20, 'bold italic'))
message.pack()
master.mainloop()
