import tkinter

# print(tkinter.TkVersion)
# print(tkinter.TclVersion)

mainWindow = tkinter.Tk()

mainWindow.title("Hello world!!!")
mainWindow.geometry('640x400')

exit_btn = tkinter.Button(mainWindow, text="Exit", command=exit)

exit_btn.pack(side='bottom')

my_label = tkinter.Label(mainWindow, text="Created by: YASHKUMAR BAROT")
my_label.pack(side='bottom')

mainWindow.mainloop()
