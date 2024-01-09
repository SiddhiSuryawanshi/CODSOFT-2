import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                messagebox.showerror("Error", "Division by zero is not allowed.")
                return
        else:
            messagebox.showerror("Error", "Invalid operation.")
            return

        result_label.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Styling
window.geometry("400x250")
window.resizable(False, False)
window.configure(bg="#f0f0f0")

# Fonts
entry_font = ("Arial", 14)
button_font = ("Arial", 12, "bold")

# Create and place widgets
entry_num1 = tk.Entry(window, width=10, font=entry_font)
entry_num1.grid(row=0, column=0, padx=10, pady=10)

operation_var = tk.StringVar()
operation_choices = ['+', '-', '*', '/']
operation_menu = tk.OptionMenu(window, operation_var, *operation_choices)
operation_menu.config(font=button_font)
operation_menu.grid(row=0, column=1, padx=10, pady=10)

entry_num2 = tk.Entry(window, width=10, font=entry_font)
entry_num2.grid(row=0, column=2, padx=10, pady=10)

calculate_button = tk.Button(window, text="Calculate", command=calculate, font=button_font, bg="#4caf50", fg="white")
calculate_button.grid(row=1, column=0, columnspan=3, pady=10)

result_label = tk.Label(window, text="Result: ", font=("Arial", 14), bg="#f0f0f0")
result_label.grid(row=2, column=0, columnspan=3)

# Run the main loop
window.mainloop()
