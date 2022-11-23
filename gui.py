from bdb import effective
from tkinter import *
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("1920x1080")
root.attributes('-fullscreen',True)
root.title("Employee Management System")
root.config(bg = "white")
bg= tk.PhotoImage(file = "Motional Dark.png")
bgig= Label(root, i=bg)
bgig.pack()






def exitt():
     res = messagebox.askquestion('Exit Application', 'Do you really want to exit')
     if res == "yes":
        root.destroy()


def employee():
    root5 = Tk()
    root5.geometry("1920x1080")
    root5.attributes('-fullscreen',True)
    root5.title("Login Method")
    root5.config(bg = "white")
    login_mode = Label(root5, text = "Login Mode", font = ("Times New Roman", 30, "bold"))
    login_mode.place(x = 700, y = 50)
    usr_var = IntVar()
    #pin_var = IntVar()
    usrid_entry = Entry(root5, textvariable = usr_var, width = 30, font = ("Times New Roman", 20))
    usrid_entry.place(x = 700, y = 200)
    lol = usrid_entry.get()
    usrid_label = Label(root5, text = "User ID", font = ("Times New Roman", 20, "bold"))
    usrid_label.place(x = 700, y = 150)
    usrid_button = Button(root5, text = "Process ID", font = ("Times New Roman", 20, "bold"), bg = "white")
    usrid_button.place(x = 1300, y = 200)
    #usrid_pin_entry = Entry(root5, textvariable = pin_var, width = 30, font = ("Times New Roman", 20))
    #usrid_pin_entry.place(x = 700, y = 300)
    #usrid_pin_label = Label(root5, text = "Enter PIN", font = ("Times New Roman", 20, "bold"))
    #usrid_pin_label.place(x = 700, y = 250)


    def root5des():
     res5 = messagebox.askquestion('Exit', 'Do you really want to go back ?')
     if res5 == "yes":
        root5.destroy()
    gobackroot2 = Button(root5, text = "Back", font = ("Partylicious", 30, "bold"), bg = "white",fg = "red", command = root5des)
    gobackroot2.place(x = 1830, y = 10)

    





    
    

def admin():
    root3 = Tk()
    root3.geometry("1920x1080")
    root3.title("Existing Employee")
    root3.config(bg = "white")
    
    def root3des():
     res3 = messagebox.askquestion('Exit', 'Do you really want to go back ?')
     if res3 == "yes":
        root3.destroy()

root.wm_attributes('-transparentcolor', '#ab23ff')

l1 = Label(root, text = "Employee Management System", font = ("Neon Pixel-7", 50),bg='#160054',fg='white')
l1.place(x = 1, y = 1)

existingempbutton = Button(root, text = "Admin", font = ("Partylicious", 30, "bold"), bg = "#160054",fg="white", command = admin)
existingempbutton.place(x = 835, y = 200)

newempbutton = Button(root, text = "Employee", font = ("Partylicious", 30, "bold"), bg = "#160054",fg = "white", command = employee)
newempbutton.place(x = 815, y = 400)

exitbutton = Button(root, text = "X", font = ("Neon Pixel-7", 30, "bold"), bg = "#0b5ead",fg = "red", command = exitt)
exitbutton.place(x = 1830, y = 10)

endcredits = Label(root,text = "This project is created by Jumping Jacks", font = ("Partylicious", 20, "bold"),bg="#9a0065")
endcredits.place(x = 20, y = 990)

#This is the gui part i designed


root.mainloop()