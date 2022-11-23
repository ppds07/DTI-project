from os import system
import re
import mysql.connector
from bdb import effective
from tkinter import *
import tkinter as tk
from tkinter import messagebox

# create main gui table
root = tk.Tk()
root.geometry("1920x1080")
root.attributes('-fullscreen',True)
root.title("Employee Management System")
root.config(bg = "white")
bg= tk.PhotoImage(file = "Motional Dark.png")
bgig= Label(root, i=bg)
bgig.pack()

#def menu():


def exitt():
     res = messagebox.askquestion('Exit Application', 'Do you really want to exit')
     if res == "yes":
        root.destroy()

def rootalldes():
    root1.destroy()


con = mysql.connector.connect(
    host="127.0.0.1",port="3306", user="root", password="amanSHARMA@070604")

# preparing a cursor object
cursorObject = con.cursor()
 
# creating database
cursorObject.execute("USE employee")

# make a regular expression
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
# for validating an Phone Number
Pattern = re.compile("(0|91)?[7-9][0-9]{9}")


# Function To Check if Employee With
# given Name Exist or not
def check_employee_name(employee_name):
    # query to select all Rows from
    # employee(empdata) table
    sql = 'select * from empdata where Name=%s'

    # making cursor buffered to make
    # rowcount method work properly
    c = con.cursor(buffered=True)
    data = (employee_name,)

    # Execute the sql query
    c.execute(sql, data)

    # rowcount method to find number
    # of rowa with given values
    r = c.rowcount
    if r == 1:
        return True
    else:
        return False
#This is actual code using the terminal part


def check_employee(employee_id):
    # query to select all Rows from
    # employee(empdata) table
    sql = 'select * from empdata where Id=%s'

    # making cursor buffered to make
    # rowcount method work properly
    c = con.cursor(buffered=True)
    data = (employee_id,)

    # Execute the sql query
    c.execute(sql, data)

    # rowcount method to find number
    # of rowa with given values
    r = c.rowcount
    if r == 1:
        return True
    else:
        return False
    

def employee_login():
    root1 = Tk()
    root1.geometry("1920x1080")
    root1.attributes('-fullscreen',False)
    root1.title("LOGIN")
    root1.config(bg = "white")
    titl_l = Label(root1,text = "Employee Id: ",font = ("Partylicious", 30, "bold"), bg = "white",fg = "red")
    titl_l.place(x=150,y=100)
    empid_entry = Entry(root1, width = 35)
    empid_entry.place(x=200,y=100)
    eidval = empid_entry.get()
    if(check_employee(Id) == False):
        messagebox.showerror("Error", "Employee Record Not Found")
        rootalldes()
        press = input("Press Any Key To Continue..")
        

    root1.mainloop()

title_label = Label(root, text = "Employee Management System", font = ("Neon Pixel-7", 50),bg='#160054',fg='white')
title_label.place(x = 1, y = 1)

empbutton = Button(root, text = "EMPLOYEE", font = ("Partylicious", 30, "bold"), bg = "#160054",fg="white", command = employee_login)
empbutton.place(x = 815, y = 250)

adminbutton = Button(root, text = "ADMIN", font = ("Partylicious", 30, "bold"), bg = "#160054",fg = "white")#, command = employee)
adminbutton.place(x = 860, y = 450)

exitbutton = Button(root, text = "X", font = ("Neon Pixel-7", 30, "bold"), bg = "#0b5ead",fg = "red", command = exitt)
exitbutton.place(x = 1830, y = 10)

endcredits = Label(root,text = "This project is created by Jumping Jacks", font = ("Partylicious", 20, "bold"),bg="#9a0065")
endcredits.place(x = 20, y = 990)

root.mainloop()