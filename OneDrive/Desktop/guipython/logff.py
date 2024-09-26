import tkinter
from tkinter import messagebox
import os

window = tkinter.Tk()
window.title("Student Login and Sign Up Form")
window.geometry('600x400')
window.configure(bg='#333333')

STUDENT_DATA_FILE = "students_data.txt"

def load_student_data():
    students = {}
    if os.path.exists(STUDENT_DATA_FILE):
        with open(STUDENT_DATA_FILE, 'r') as f:
            for line in f:
                username, password = line.strip().split(',')
                students[username.strip()] = password.strip()
    return students

def save_student_data(username, password):
    with open(STUDENT_DATA_FILE, 'a') as f:
        f.write(f"{username},{password}\n")

students_data = load_student_data()

def sign_up():
    new_username = signup_username_entry.get().strip()
    new_password = signup_password_entry.get().strip()
    
    if new_username and new_password:
        if new_username in students_data:
            messagebox.showerror(title="Error", message="Username already exists. Please log in.")
        else:
            students_data[new_username] = new_password
            save_student_data(new_username, new_password)
            messagebox.showinfo(title="Sign Up Success", message="Sign Up successful! Now, log in to continue.")
            switch_to_login()
    else:
        messagebox.showerror(title="Error", message="Please enter both username and password.")

def login():
    username = login_username_entry.get().strip()
    password = login_password_entry.get().strip()
    
    if username in students_data and students_data[username] == password:
        show_greeting(username)
    else:
        messagebox.showerror(title="Error", message="Invalid login.")

def show_greeting(username):
    clear_window()

    window.geometry("800x600")
    greeting_frame = tkinter.Frame(window, bg='#333333')
    greeting_frame.pack(expand=True, fill="both")

    greeting_label = tkinter.Label(greeting_frame, text=f"Hi {username}!", font=("Arial", 40), fg="#FF3399", bg='#333333')
    greeting_label.pack(pady=20)

    additional_label = tkinter.Label(greeting_frame, text="Welcome to the student portal!", font=("Arial", 20), fg="#FFFFFF", bg='#333333')
    additional_label.pack(pady=10)

    centered_label = tkinter.Label(greeting_frame, text="Enjoy exploring our system.", font=("Arial", 16), fg="#FFFFFF", bg='#333333')
    centered_label.pack(pady=40)

    logout_button = tkinter.Button(greeting_frame, text="Log Out", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=switch_to_login)
    logout_button.pack(pady=30)

def switch_to_login():
    clear_window()
    create_login_frame()

def switch_to_signup():
    clear_window()
    create_signup_frame()

def clear_window():
    for widget in window.winfo_children():
        widget.destroy()

def create_login_frame():
    frame_login = tkinter.Frame(window, bg='#333333')
    
    login_label = tkinter.Label(frame_login, text="Student Login", bg='#333333', fg="#FF3399", font=("Arial", 30))
    login_label.grid(row=0, column=0, columnspan=2, pady=40)

    login_username_label = tkinter.Label(frame_login, text="Username", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
    login_username_label.grid(row=1, column=0)

    global login_username_entry
    login_username_entry = tkinter.Entry(frame_login, font=("Arial", 16))
    login_username_entry.grid(row=1, column=1, pady=20)

    login_password_label = tkinter.Label(frame_login, text="Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
    login_password_label.grid(row=2, column=0)

    global login_password_entry
    login_password_entry = tkinter.Entry(frame_login, show="*", font=("Arial", 16))
    login_password_entry.grid(row=2, column=1, pady=20)

    login_button = tkinter.Button(frame_login, text="Login", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=login)
    login_button.grid(row=3, column=0, columnspan=2, pady=30)

    signup_link = tkinter.Label(frame_login, text="Don't have an account? Sign Up", bg='#333333', fg="#FF3399", cursor="hand2", font=("Arial", 12))
    signup_link.grid(row=4, column=0, columnspan=2)
    signup_link.bind("<Button-1>", lambda e: switch_to_signup())

    frame_login.pack(pady=40)

def create_signup_frame():
    frame_signup = tkinter.Frame(window, bg='#333333')

    signup_label = tkinter.Label(frame_signup, text="Student Sign Up", bg='#333333', fg="#FF3399", font=("Arial", 30))
    signup_label.grid(row=0, column=0, columnspan=2, pady=40)

    signup_username_label = tkinter.Label(frame_signup, text="Username", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
    signup_username_label.grid(row=1, column=0)

    global signup_username_entry
    signup_username_entry = tkinter.Entry(frame_signup, font=("Arial", 16))
    signup_username_entry.grid(row=1, column=1, pady=20)

    signup_password_label = tkinter.Label(frame_signup, text="New Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
    signup_password_label.grid(row=2, column=0)

    global signup_password_entry
    signup_password_entry = tkinter.Entry(frame_signup, show="*", font=("Arial", 16))
    signup_password_entry.grid(row=2, column=1, pady=20)

    signup_button = tkinter.Button(frame_signup, text="Sign Up", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=sign_up)
    signup_button.grid(row=3, column=0, columnspan=2, pady=30)

    login_link = tkinter.Label(frame_signup, text="Already have an account? Log In", bg='#333333', fg="#FF3399", cursor="hand2", font=("Arial", 12))
    login_link.grid(row=4, column=0, columnspan=2)
    login_link.bind("<Button-1>", lambda e: switch_to_login())

    frame_signup.pack(pady=40)

create_login_frame()

window.mainloop()
