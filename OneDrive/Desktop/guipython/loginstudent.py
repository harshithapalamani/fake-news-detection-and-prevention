import tkinter as tk
from tkinter import messagebox

# Dictionary to store registered students
students_db = {}

# Function for signup
def signup():
    username = signup_username_entry.get()
    password = signup_password_entry.get()
    confirm_password = signup_confirm_password_entry.get()
    
    if username == "" or password == "" or confirm_password == "":
        messagebox.showerror("Error", "All fields are required!")
    elif password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match!")
    elif username in students_db:
        messagebox.showerror("Error", "Username already exists!")
    else:
        students_db[username] = password
        messagebox.showinfo("Success", "Signup successful!")
        switch_to_login()

# Function for login
def login():
    username = login_username_entry.get()
    password = login_password_entry.get()

    if username in students_db and students_db[username] == password:
        messagebox.showinfo("Success", f"Welcome {username}!")
        show_welcome_screen(username)
    else:
        messagebox.showerror("Error", "Invalid username or password!")

# Function to switch to login frame
def switch_to_login():
    signup_frame.pack_forget()
    login_frame.pack(fill='both', expand=True)

# Function to switch to signup frame
def switch_to_signup():
    login_frame.pack_forget()
    signup_frame.pack(fill='both', expand=True)

# Function to show welcome screen after login
def show_welcome_screen(username):
    login_frame.pack_forget()
    signup_frame.pack_forget()
    welcome_frame.pack(fill='both', expand=True)
    welcome_label.config(text=f"Hi {username}, welcome to the student portal!")
    animate_text("Welcome to the Student Portal!", 0)

# Function to animate text
def animate_text(text, index):
    if index < len(text):
        animated_label.config(text=animated_label.cget("text") + text[index])
        window.after(100, animate_text, text, index + 1)  # 100 ms delay between each character

# Main window
window = tk.Tk()
window.title("Student Login Form")
window.geometry('400x500')
window.configure(bg='#333333')

# Frames for login, signup, and welcome screen
login_frame = tk.Frame(window, bg='#333333')
signup_frame = tk.Frame(window, bg='#333333')
welcome_frame = tk.Frame(window, bg='#333333')

# Login Frame Widgets
login_label = tk.Label(login_frame, text="Login", bg='#333333', fg="#FF3399", font=("Arial", 30))
login_label.pack(pady=20)

login_username_label = tk.Label(login_frame, text="Username", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
login_username_label.pack(pady=10)
login_username_entry = tk.Entry(login_frame, font=("Arial", 16))
login_username_entry.pack(pady=10)

login_password_label = tk.Label(login_frame, text="Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
login_password_label.pack(pady=10)
login_password_entry = tk.Entry(login_frame, show="*", font=("Arial", 16))
login_password_entry.pack(pady=10)

login_button = tk.Button(login_frame, text="Login", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=login)
login_button.pack(pady=20)

signup_button = tk.Button(login_frame, text="Signup", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=switch_to_signup)
signup_button.pack(pady=20)

# Signup Frame Widgets
signup_label = tk.Label(signup_frame, text="Signup", bg='#333333', fg="#FF3399", font=("Arial", 30))
signup_label.pack(pady=20)

signup_username_label = tk.Label(signup_frame, text="Username", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
signup_username_label.pack(pady=10)
signup_username_entry = tk.Entry(signup_frame, font=("Arial", 16))
signup_username_entry.pack(pady=10)

signup_password_label = tk.Label(signup_frame, text="Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
signup_password_label.pack(pady=10)
signup_password_entry = tk.Entry(signup_frame, show="*", font=("Arial", 16))
signup_password_entry.pack(pady=10)

signup_confirm_password_label = tk.Label(signup_frame, text="Confirm Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
signup_confirm_password_label.pack(pady=10)
signup_confirm_password_entry = tk.Entry(signup_frame, show="*", font=("Arial", 16))
signup_confirm_password_entry.pack(pady=10)

signup_submit_button = tk.Button(signup_frame, text="Signup", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=signup)
signup_submit_button.pack(pady=20)

back_to_login_button = tk.Button(signup_frame, text="Back to Login", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=switch_to_login)
back_to_login_button.pack(pady=20)

# Welcome Screen Widgets
welcome_label = tk.Label(welcome_frame, text="", bg='#333333', fg="#FFFFFF", font=("Arial", 24))
welcome_label.pack(pady=20)

animated_label = tk.Label(welcome_frame, text="", bg='#333333', fg="#FF3399", font=("Arial", 20))
animated_label.pack(pady=20)

# Initially show login frame
login_frame.pack(fill='both', expand=True)

# Start the application
window.mainloop()
