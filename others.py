import os
import tkinter as tk
# name = "John"
# age = 23
# if name == "John" and age == 23:
#     print("Your name is John, and you are also 23 years old.")
#
# if name == "John" or name == "Rick":
#     print("Your name is either John or Rick.")
#
# pingName = input('What is the org you wanna search for?\n')
# os.system("ping -n 5 %s.org" %pingName)
# tupin = input('What info do you wanna search for?\n')
# os.system("%s tupin" %tupin)

root = tk.Tk()

def click():
    os.system(('C:\\Windows\\System32\\calc.exe'))

root.geometry("800x500")
root.title("GUI")

label = tk.Label(root, text="hello bro", font=('Arial', 18))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=3,  font=('Arial', 10))
textbox.pack()

#same as text but it is only one line
myentry= tk.Entry(root)
myentry.pack()

button = tk.Button(root, text="click here", font=('Arial', 18))
button.pack(padx=20, pady=20)

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(0, weight=2)
buttonframe.columnconfigure(0, weight=3)

btn1 = tk.Button(buttonframe, text="1", font=('Arial', 15))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

btn2 = tk.Button(buttonframe, text="2", font=('Arial', 15))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(buttonframe, text="3", font=('Arial', 15))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

#if i put command=click() instead of click(raw) then it would automatically open without me doing anything
butto = tk.Button(root, text="calculator",command=click)
butto.pack()

buttonframe.pack()

root.mainloop()
