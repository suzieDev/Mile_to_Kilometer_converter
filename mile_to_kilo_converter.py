from tkinter import *
import tkinter

def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    kilometer_result_label.config(text=f"{km}")


window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

is_equal_label = tkinter.Label(text="is equal to", font=("Arial", 20))
is_equal_label.grid(column=0, row=1)
is_equal_label.config(pady=10, padx=50)

miles_label = tkinter.Label(text="Miles", font=("Arial", 20))
miles_label.grid(column=2, row=0)
miles_label.config(padx=50)

kilometer_label = tkinter.Label(text="Km", font=("Arial", 20))
kilometer_label.grid(column=2, row=1)
kilometer_label.config(padx=50)

# Entries
miles_input = tkinter.Entry(width=7)
miles_input.grid(column=1, row=0)

kilometer_result_label = tkinter.Label(text="0")
kilometer_result_label.grid(column=1, row=1)

# Button
cal_button = tkinter.Button(text="Calculate", command=miles_to_km)
cal_button.grid(column=1, row=2)



window.mainloop()