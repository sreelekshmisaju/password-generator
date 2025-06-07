import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip
import math

# 🔐 Password Generator Function
def generate():
    try:
        length = int(entry_length.get())
        if length <= 0:
            raise ValueError

        characters = ""
        if var_upper.get():
            characters += string.ascii_uppercase
        if var_lower.get():
            characters += string.ascii_lowercase
        if var_digits.get():
            characters += string.digits
        if var_special.get():
            characters += string.punctuation

        if not characters:
            messagebox.showerror("Error", "Select at least one character type.")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        result_entry.delete(0, tk.END)
        result_entry.insert(0, password)

        # 📋 Copy to clipboard
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

        # 🧮 Check password strength
        pool_size = len(set(characters))
        strength = calculate_entropy(password, pool_size)
        label_strength.config(text=f"Strength: {strength}")

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

# 📁 Save password to file
def save_password():
    password = result_entry.get()
    if password:
        with open("saved_passwords.txt", "a") as file:
            file.write(password + "\n")
        messagebox.showinfo("Saved", "Password saved to 'saved_passwords.txt'")
    else:
        messagebox.showerror("Error", "No password to save.")

# 🔐 Entropy-based strength check
def calculate_entropy(password, pool_size):
    entropy = len(password) * math.log2(pool_size)
    if entropy < 28:
        return "Very Weak"
    elif entropy < 36:
        return "Weak"
    elif entropy < 60:
        return "Reasonable"
    elif entropy < 128:
        return "Strong"
    else:
        return "Very Strong"

# 🌙 Toggle Dark Mode
def toggle_dark_mode():
    if dark_mode.get():
        root.configure(bg="#1e1e1e")
        for widget in root.winfo_children():
            try:
                widget.configure(bg="#1e1e1e", fg="white")
            except:
                pass
    else:
        root.configure(bg="SystemButtonFace")
        for widget in root.winfo_children():
            try:
                widget.configure(bg="SystemButtonFace", fg="black")
            except:
                pass

# 🧱 GUI Layout
root = tk.Tk()
root.title("🔐 Password Generator")
root.geometry("300x400")

tk.Label(root, text="Password Length:").pack()
entry_length = tk.Entry(root)
entry_length.pack()

var_upper = tk.BooleanVar(value=True)
var_lower = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_special = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Uppercase", variable=var_upper).pack()
tk.Checkbutton(root, text="Include Lowercase", variable=var_lower).pack()
tk.Checkbutton(root, text="Include Digits", variable=var_digits).pack()
tk.Checkbutton(root, text="Include Special Characters", variable=var_special).pack()

tk.Button(root, text="Generate Password", command=generate).pack(pady=10)

result_entry = tk.Entry(root, width=30)
result_entry.pack()

tk.Button(root, text="Save Password", command=save_password).pack(pady=5)

label_strength = tk.Label(root, text="Strength: ")
label_strength.pack()

# Dark Mode Toggle
dark_mode = tk.BooleanVar()
tk.Checkbutton(root, text="Dark Mode", variable=dark_mode, command=toggle_dark_mode).pack(pady=5)

root.mainloop()
