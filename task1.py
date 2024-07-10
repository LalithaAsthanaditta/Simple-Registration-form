import tkinter as tk
from tkinter import messagebox

def register_form():
    name = fill_name.get()
    email = fill_email.get()
    age = fill_age.get()
    if name and email and age:
        messagebox.showinfo("Registration Successful", "Thank you for registering!")
    else:
        messagebox.showerror("Error", "Please fill in all fields")

reg = tk.Tk()
reg.title("Registration filling page")
reg.geometry('400x400')
tk.Label(reg, text="Name").grid(row=0)
tk.Label(reg, text="Email").grid(row=1)
tk.Label(reg, text="Age").grid(row=2)

fill_name = tk.Entry(reg)
fill_email = tk.Entry(reg)
fill_age = tk.Entry(reg)

fill_name.grid(row=0, column=2)
fill_email.grid(row=1, column=2)
fill_age.grid(row=2, column=2)

register_button = tk.Button(reg, text="Submit", command=register_form)
register_button.grid(row=3, column=1)

reg.mainloop()
