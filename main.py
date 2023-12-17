import tkinter

window = tkinter.Tk()
window.title("BMI CALCULATOR")
window.config(padx=40, pady=40)


def click_button():
    weight_input = weight_entry.get()
    height_input = height_entry.get()

    if weight_input == "" or height_input == "":
        bmi_label.config(text="Please Enter Number")

    else:
        try:
            bmi = float(weight_input) / (float(height_input) / 100) ** 2

            if bmi < 18.5:
                bmi_index = "Under Weight"
                bmi_label.config(text=f"Your Bmi is {round(bmi, 2)}.\nYou are {bmi_index}.")

            elif 18.5 <= bmi < 25:
                bmi_index = "Normal Weight"
                bmi_label.config(text=f"Your Bmi is {round(bmi, 2)}.\nYou are {bmi_index}.")

            elif 25 <= bmi < 30:
                bmi_index = "Over Weight"
                bmi_label.config(text=f"Your Bmi is {round(bmi, 2)}.\nYou are {bmi_index}.")

            elif bmi >= 30:
                bmi_index = "Obese"
                bmi_label.config(text=f"Your Bmi is {round(bmi, 2)}.\nYou are {bmi_index}.")

        except Exception:
            bmi_label.config(text="Please Enter Number")


weight_label = tkinter.Label(text="Enter Your Weight (kg)")
weight_label.pack()

weight_entry = tkinter.Entry(width=10)
weight_entry.pack()
weight_entry.focus()

height_label = tkinter.Label(text="Enter Your Height (cm)")
height_label.pack()

height_entry = tkinter.Entry(width=10)
height_entry.pack()

calc_button = tkinter.Button(text="Calculate", command=click_button)
calc_button.pack()

bmi_label = tkinter.Label()
bmi_label.pack()

window.mainloop()
