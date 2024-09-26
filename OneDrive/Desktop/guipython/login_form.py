import tkinter as tk
from tkinter import messagebox

# Dictionary to store user credentials (In an actual use case, this should be a secure database)
users = {}

def signup():
    username = entry_username.get()
    password = entry_password.get()

    if username in users:
        messagebox.showerror("Error", "Username already exists!")
    elif username == "" or password == "":
        messagebox.showerror("Error", "Please fill out both fields!")
    else:
        users[username] = password
        messagebox.showinfo("Success", "Signed up successfully!")
        clear_entries()

def login():
    username = entry_username.get()
    password = entry_password.get()

    if username == "" or password == "":
        messagebox.showerror("Error", "Please fill out both fields!")
    elif username not in users:
        messagebox.showerror("Error", "Username not found! Please sign up.")
    elif users[username] != password:
        messagebox.showerror("Error", "Incorrect password!")
    else:
        messagebox.showinfo("Success", f"Welcome {username}!")
        clear_entries()

def clear_entries():
    entry_username.delete(0, tk.END)
    entry_password.delete(0, tk.END)

# Create the main window using tkinter
root = tk.Tk()
root.title("Login/Sign-up Form")
root.geometry("400x300")
root.config(bg="#ADD8E6")  # Light blue background

# Create frames for the layout
frame = tk.Frame(root, bg="#ADD8E6")
frame.pack(pady=20)

# Custom fonts and styles
label_style = {'bg': "#ADD8E6", 'font': ("Helvetica", 14, 'bold'), 'fg': "#00008B"}  # Dark blue text
entry_style = {'font': ("Helvetica", 12)}
button_style = {'font': ("Helvetica", 12, 'bold'), 'bg': "#32CD32", 'fg': "white", 'activebackground': "#228B22", 'activeforeground': "white", 'relief': tk.GROOVE}  # Green button

# Username Label and Entry
label_username = tk.Label(frame, text="Username", **label_style)
label_username.grid(row=0, column=0, padx=10, pady=10)
entry_username = tk.Entry(frame, **entry_style)
entry_username.grid(row=0, column=1, padx=10, pady=10)

# Password Label and Entry
label_password = tk.Label(frame, text="Password", **label_style)
label_password.grid(row=1, column=0, padx=10, pady=10)
entry_password = tk.Entry(frame, show="*", **entry_style)
entry_password.grid(row=1, column=1, padx=10, pady=10)

# Buttons for Login and Sign-up
button_login = tk.Button(frame, text="Login", command=login, **button_style)
button_login.grid(row=2, column=0, padx=10, pady=20)

button_signup = tk.Button(frame, text="Sign Up", command=signup, **button_style)
button_signup.grid(row=2, column=1, padx=10, pady=20)

# Run the application
root.mainloop()
