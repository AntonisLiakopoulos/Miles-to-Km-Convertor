from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Miles to Kilometers Converter")
#window.minsize(width=300, height=200)
window.configure(padx=20,pady=20)

#INPUT
entry = Entry(width=10)
entry.insert(END, string="")
entry.grid(column=2,row=1)

#LABELS
label_2 = Label(text="is equal to")
label_2.grid(column=1, row=2)
label_3 = Label(text="0")
label_3.grid(column=2,row=2)
label_miles = Label(text="Miles")
label_miles.grid(column=3,row=1)
label_km = Label(text="Km")
label_km.grid(column=3,row=2)

def updated_entry_scale(value):
        entry.delete(0, END)  # Clear previous value
        entry.insert(0, value)

def scale_used(value):
    entry.insert(END, string=str(scale.get()))
scale = Scale(from_=0, to=100, sliderlength=20, command=updated_entry_scale)
scale.grid(column=4,row=2)

# CONVERSION FUNCTIONS
def miles_to_km():
        miles = float(entry.get())
        km = miles * 1.609
        return km

def km_to_miles():
        km = float(entry.get())
        miles = km / 1.609
        return miles

#SELECT CONVERTOR

def radio_used():
        km = miles_to_km()
        miles = km_to_miles()
        if radio_state.get() == 1:
                label_miles.config(text="Miles")
                label_km.config(text="Km")
                label_3.configure(text=km)
        elif radio_state.get() == 2:
                label_miles.config(text="Km")
                label_km.config(text="Miles")
                label_3.configure(text=miles)

radio_state = IntVar()
radiobutton1 = Radiobutton(text="From Miles to Km", value=1, variable=radio_state, command=miles_to_km)
radiobutton2 = Radiobutton(text="From Km to Miles", value=2, variable=radio_state, command=km_to_miles)
radiobutton1.grid()
radiobutton2.grid()


#BUTTON

button = Button(text="Calculate", command=radio_used)
button.grid(column=2,row=3)


window.mainloop()
