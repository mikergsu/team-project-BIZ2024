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
root.geometry("400x550")
root.resizable(False, False)
root.configure(bg="#2E2E2E")

# Поле ввода
entry = tk.Entry(root, width=16, font=("Segoe UI", 32), justify="right", bd=0, bg="#1E1E1E", fg="#FFFFFF", insertbackground="white")
entry.grid(row=0, column=0, columnspan=4, pady=(30, 20), padx=20, ipady=15)

# Цвета кнопок
btn_bg = "#3C3F41"
btn_fg = "#FFFFFF"
btn_active_bg = "#575A5C"
op_bg = "#FF9500"
op_fg = "#FFFFFF"
op_active_bg = "#CC7A00"
clear_bg = "#D64545"
clear_active_bg = "#A53030"

# Функция создания кнопок с дизайном
def create_button(text, row, col, width=5, height=2, command=None, bg=btn_bg, fg=btn_fg, activebg=btn_active_bg, colspan=1):
    btn = tk.Button(root, text=text, command=command, bg=bg, fg=fg, activebackground=activebg,
                    font=("Segoe UI", 20, "bold"), bd=0, relief="flat",
                    width=width, height=height, cursor="hand2")
    btn.grid(row=row, column=col, columnspan=colspan, padx=8, pady=8, sticky="nsew")
    return btn

# Кнопки с их расположением
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("+", 4, 2), ("=", 4, 3),
]

for (text, row, col) in buttons:
    if text in {"+", "-", "*", "/"}:
        create_button(text, row, col, bg=op_bg, fg=op_fg, activebg=op_active_bg, command=lambda t=text: click(t))
    elif text == "=":
        create_button(text, row, col, bg=op_bg, fg=op_fg, activebg=op_active_bg, command=calculate)
    else:
        create_button(text, row, col, command=lambda t=text: click(t))

# Кнопка очистки на всю ширину снизу
create_button("C", 5, 0, width=22, bg=clear_bg, fg="#FFFFFF", activebg=clear_active_bg, command=clear, colspan=4)

# Заставляем строки и колонки растягиваться одинаково
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

root.mainloop()
