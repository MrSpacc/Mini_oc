# -*- coding: utf-8 -*-
import os
import sys
import time
import platform
import datetime
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, filedialog
import shutil

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

class MiniOSApp:
    def __init__(self, root):
        self.root = root
        root.title("💻 Mini_OS от SPACY")
        root.geometry("540x540")
        root.resizable(False, False)
        self.center_window(root)

        # Настройка иконки
        try:
            icon_path = resource_path("icon.ico")
            root.iconbitmap(icon_path)
        except Exception as e:
            print("⚠️ Не удалось загрузить иконку:", e)

        # Тёмная тема
        style = ttk.Style()
        style.theme_use("default")

        bg = "#1e1e1e"
        fg = "#ffffff"
        accent = "#0a84ff"

        root.configure(bg=bg)
        style.configure("TLabel", background=bg, foreground=fg, font=("Segoe UI", 11))
        style.configure("TButton", background=accent, foreground=fg, font=("Segoe UI", 10), padding=6)
        style.map("TButton", background=[("active", "#005bbb")])
        style.configure("CustomListbox.TFrame", background=bg)

        self.label = ttk.Label(root, text="👋 Добро пожаловать в mini_os от SPACY!", font=("Segoe UI", 13, "bold"))
        self.label.pack(pady=15)

        self.list_frame = ttk.Frame(root, style="CustomListbox.TFrame")
        self.list_frame.pack(pady=10)

        self.actions = [
            "1 - Калькулятор",
            "2 - Вывод текста",
            "3 - Насрать текстом",
            "4 - Создать директорию",
            "5 - Удалить папку",
            "6 - Удалить файл",
            "7 - Информация об ОС",
            "8 - Текущее время",
            "0 - Выйти"
        ]

        self.listbox = tk.Listbox(self.list_frame, height=10, width=42, font=("Segoe UI", 10),
                                  bg=bg, fg=fg, highlightthickness=0, selectbackground=accent)
        for item in self.actions:
            self.listbox.insert(tk.END, item)
        self.listbox.pack()

        self.button = ttk.Button(root, text="🚀 Выполнить", command=self.execute_action)
        self.button.pack(pady=20)

        self.status = ttk.Label(root, text="Версия: GUI 1.0", foreground="#888888")
        self.status.pack()

    def center_window(self, root):
        w = 540
        h = 540
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        x = (ws // 2) - (w // 2)
        y = (hs // 2) - (h // 2)
        root.geometry(f'{w}x{h}+{x}+{y}')

    def execute_action(self):
        try:
            selection = self.listbox.curselection()
            if not selection:
                messagebox.showwarning("Выбор", "Пожалуйста, выберите действие.")
                return
            choice = selection[0]

            if choice == 0:
                number1 = simpledialog.askfloat("Калькулятор", "Введите первое число:")
                number2 = simpledialog.askfloat("Калькулятор", "Введите второе число:")
                operation = simpledialog.askinteger("Калькулятор", "1 - сложить\n2 - вычесть\n3 - умножить\n4 - поделить")
                if operation == 1:
                    result = number1 + number2
                elif operation == 2:
                    result = number1 - number2
                elif operation == 3:
                    result = number1 * number2
                elif operation == 4:
                    if number2 == 0:
                        raise ZeroDivisionError
                    result = number1 / number2
                else:
                    raise ValueError("Неизвестная операция")
                messagebox.showinfo("Результат", f"Ответ: {result}")

            elif choice == 1:
                text = simpledialog.askstring("Вывод текста", "Введите текст:")
                messagebox.showinfo("Результат", f"Ваш текст: {text}")

            elif choice == 2:
                messagebox.showinfo("Насрал", "💩 Я насрал, я молодец :-)")

            elif choice == 3:
                directory = filedialog.askdirectory(title="Выберите путь для папки")
                if not directory:
                    return
                name = simpledialog.askstring("Имя папки", "Введите имя новой папки:")
                full_path = os.path.join(directory, name)
                os.mkdir(full_path)
                messagebox.showinfo("Успех", f"Папка создана:\n{full_path}")

            elif choice == 4:
                folder = filedialog.askdirectory(title="Выберите папку для удаления")
                if not folder or not os.path.exists(folder):
                    messagebox.showerror("Ошибка", "Папка не найдена.")
                    return
                if messagebox.askyesno("Удаление", f"Удалить папку и всё содержимое?\n{folder}"):
                    shutil.rmtree(folder)
                    messagebox.showinfo("Успех", "Папка удалена.")

            elif choice == 5:
                file = filedialog.askopenfilename(title="Выберите файл для удаления")
                if not file or not os.path.exists(file):
                    messagebox.showerror("Ошибка", "Файл не найден.")
                    return
                if messagebox.askyesno("Удаление", f"Удалить файл?\n{file}"):
                    os.remove(file)
                    messagebox.showinfo("Успех", "Файл удалён.")

            elif choice == 6:
                info = f"ОС: SPACY OS (на базе {platform.system()})\nТекущий каталог: {os.getcwd()}"
                messagebox.showinfo("Информация об ОС", info)

            elif choice == 7:
                now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                messagebox.showinfo("Время", f"🕒 Текущее время: {now}")

            elif choice == 8:
                self.root.quit()

        except ZeroDivisionError:
            messagebox.showerror("Ошибка", "Деление на ноль!")
        except FileNotFoundError:
            messagebox.showerror("Ошибка", "Файл или папка не найдены!")
        except PermissionError:
            messagebox.showerror("Ошибка", "Нет доступа. Попробуйте запустить от имени администратора.")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")

if __name__ == '__main__':
    root = tk.Tk()
    app = MiniOSApp(root)
    root.mainloop()
