import tkinter as tk
from tkinter import filedialog
import pandas as pd

root = tk.Tk()
root.title("Login")
bg = "#F5F5F5"
root.configure(bg=bg)
font = ("Arial", 14)

user_label = tk.Label(root, text="Username:", font=font, bg=bg)
pwd_label = tk.Label(root, text="Password:", font=font, bg=bg)

user_entry = tk.Entry(root, font=font)
pwd_entry = tk.Entry(root, font=font, show="*")

login_btn = tk.Button(root, text="Login", font=font, bg="#007BFF", fg="#FFFFFF", width=10)
create_btn = tk.Button(root, text="Create Account", font=font, bg="#28A745", fg="#FFFFFF", width=15)

user_label.grid(row=0, column=0, padx=10, pady=10)
user_entry.grid(row=0, column=1, padx=10, pady=10)
pwd_label.grid(row=1, column=0, padx=10, pady=10)
pwd_entry.grid(row=1, column=1, padx=10, pady=10)
login_btn.grid(row=2, column=0, padx=10, pady=10)
create_btn.grid(row=2, column=1, padx=10, pady=10)

def create():
    u = user_entry.get()
    p = pwd_entry.get()
    with open("accounts.txt", "a") as f:
        f.write(f"{u}:{p}\n")
    print("Account created successfully!")

def login():
    u = user_entry.get()
    p = pwd_entry.get()
    with open("accounts.txt", "r") as f:
        for line in f:
            line = line.strip()
            acc = line.split(":")
            if acc[0] == u and acc[1] == p:
                file_path = filedialog.askopenfilename(title="Select .xls File", filetypes=[("Excel Files", "*.xls")])
                if file_path:
                    df = pd.read_excel(file_path)
                    sort_type_var = tk.StringVar()
                    sort_options = ["Ascending", "Descending"]
                    sort_dropdown = tk.OptionMenu(root, sort_type_var, *sort_options)
                    sort_dropdown.grid(row=3, column=0, padx=10, pady=10)
                    sort_btn = tk.Button(root, text="Sort and Save", font=font, bg="#007BFF", fg="#FFFFFF", width=15, command=lambda: sort_and_save(df, sort_type_var.get()))
                    sort_btn.grid(row=3, column=1, padx=10, pady=10)
                return

def sort_and_save(df, sort_type):
    df = df.sort_values(by=[df.columns[0]], ascending=(sort_type == "Ascending"))
    save_path = filedialog.asksaveasfilename(title="Save .xls File", filetypes=[("Excel Files", "*.xls")])
    if save_path:
        df.to_excel(save_path, index=False)
        print("File saved successfully!")

create_btn.configure(command=create)
login_btn.configure(command=login)

root.mainloop()
