import tkinter as tk

root = tk.Tk()

pic = tk.PhotoImage(file='C:\\Users\\yash2\\Downloads\\logo.png')

intro = """This is python i recently get a really huge 
popularity community support because of my simple syntax 
and power.i'm king of machine learning and data science
with rich  library support."""

# label1 = tk.Label(root, image=pic).pack(side='right')


label2 = tk.Label(root, text=intro, compound=tk.CENTER, image=pic)
label2.pack(side='left')

# w = tk.Label(root,
#              justify=tk.LEFT,
#              compound=tk.LEFT,
#              padx=10,
#              text=intro,
#              image=pic).pack(side="right")
tk.Label(root,
         text='Hey im in red color with blue background',
         bg='blue',
         fg='red').pack(side='bottom')


root.mainloop()
