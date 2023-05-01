import tkinter as tk
# window
window = tk.Tk()
window.title("Login")
# bg and fonts
background_color = "#F5F5F5"
window.configure(bg=background_color)
font = ("Arial", 14)
#  labels
username_label = tk.Label(window, text="Username:", font=font, bg=background_color)
password_label = tk.Label(window, text="Password:", font=font, bg=background_color)
#entry
username_entry = tk.Entry(window, font=font)
password_entry = tk.Entry(window, font=font, show="*")
# buttons
login_button = tk.Button(window, text="Login", font=font, bg="#007BFF", fg="#FFFFFF", width=10)
create_account_button = tk.Button(window, text="Create Account", font=font, bg="#28A745", fg="#FFFFFF", width=15)
#  labels, entry fields, and buttons
username_label.grid(row=0, column=0, padx=10, pady=10)
username_entry.grid(row=0, column=1, padx=10, pady=10)
password_label.grid(row=1, column=0, padx=10, pady=10)
password_entry.grid(row=1, column=1, padx=10, pady=10)
login_button.grid(row=2, column=0, padx=10, pady=10)
create_account_button.grid(row=2, column=1, padx=10, pady=10)
#  create a new account
def create_account():
    username = username_entry.get()
    password = password_entry.get()
 # store the credentials
    with open("accounts.txt", "a") as file:
        file.write(f"{username}:{password}\n")
    print("Account created successfully!")
# check the username and password
def login():
    #  username and password from the entry fields
    username = username_entry.get()
    password = password_entry.get()
# check if the credentials are correct
    with open("accounts.txt", "r") as file:
        for line in file:
            line = line.strip()
            account = line.split(":")
            if account[0] == username and account[1] == password:
                # logged in
                logged_in_window = tk.Toplevel(window)
                logged_in_window.title("Logged In")
                logged_in_label = tk.Label(logged_in_window, text="You are logged in!", font=font)
                logged_in_label.pack(padx=50, pady=50)
                return
   # credentials are incorrect
    error_window = tk.Toplevel(window)
    error_window.title("Error")
    error_label = tk.Label(error_window, text="Incorrect username or password.", font=font)
    error_label.pack(padx=50, pady=50)
# Bind the create account and login buttons to their respective functions
create_account_button.configure(command=create_account)
login_button.configure(command=login)




window.mainloop()
