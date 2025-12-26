import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

root = tk.Tk()
root.title("Secure Password Generator")
root.state("zoomed")   
root.configure(bg="#1f0329")
root.resizable(False, False)

# ================= Header =================
header = tk.Frame(root, bg="#020617", height=80)
header.pack(fill="x")

tk.Label(header, text="🔐 Password Generator", bg="#020617",
         fg="white", font=("Segoe UI", 22, "bold")).pack(pady=20)

# ================= Main Card =================
card = tk.Frame(root, bg="#020617", bd=0)
card.pack(padx=30, pady=25, fill="both", expand=True)

# Length
tk.Label(card, text="Password Length", fg="#e3e6f2",
         bg="#020617", font=("Segoe UI", 22)).pack(pady=(15, 5))

length_entry = tk.Entry(card, font=("Segoe UI", 16), justify="center", bg="#14081D",
                        fg="white", insertbackground="white", relief="flat")
length_entry.pack(ipady=8, fill="x", padx=20)
length_entry.insert(0, "12")

# ================= Options =================
def make_check(text, var):
    tk.Checkbutton(card, text=text, variable=var, fg="white", bg="#020617",
                   activebackground="#020617", activeforeground="white",
                   selectcolor="#020617", font=("Segoe UI", 16)).pack(anchor="w", padx=40, pady=4)

upper = tk.IntVar(value=1)
lower = tk.IntVar(value=1)
digits = tk.IntVar(value=1)
symbols = tk.IntVar(value=1)
exclude = tk.IntVar()

make_check("Include Uppercase Letters", upper)
make_check("Include Lowercase Letters", lower)
make_check("Include Numbers", digits)
make_check("Include Symbols", symbols)
make_check("Exclude Similar Characters (O, 0, l, 1)", exclude)

# ================= Result =================
result_entry = tk.Entry(card, font=("Segoe UI", 18), justify="center", bg="#03180B",
                        fg="#eae1ed", insertbackground="white", relief="flat")
result_entry.pack(ipady=10, fill="x", padx=20, pady=15)

# ================= Buttons =================
def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showerror("Error", "Password must be at least 4 characters")
            return

        chars = ""
        if upper.get(): chars += string.ascii_uppercase
        if lower.get(): chars += string.ascii_lowercase
        if digits.get(): chars += string.digits
        if symbols.get(): chars += string.punctuation

        if exclude.get():
            for ch in "O0l1":
                chars = chars.replace(ch, "")

        if not chars:
            messagebox.showerror("Error", "Select at least one option!")
            return

        pwd = "".join(random.choice(chars) for _ in range(length))
        result_entry.delete(0, tk.END)
        result_entry.insert(0, pwd)

    except:
        messagebox.showerror("Error", "Enter valid number")

def copy_password():
    if result_entry.get():
        pyperclip.copy(result_entry.get())
        messagebox.showinfo("Copied", "Password copied!")
    else:
        messagebox.showerror("Error", "Generate password first")

tk.Button(card, text="Generate Password", command=generate_password,
          bg="#6C298B", fg="white", font=("Segoe UI", 14, "bold"),
          relief="flat").pack(fill="x", padx=20, pady=(10, 5), ipady=10)

tk.Button(card, text="Copy to Clipboard", command=copy_password,
          bg="#3b0e50", fg="white", font=("Segoe UI", 14, "bold"),
          relief="flat").pack(fill="x", padx=20, pady=(0, 10), ipady=10)

root.mainloop()
