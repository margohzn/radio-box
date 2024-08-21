#radio button widjet and cheak button widjet

from tkinter import * 
from tkinter import messagebox

def submit():
    selected_color = colorvar.get()
    selected_options = []
    if option1_var.get():
        selected_options.append("option1")
    if option2_var.get():
        selected_options.append("option2")
    if option3_var.get():
        selected_options.append("option3")

    message = f"Selected color is: {selected_color}\n Selected options: {selected_options}"
    messagebox.showinfo("Final data", message)

window = Tk()
window.geometry("300x300")
window.title("Radio button and Cheak box")

colorvar = StringVar(value = "Red")
option1_var = BooleanVar(value = False)
option2_var = BooleanVar(value = False)
option3_var = BooleanVar(value = False)

label1 = Label(window, text = "Select a color").pack(pady = 10)

radio_frame = Frame(window).pack()
Radiobutton(radio_frame, text = "Red", variable = colorvar, value = "Red").pack()
Radiobutton(radio_frame, text = "Blue", variable = colorvar, value = "Blue").pack()
Radiobutton(radio_frame, text = "Green", variable = colorvar, value = "Green").pack()

label2 = Label(window, text = "Select options").pack(pady = 10)

cheak_frame = Frame(window).pack()
Checkbutton(cheak_frame, text = "Option 1", variable = option1_var).pack()
Checkbutton(cheak_frame, text = "Option 2", variable = option2_var).pack()
Checkbutton(cheak_frame, text = "Option 3", variable = option3_var).pack()

button1 = Button(window, text = "Submit", command = submit).pack()


window.mainloop()