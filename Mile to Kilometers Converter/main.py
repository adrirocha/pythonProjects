from tkinter import *

window = Tk()
window.title("Mile to Km Converter")

# Converter function
def miles_to_km():
    miles_to_convert = float(miles_entry.get())
    km = miles_to_convert*1.609
    converter_answer_label.config(text=str(km))

# Entry
miles_entry = Entry(width=10)
miles_entry.insert(END, string="0")
miles_entry.grid(row=0, column=1)

# Miles Label
miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

# is equal to Label
is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(row=1, column=0)

# Converter Answer Label
converter_answer_label = Label(text="0")
converter_answer_label.grid(row=1, column=1)

# Km Label
km_label = Label(text="Km")
km_label.grid(row=1,column=2)

# Calculate Button
calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(row=2,column=1)



window.mainloop()
