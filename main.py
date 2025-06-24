#Калькулятор
import tkinter as tk
from tkinter import messagebox


def click(symbol):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + symbol)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except ZeroDivisionError:
        messagebox.showerror("Ошибка", "Деление на ноль невозможно.")
        clear()
    except Exception:
        messagebox.showerror("Ошибка", "Неверное выражение.")
        clear()

# Создание основного окна
root = tk.Tk()
root.title("Калькулятор")
root.geometry("600x600")
root.resizable(False, False)

# Поле ввода
entry = tk.Entry(root, width=16, font=("Arial", 24), justify="right", bd=5)
entry.grid(row=0, column=0, columnspan=4, pady=10)

# Кнопки
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("+", 4, 2), ("=", 4, 3),
    ("C", 5, 0)
]

for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=calculate)
    elif text == "C":
        btn = tk.Button(root, text=text, width=22, height=2, font=("Arial", 18), command=clear)
        btn.grid(row=row, column=col, columnspan=4, pady=10)
        continue
    else:
        btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=lambda t=text: click(t))
    btn.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()
