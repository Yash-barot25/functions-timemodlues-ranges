# import tkinter as tk
#
# root = tk.Tk()
# root.title('Languages')
# root.geometry('500x300')
#
# v = tk.IntVar()
# v.set(1)
#
#
# def show_val():
#     print(v.get())
#
#
# languages = [(1, "JAVA"), (2, "Python"), (3, "c#"), (4, "Javascript")]
# tk.Label(root, text="""Choose Language you like most""", justify=tk.LEFT, padx=20).pack()
#
# for val, language in languages:
#     tk.Radiobutton(root, text=languages, value=val, variable=v, command=show_val, padx=20).pack(anchor=tk.W)
# root.mainloop()
import tkinter as tk

root = tk.Tk()

v = tk.IntVar()
v.set(1)  # initializing the choice, i.e. Python

languages = [
    ("Python", 1),
    ("Perl", 2),
    ("Java", 3),
    ("C++", 4),
    ("C", 5)
]


def ShowChoice():
    print(v.get())


tk.Label(root,
         text="""Choose your favourite 
programming language:""",
         justify=tk.LEFT,
         padx=20).pack()

for val, language in enumerate(languages):
    tk.Radiobutton(root,
                   text=language,
                   padx=20,
                   variable=v,
                   command=ShowChoice,
                   value=val).pack(anchor=tk.W)

root.mainloop()
