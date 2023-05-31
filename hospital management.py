from tkinter import *
from tkinter import messagebox
import time
root = Tk()
root.geometry("400x300")
root.config(bg = "light blue")


def new_window2():

    root2 = Tk()
    root2.geometry("400x300")
    root2.config(bg = "light blue")

    heading_label1 = Label(root2 , text = "Doctor's Dashboard" , font = ("calibri" , 15 , "bold") , bg = "light blue")
    heading_label1.place(x = 110 , y = 20)

    name_label = Label(root2 , text = "Name:" , font = ("calibri" , 15 ), bg = "light blue")
    name_label.place(x = 30 , y = 60)

    name_entry = Entry(root2 , width = 25)
    name_entry.place(x = 90 , y = 65)

    prescription_label = Label(root2 , text = "Prescription:" , font = ("calibri" , 15 ), bg = "light blue")
    prescription_label.place(x = 30 , y = 90)

    prescription_text = Text(root2 , height = 5 , width = 30)
    prescription_text.place(x = 140 , y = 92)

    def ok():
        messagebox.showinfo("thank you" , "we have recived the prescription")

    proceed_button = Button(root2 , text = "PROCEED" ,font = ("calibri" , 15 , "bold") , command = ok)
    proceed_button.place(x = 110 , y = 200)

    cancel_button = Button(root2 ,text = "CANCEL" ,font = ("calibri" , 15 , "bold"))
    cancel_button.place(x = 220 , y = 200)

    clock_label = Label(root2, fg="black", bg="light blue", font=("calibri", 12, "bold"))
    clock_label.place(x = 310 , y = 10)

    def digital_clock():
        time_live = time.strftime("%I:%M:%S %p")
        clock_label.config(text=time_live)
        clock_label.after(1000, digital_clock)

    digital_clock()

def new_window3():
    root3 = Tk()
    root3.geometry("400x300")
    root3.config(bg = "light blue")

    heading_label2 = Label(root3 , text = "Patient Dashboard" , font = ("calibri" , 15 , "bold") , bg = "light blue")
    heading_label2.place(x = 110 , y = 20)

    def check():
        if disease_entry.get() == "dengue" or "cancer" or "asthma" or "cough" and contact_entry.get() == 10:
            messagebox.showinfo("thank you" , "we have recived your response")
        else:
            messagebox.showerror("wrong" , "please fill the fields correctly")

    name_label2 = Label(root3 , text = "Name:" , font = ("calibri" , 15) , bg = "light blue")
    name_label2.place(x = 30 , y = 60)

    name_entry2 = Entry(root3 , width = 25)
    name_entry2.place(x = 150 , y = 65)

    disease_label = Label(root3 , text = "Disease:" , font = ("calibri" , 15) , bg = "light blue")
    disease_label.place(x = 30 , y = 100)

    disease_entry = Entry(root3 , width = 25)
    disease_entry.place(x = 150 ,y = 105)

    weight_label = Label(root3, text = "Weight:" , font = ("calibri" , 15) , bg = "light blue")
    weight_label.place(x = 30 , y = 140)

    weight_entry = Entry(root3 , width = 25)
    weight_entry.place(x = 150 , y = 145)

    contact_label = Label(root3 , text = "Contact No. :" , font = ("calibri" , 15) , bg = "light blue")
    contact_label.place(x = 30 , y = 180)

    contact_entry = Entry(root3 , width = 25)
    contact_entry.place(x = 150 , y = 185)

    ok_button = Button(root3 , text = "OK" , font = ("calibri" , 15) , command = check)
    ok_button.place(x = 130 , y = 230)

    cancel_button2 = Button(root3 , text = "CANCEL" , font = ("calibri" , 15))
    cancel_button2.place(x = 200 , y = 230)

    clock_label = Label(root3, fg="black", bg="light blue", font=("calibri", 12, "bold"))
    clock_label.place(x=310, y=10)

    def digital_clock():
        time_live = time.strftime("%I:%M:%S %p")
        clock_label.config(text=time_live)
        clock_label.after(1000, digital_clock)

    digital_clock()

heading_label = Label(root , text = "HOSPITAL MANAGEMENT SYSTEM" , font = ("gabriola" , 16 , "bold") , bg = "light blue")
heading_label.place(x = 55 , y = 25)

doctor_button = Button(root , text = "Doctor's login" , font = ("calibri" , 13 , "bold") , fg = "red" , command = new_window2)
doctor_button.place(x = 20 , y = 80)

nurse_button = Button(root , text = "Nurse's login" , font = ("calibri" , 13 , "bold") , fg = "red")
nurse_button.place(x = 140 , y = 80)

patient_button = Button(root , text = "Patient's login" , font = ("calibri" , 13 , "bold") , fg = "red" , command = new_window3)
patient_button.place(x = 260 , y = 80)

adminn_button = Button(root , text = "Admin's login" , font = ("calibri " , 13 , "bold") , fg = "red")
adminn_button.place(x = 140 , y = 140)

clock_label = Label(root, fg="black", bg="light blue", font=("calibri", 10, "bold"))
clock_label.place(x=315, y=5)


def digital_clock():
    time_live = time.strftime("%I:%M:%S %p")
    clock_label.config(text=time_live)
    clock_label.after(1000, digital_clock)


digital_clock()

root.mainloop()
