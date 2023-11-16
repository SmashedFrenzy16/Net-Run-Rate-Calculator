from tkinter import *

root = Tk()

root.title("Net Run Rate Calculator By @SmashedFrenzy16")

root.geometry("600x400")

def execute():

    global runs_s

    runs_s = float(runs_s_e.get())

def execute2():

    global overs_f

    overs_f = float(overs_f_e.get())

def execute3():

    global runs_c

    runs_c = float(runs_c_e.get())

def execute4():

    global overs_b

    overs_b = float(overs_b_e.get())

def execute5():

    nrr = (runs_s / overs_f) - (runs_c / overs_b)

    blank_label2 = Label(root, text="")

    blank_label2.pack()

    result = Label(root, text=str(nrr))

    result.pack()

title_label = Label(
            root, fg="black", text="BMI Calculator", font=("Arial", 48))

title_label.pack()

blank_label = Label(root, text="")

blank_label.pack()

runs_s_e = Entry(root, width=100, borderwidth=5)

runs_s_e.pack()

runs_s_e.insert(0, "Enter in the total runs scored")

runs_s_button = Button(root, text="Enter", command=execute)

runs_s_button.pack()

overs_f_e = Entry(root, width=100, borderwidth=5)

overs_f_e.pack()

overs_f_e.insert(0, "Enter in the total overs faced")

overs_f_button = Button(root, text="Enter", command=execute2)

overs_f_button.pack()

runs_c_e = Entry(root, width=100, borderwidth=5)

runs_c_e.pack()

runs_c_e.insert(0, "Enter in the total runs conceded")

runs_c_button = Button(root, text="Enter", command=execute3)

runs_c_button.pack()

overs_b_e = Entry(root, width=100, borderwidth=5)

overs_b_e.pack()

overs_b_e.insert(0, "Enter in the total overs bowled")

overs_b_button = Button(root, text="Enter", command=execute4)

overs_b_button.pack()

result_button = Button(root, text="Get Result", command=execute5)

result_button.pack()

root.mainloop()