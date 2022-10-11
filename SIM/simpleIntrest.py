
from cProfile import label
from tkinter import *
from unicodedata import name
from unittest import result

window = Tk()
window.title("Simple Interest Calculator")
window.geometry("400x400")
window.configure(bg='grey')


def simpleInterest():
    p = int(principal.get())
    r = int(rate_lable.get())
    t = int(time.get())
    si = (p*r*t)/100
    si = round(si, 2)
    result_lable.destroy()
    output_msg = Label(result_frame, text='Simple Interest is: ' + str(si))
    output_msg.place(x=20, y=40)
    output_msg.pack()


heading_lable = Label(window, text="Simple Interest Calculator",
                      bg='grey', fg='black', font=('Arial', 20), bd=5)
heading_lable.place(x=50, y=20)

name_lable = Label(window, text="Principal", bg='grey',
                   fg='black', font=('Arial', 12), bd=4)
name_lable.place(x=20, y=90)

principal = Entry(window, text='', width=22)
principal.place(x=150, y=90)

result_frame = LabelFrame(
    window, text="Result", bg='grey', fg='black', font=('Arial', 12), width=33)
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20, y=300)

result_lable = Label(result_frame, text="Your Simple Interest is: ",
                     bg='grey', font=('Arial', 12), width=33)
result_lable.place(x=20, y=20)
result_lable.pack()

rate_lable = Label(window, text="Rate", bg='grey',
                   fg='black', font=('Arial', 12), bd=1)
rate_lable.place(x=20, y=120)
rate_lable = Entry(window, text='', width=22)
rate_lable.place(x=150, y=142)


time = Label(window, text="Time", bg='grey',
             fg='black', font=('Arial', 12), bd=1)
time.place(x=20, y=170)
time = Entry(window, text='', width=22)
time.place(x=150, y=192)

calculate_button = Button(window, text="Calculate", command=simpleInterest,
                          fg='black', bg='grey', font=('Arial', 12), bd=4)
calculate_button.place(x=150, y=220)


window.mainloop()
