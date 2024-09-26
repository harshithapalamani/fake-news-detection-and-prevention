import tkinter
from tkinter import messagebox
import os
import re

window = tkinter.Tk()
window.title("Student Login and Sign Up Form")
window.geometry('600x400')

STUDENT_DATA_FILE = "students_data.txt"

def load_student_data():
    students = {}
    if os.path.exists(STUDENT_DATA_FILE):
        with open(STUDENT_DATA_FILE, 'r') as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) == 4:  # Ensure there are exactly 4 parts
                    username, password, question, answer = parts
                    students[username.strip()] = {
                        'password': password.strip(),
                        'question': question.strip(),
                        'answer': answer.strip()
                    }
                else:
                    print(f"Skipping invalid line: {line.strip()}")
    return students

def save_student_data(username, password, question, answer):
    with open(STUDENT_DATA_FILE, 'a') as f:
        f.write(f"{username},{password},{question},{answer}\n")

students_data = load_student_data()

def is_valid_email(email):
    # Simple regex for email validation
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

def is_valid_password(password):
    # Check for password constraints
    if (len(password) < 8 or 
        not re.search(r"[A-Z]", password) or 
        not re.search(r"[a-z]", password) or 
        not re.search(r"[0-9]", password) or 
        not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)):  # Modify the special characters as needed
        return False
    return True

def sign_up():
    new_username = signup_username_entry.get().strip()
    new_password = signup_password_entry.get().strip()
    security_question = signup_question_entry.get().strip()
    security_answer = signup_answer_entry.get().strip()

    if new_username and new_password and security_question and security_answer:
        if not is_valid_email(new_username):
            messagebox.showerror(title="Error", message="Please use a valid email address as your username.")
            return

        if not is_valid_password(new_password):
            messagebox.showerror(title="Error", message="Password must be at least 8 characters long, contain an uppercase letter, a lowercase letter, a digit, and a special character.")
            return

        if new_username in students_data:
            messagebox.showerror(title="Error", message="Username already exists. Please log in.")
        else:
            students_data[new_username] = {
                'password': new_password,
                'question': security_question,
                'answer': security_answer
            }
            save_student_data(new_username, new_password, security_question, security_answer)
            messagebox.showinfo(title="Sign Up Success", message="Sign Up successful! Now, log in to continue.")
            switch_to_login()
    else:
        messagebox.showerror(title="Error", message="Please fill in all fields.")

def login():
    username = login_username_entry.get().strip()
    password = login_password_entry.get().strip()

    if username in students_data:
        if students_data[username]['password'] == password:
            show_greeting(username)
        else:
            messagebox.showerror(title="Error", message="Incorrect password. Please try again.")
    else:
        messagebox.showerror(title="Error", message="Username not found. Please provide your email as the username.")

def show_greeting(username):
    clear_window()

    greeting_frame = tkinter.Frame(window)
    greeting_frame.pack(expand=True, fill="both")

    greeting_label = tkinter.Label(greeting_frame, text=f"Hi {username}!", font=("Arial", 40))
    greeting_label.pack(pady=20)

    additional_label = tkinter.Label(greeting_frame, text="Welcome to the student portal!", font=("Arial", 20))
    additional_label.pack(pady=10)

    centered_label = tkinter.Label(greeting_frame, text="Enjoy exploring our system.", font=("Arial", 16))
    centered_label.pack(pady=40)

    logout_button = tkinter.Button(greeting_frame, text="Log Out", font=("Arial", 16), command=switch_to_login)
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
    frame_login = tkinter.Frame(window)
    
    login_label = tkinter.Label(frame_login, text="Student Login", font=("Arial", 30))
    login_label.grid(row=0, column=0, columnspan=2, pady=40)

    login_username_label = tkinter.Label(frame_login, text="Username (Email)", font=("Arial", 16))
    login_username_label.grid(row=1, column=0)

    global login_username_entry
    login_username_entry = tkinter.Entry(frame_login, font=("Arial", 16))
    login_username_entry.grid(row=1, column=1, pady=20)

    login_password_label = tkinter.Label(frame_login, text="Password", font=("Arial", 16))
    login_password_label.grid(row=2, column=0)

    global login_password_entry
    login_password_entry = tkinter.Entry(frame_login, show="*", font=("Arial", 16))
    login_password_entry.grid(row=2, column=1, pady=20)

    login_button = tkinter.Button(frame_login, text="Login", font=("Arial", 16), command=login)
    login_button.grid(row=3, column=0, columnspan=2, pady=30)

    signup_link = tkinter.Label(frame_login, text="Don't have an account? Sign Up", font=("Arial", 12))
    signup_link.grid(row=4, column=0, columnspan=2)
    signup_link.bind("<Button-1>", lambda e: switch_to_signup())

    forgot_password_link = tkinter.Label(frame_login, text="Forgot Password?", font=("Arial", 12))
    forgot_password_link.grid(row=5, column=0, columnspan=2)
    forgot_password_link.bind("<Button-1>", lambda e: show_forgot_password_frame())

    frame_login.pack(pady=40)

