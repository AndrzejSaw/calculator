import tkinter as tk
from tkinter import ttk
import math

# Создание главного окна
root = tk.Tk()
root.title("Калькулятор")
root.geometry("400x500")
root.configure(bg='#5b4ea3')

# Настройка стиля
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 14), padding=10)
style.configure("TEntry", font=("Helvetica", 18), padding=10)

# Создание поля для ввода
entry = ttk.Entry(root, width=25, font=("Helvetica", 18))
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

# Функции для обработки нажатий кнопок
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        expression = entry.get()
        if '^' in expression:
            base, exp = map(float, expression.split('^'))
            result = str(base ** exp)
        else:
            result = str(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Ошибка")

def button_sqrt():
    try:
        result = str(math.sqrt(eval(entry.get())))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Ошибка")

def button_square():
    try:
        result = str(eval(entry.get()) ** 2)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Ошибка")

# Создание кнопок
buttons = [
    ('1', 1, 0), ('2', 1, 1), ('3', 1, 2), ('+', 1, 3), ('sqrt', 1, 4),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3), ('x^2', 2, 4),
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('*', 3, 3), ('^', 3, 4),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('/', 4, 3)
]

for (text, row, col) in buttons:
    if text == '=':
        button = ttk.Button(root, text=text, command=button_equal)
    elif text == 'C':
        button = ttk.Button(root, text=text, command=button_clear)
    elif text == 'sqrt':
        button = ttk.Button(root, text=text, command=button_sqrt)
    elif text == 'x^2':
        button = ttk.Button(root, text=text, command=button_square)
    else:
        button = ttk.Button(root, text=text, command=lambda t=text: button_click(t))
    button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

# Настройка размеров колонок и строк
for i in range(5):
    root.columnconfigure(i, weight=1)
for i in range(5):
    root.rowconfigure(i, weight=1)

# Запуск основного цикла программы
root.mainloop()




