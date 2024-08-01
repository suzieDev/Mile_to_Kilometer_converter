# from tkinter import *
import tkinter


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)


# Label
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
# my_label.pack(side="left")
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)
my_label.config(pady=50, padx=50)


# Button
button = tkinter.Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

# New Button
new_button = tkinter.Button(text="New Button")
new_button.grid(column=2, row=0)


# Entry
input = tkinter.Entry(width=10)
print(input.get())
# input.pack()
input.grid(column=3, row=2)




window.mainloop()

