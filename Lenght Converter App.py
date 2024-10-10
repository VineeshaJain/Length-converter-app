import tkinter as tk
from tkinter import messagebox

def convert_to_cm():
    try:
        inches = float(entry.get())
        centimeters = inches * 2.54
        result_label.config(text=f"{inches} inches is {centimeters:.2f} cm")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number.")

window = tk.Tk()
window.title("Inches to Centimeters Converter")
window.geometry("300x150")

entry_label = tk.Label(window, text="Enter length in inches:")
entry_label.pack(pady=5)

entry = tk.Entry(window)
entry.pack(pady=5)

convert_button = tk.Button(window, text="Convert", command=convert_to_cm)
convert_button.pack(pady=10)

result_label = tk.Label(window, text="")
result_label.pack(pady=5)

window.mainloop()