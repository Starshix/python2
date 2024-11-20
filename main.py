import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox
import random

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Обработка данных")
        self.geometry("350x600")
        self.create_widgest()

    def generate_file(self):
        """Создает новый текстовый файл с заданным количеством случайных чисел."""
        try:
            count = int(self.number_entry.get())
            filepath = filedialog.asksaveasfilename(defaultextension=".txt")
            if filepath:
                with open(filepath, "w") as file:
                    for _ in range(count):
                        file.write(str(random.randint(1, 100)) + "\n")
                messagebox.showinfo("Успех", f"Файл '{filepath}' создан с {count} случайных чисел.")
        except ValueError as e:
            messagebox.showerror("Ошибка", str(e))


    def read_and_calculate(self, filepath):
        """Читает текстовый файл с числами, вычисляет среднее и выводит результат."""
        try:
            with open(filepath, "r") as file:
                numbers = [int(line) for line in file]
                average = sum(numbers) / len(numbers)
                result_text = f"Содержимое файла:\n" + "\n".join(str(num) for num in numbers) + f"\n\nСреднее значение: {average:.2f}"
                self.result_label.config(text=result_text)
        except ValueError as e:
            messagebox.showerror("Ошибка", str(e))

    def calculate(self, op):
        """Выполняет математическую операцию над двумя числами."""
        try:
            num1 = float(self.a_value.get())
            num2 = float(self.b_value.get())
            if op == "умножить":
                result = num1 * num2
            elif op == "делить":
                result = num1 / num2 if num2 != 0 else "Ошибка: деление на ноль"
            elif op == "сложить":
                result = num1 + num2
            elif op == "вычесть":
                result = num1 - num2
            elif op == "возвести в степень":
                result = num1 ** num2
            self.result_label.config(text=f"Результат: {result}")
        except ValueError as e:
            messagebox.showerror("Ошибка", f"Некорректный ввод: {e}")

    def read_file(self):
        """Открывает диалоговое окно для выбора файла и вычисляет среднее."""
        filepath = filedialog.askopenfilename(defaultextension=".txt")
        if filepath:
            self.read_and_calculate(filepath)


    def multiply(self): 
        self.calculate("умножить")
    def division(self): 
        self.calculate("делить")
    def addition(self): 
        self.calculate("сложить")
    def subtract(self): 
        self.calculate("вычесть")
    def exponentiaton(self): 
        self.calculate("возвести в степень")


    def create_widgest(self):
        style = ttk.Style()
        style.configure("TButton", padding=5, font=("Arial", 10), background="#E0FFFF")

        result_frame = ttk.LabelFrame(self, text="Результат")
        self.result_label = ttk.Label(result_frame, text="", wraplength=300)
        self.result_label.pack(pady=10)
        result_frame.grid(row=20, column=0, columnspan=2, sticky="nsew")

        self.number_label = ttk.Label(self, text="Введите количество чисел:")
        self.number_label.grid(row=0, column=0, padx=5, pady=5)
        self.number_entry = ttk.Entry(self, width=10)
        self.number_entry.grid(row=0, column=1, padx=5, pady=5)

        self.generate_button = ttk.Button(self, text="Создать файл", command=self.generate_file, style="TButton")
        self.generate_button.grid(row=1, column=0, columnspan=2, pady=5, sticky="ew")

        read_button = ttk.Button(self, text="Прочитать файл", command=self.read_file, style="TButton")
        read_button.grid(row=2, column=0, columnspan=2, pady=5, sticky="ew")

        number_value = ttk.Label(self, text="Введите два числа для операций:")
        number_value.grid(row=3, column=0, columnspan=2, pady=5)

        self.a_value = ttk.Entry(self, width=10)
        self.a_value.grid(row=4, column=0, padx=5, pady=5)
        self.b_value = ttk.Entry(self, width=10)
        self.b_value.grid(row=4, column=1, padx=5, pady=5)

        multiply_button = ttk.Button(self, text="Умножить", command=self.multiply, style="TButton")
        multiply_button.grid(row=5, column=0, columnspan=1, pady=5, sticky="ew")
        division_button = ttk.Button(self, text="Делить", command=self.division, style="TButton")
        division_button.grid(row=5, column=1, columnspan=1, pady=5, sticky="ew")

        addition_button = ttk.Button(self, text="Сложить", command=self.addition, style="TButton")
        addition_button.grid(row=6, column=0, columnspan=1, pady=5, sticky="ew")

        subtract_button = ttk.Button(self, text="Вычесть", command=self.subtract, style="TButton")
        subtract_button.grid(row=6, column=1, columnspan=1, pady=5, sticky="ew")

        exponentiation_button = ttk.Button(self, text="Возвести в степень", command=self.exponentiaton, style="TButton")
        exponentiation_button.grid(row=7, column=0, columnspan=2, pady=5, sticky="ew")



app = App()
app.mainloop()