def create_signup_frame():
    frame_signup = tkinter.Frame(window)

    signup_label = tkinter.Label(frame_signup, text="Student Sign Up", font=("Arial", 30))
    signup_label.grid(row=0, column=0, columnspan=2, pady=40)

    signup_username_label = tkinter.Label(frame_signup, text="Username (Email)", font=("Arial", 16))
    signup_username_label.grid(row=1, column=0)

    global signup_username_entry
    signup_username_entry = tkinter.Entry(frame_signup, font=("Arial", 16))
    signup_username_entry.grid(row=1, column=1, pady=20)

    signup_password_label = tkinter.Label(frame_signup, text="New Password", font=("Arial", 16))
    signup_password_label.grid(row=2, column=0)

    global signup_password_entry
    signup_password_entry = tkinter.Entry(frame_signup, show="*", font=("Arial", 16))
    signup_password_entry.grid(row=2, column=1, pady=20)

    signup_question_label = tkinter.Label(frame_signup, text="Security Question", font=("Arial", 16))
    signup_question_label.grid(row=3, column=0)

    global signup_question_entry
    signup_question_entry = tkinter.Entry(frame_signup, font=("Arial", 16))
    signup_question_entry.grid(row=3, column=1, pady=20)

    signup_answer_label = tkinter.Label(frame_signup, text="Security Answer", font=("Arial", 16))
    signup_answer_label.grid(row=4, column=0)

    global signup_answer_entry
    signup_answer_entry = tkinter.Entry(frame_signup, font=("Arial", 16))
    signup_answer_entry.grid(row=4, column=1, pady=20)

    signup_button = tkinter.Button(frame_signup, text="Sign Up", font=("Arial", 16), command=sign_up)
    signup_button.grid(row=5, column=0, columnspan=2, pady=30)

    login_link = tkinter.Label(frame_signup, text="Already have an account? Log In", font=("Arial", 12))
    login_link.grid(row=6, column=0, columnspan=2)
    login_link.bind("<Button-1>", lambda e: switch_to_login())

    frame_signup.pack(pady=40)

def show_forgot_password_frame():
    clear_window()
    
    forgot_username_label = tkinter.Label(window, text="Username (Email)", font=("Arial", 16))
    forgot_username_label.pack()

    global forgot_username_entry
    forgot_username_entry = tkinter.Entry(window, font=("Arial", 16))
    forgot_username_entry.pack(pady=10)

    submit_username_button = tkinter.Button(window, text="Submit", command=forgot_password)
    submit_username_button.pack(pady=10)

    global forgot_question_label
    forgot_question_label = tkinter.Label(window, text="", font=("Arial", 16))
    forgot_question_label.pack(pady=10)

    global answer_entry
    answer_entry = tkinter.Entry(window, font=("Arial", 16))
    answer_entry.pack(pady=10)

    global submit_answer_button
    submit_answer_button = tkinter.Button(window, text="", command=submit_answer)
    submit_answer_button.pack(pady=10)

def forgot_password():
    username = forgot_username_entry.get().strip()

    if username in students_data:
        security_question = students_data[username]['question']
        forgot_question_label.config(text=security_question)
        submit_answer_button.config(text="Submit Answer")
    else:
        messagebox.showerror(title="Error", message="Username not found. Please provide your email as the username.")

def submit_answer():
    username = forgot_username_entry.get().strip()
    answer = answer_entry.get().strip()

    if username in students_data:
        if students_data[username]['answer'] == answer:
            messagebox.showinfo(title="Success", message=f"Your password is: {students_data[username]['password']}")
            switch_to_login()  # Switch back to the login page after retrieving the password
        else:
            messagebox.showerror(title="Error", message="Incorrect answer to the security question.")
    else:
        messagebox.showerror(title="Error", message="Username not found. Please provide your email as the username.")

create_login_frame()
window.mainloop()
