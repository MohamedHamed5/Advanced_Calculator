

# advanced calculator with gui (way 2)

import tkinter as tk
from tkinter import ttk, messagebox
import math

def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else float('inf')
def floor_div(x, y): return x // y if y != 0 else float('inf')
def power(x, y):
    if x == 0 and y == 0:
        raise ValueError("Math error: 0 ** 0 is undefined.")
    elif x == 0 and y < 0:
        raise ZeroDivisionError("Math error: Cannot raise 0 to a negative power.")
    return x ** y

def trig_func(func, angle, mode):
    angle_rad = math.radians(angle) if mode == 'Degrees' else angle
    if func == 'sin': return round(math.sin(angle_rad), 5)
    if func == 'cos': return round(math.cos(angle_rad), 5)
    if func == 'tan':
        if angle % 180 == 90 and mode == 'Degrees':
            raise ValueError("tan(90 + 180k) is undefined.")
        return round(math.tan(angle_rad), 5)

def inv_trig_func(func, val):
    if not -1 <= val <= 1 and func in ['asin', 'acos']:
        raise ValueError(f"{func} is only defined for -1 ≤ x ≤ 1.")
    rad = getattr(math, func)(val)
    return round(math.degrees(rad), 5)

def factorial(n):
    if n < 0 or not float(n).is_integer():
        raise ValueError("Factorial only defined for non-negative integers.")
    return math.factorial(int(n))

def log_func(x, base):
    if x <= 0 or base <= 0 or base == 1:
        raise ValueError("Logarithm undefined for number ≤ 0 or base ≤ 0 or base = 1.")
    return math.log(x, base)

root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("540x540")
root.configure(bg="#222222")
style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", foreground="#ffffff", background="#222222", font=("Segoe UI", 11))
style.configure("TButton", font=("Segoe UI", 11), padding=5)
style.configure("TCombobox", padding=5)

operation_label = ttk.Label(root, text="Select Operation:")
operation_label.pack(pady=(80, 5))

operation_cb = ttk.Combobox(root, width=30, state="readonly")
operation_cb["values"] = (
    "Addition", "Subtraction", "Multiplication", "Power", "Division", "Floor Division",
    "Logarithm", "Factorial", "Square Root",
    "Sine", "Cosine", "Tangent",
    "Asin", "Acos", "Atan"
)
operation_cb.pack()

frame_inputs = tk.Frame(root, bg="#222222")
frame_inputs.pack(pady=(40, 10))

entry1_label = ttk.Label(frame_inputs, text="First Number:")
entry1_label.grid(row=0, column=0, padx=5, sticky="w")
entry1 = ttk.Entry(frame_inputs, width=25)
entry1.grid(row=0, column=1, padx=5)

entry2_label = ttk.Label(frame_inputs, text="Second Number:")
entry2_label.grid(row=1, column=0, padx=5, sticky="w")
entry2 = ttk.Entry(frame_inputs, width=25)
entry2.grid(row=1, column=1, padx=5)

angle_mode_label = ttk.Label(frame_inputs, text="Angle Mode:")
angle_mode_cb = ttk.Combobox(frame_inputs, width=10, state="readonly")
angle_mode_cb["values"] = ("Degrees", "Radians")
angle_mode_cb.current(0)

def update_visibility(event=None):
    op = operation_cb.get().lower()
    entry1_label.grid_remove()
    entry1.grid_remove()
    entry2_label.grid_remove()
    entry2.grid_remove()
    angle_mode_label.grid_remove()
    angle_mode_cb.grid_remove()

    if any(k in op for k in ["addition", "subtraction", "multiplication", "power", "division", "floor", "logarithm"]):
        entry1_label.config(text="First Number:")
        entry2_label.config(text="Second Number:")
        entry1_label.grid(row=0, column=0, sticky="w")
        entry1.grid(row=0, column=1)
        entry2_label.grid(row=1, column=0, sticky="w")
        entry2.grid(row=1, column=1)

    elif any(k in op for k in ["factorial", "square root", "asin", "acos", "atan"]):
        entry1_label.config(text="Value:")
        entry1_label.grid(row=0, column=0, sticky="w")
        entry1.grid(row=0, column=1)

    elif any(k in op for k in ["sine", "cosine", "tangent"]):
        entry1_label.config(text="Angle:")
        entry1_label.grid(row=0, column=0, sticky="w")
        entry1.grid(row=0, column=1)
        angle_mode_label.grid(row=1, column=0, sticky="w")
        angle_mode_cb.grid(row=1, column=1)

operation_cb.bind("<<ComboboxSelected>>", update_visibility)

def calculate():
    try:
        op = operation_cb.get().lower()
        x = entry1.get()
        y = entry2.get()
        result = None

        if "addition" in op or "subtraction" in op or "multiplication" in op or "power" in op or "division" in op or "floor" in op:
            x, y = float(x), float(y)
            funcs = {
                "addition": add,
                "subtraction": subtract,
                "multiplication": multiply,
                "power": power,
                "division": divide,
                "floor": floor_div
            }
            for key in funcs:
                if key in op:
                    result = funcs[key](x, y)
                    break

        elif "logarithm" in op:
            x, y = float(x), float(y)
            result = log_func(x, y)

        elif "factorial" in op:
            result = factorial(float(x))

        elif "square root" in op:
            x = float(x)
            if x < 0:
                raise ValueError("Cannot take square root of negative number.")
            result = math.sqrt(x)

        elif "sine" in op or "cosine" in op or "tangent" in op:
            x = float(x)
            func_map = {"sine": "sin", "cosine": "cos", "tangent": "tan"}
            for key in func_map:
                if key in op:
                    result = trig_func(func_map[key], x, angle_mode_cb.get())
                    break

        elif "asin" in op or "acos" in op or "atan" in op:
            x = float(x)
            for key in ["asin", "acos", "atan"]:
                if key in op:
                    result = inv_trig_func(key, x)
                    break

        messagebox.showinfo("Result", f"Result: {result}")

    except Exception as e:
        messagebox.showerror("Error", str(e))

def clear_all():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    operation_cb.set("")
    angle_mode_cb.current(0)
    update_visibility()

buttons_frame = tk.Frame(root, bg="#222222")
buttons_frame.pack(pady=10)

calc_btn = tk.Button(buttons_frame, text="= Calculate", command=calculate, bg="#4CAF50", fg="white", font=("Segoe UI", 11), width=12)
calc_btn.grid(row=0, column=0, padx=10)

clear_btn = tk.Button(buttons_frame, text="Clear", command=clear_all, bg="#f44336", fg="white", font=("Segoe UI", 11), width=12)
clear_btn.grid(row=0, column=1, padx=10)

update_visibility()
root.mainloop()