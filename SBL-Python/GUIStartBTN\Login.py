"""Code to create a start button"""
import tkinter as tk

# Function to start an action
def start_action():
    label.config(text="Action started!")

# Create the main window
root = tk.Tk()
root.title("Start Button GUI")

# Create a label
label = tk.Label(root, text="Press the Start button to begin an action.")
label.pack(pady=20)

# Create a Start button
start_button = tk.Button(root, text="Start", command=start_action)
start_button.pack()

# Run the Tkinter main loop
root.mainloop()

"""Code to create a login entry field"""
import tkinter as tk
# Function to perform login action
def login():
    username = username_entry.get()
    password = password_entry.get()
    if username == "your_username" and password == "your_password":
        message.config(text="Login successful!")
    else:
        message.config(text="Login failed. Please check your credentials.")

# Create the main window
root = tk.Tk()
root.title("Login and Password GUI")

# Create and place Entry fields for login and password
username_label = tk.Label(root, text="Username:")
username_label.pack(pady=5)
username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack(pady=5)
password_entry = tk.Entry(root, show="*")  # Passwords are hidden
password_entry.pack()

# Create a login button
login_button = tk.Button(root, text="Login", command=login)
login_button.pack(pady=10)

# Create a label to display the login result
message = tk.Label(root, text="")
message.pack()

# Run the Tkinter main loop
root.mainloop()
