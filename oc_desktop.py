# -*- coding: utf-8 -*-
import os
import sys
import platform
import datetime
import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog

def resource_path(relative_path):
    """Корректный путь к файлу для PyInstaller"""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

class MiniOSApp:
    def __init__(self, root):
        self.root = root
        self.setup_window()
        self.setup_ui()

    def setup_window(self):
        self.root.title("SPACY OS")
        self.root.geometry("400x500")
        try:
            self.root.iconbitmap(resource_path("logo.ico"))
        except:
            print("Иконка не найдена, продолжаем без неё.")

    def setup_ui(self):
        # Заголовок
        title = tk.Label(self.root, text="SPACY OS", font=("Arial", 20, "bold"), fg="#3a5a9f")
        title.pack(pady=10)

        # Кнопки
        buttons = [
            ("Калькулятор", self.calc),
            ("Вывод текста", self.print_text),
            ("Создать папку", self.create_dir),
            ("Удалить папку", self.delete_dir),
            ("Удалить файл", self.delete_file),
            ("Информация об ОС", self.sys_info),
            ("Текущее время", self.current_time),
            ("Выход", self.exit_app),
        ]

        for text, command in buttons:
            tk.Button(
                self.root, text=text, command=command,
                font=("Arial", 11), bg="#4a6baf", fg="white",
                activebackground="#3a5a9f", activeforeground="white",
                relief="flat", bd=0, height=2
            ).pack(pady=5, fill="x", padx=20)

    # ==== Функции ====

    def calc(self):
        print("Калькулятор вызван.")
        try:
            n1 = simpledialog.askfloat("Калькулятор", "Первое число:", parent=self.root)
            if n1 is None:
                print("Отменено.")
                return

            n2 = simpledialog.askfloat("Калькулятор", "Второе число:", parent=self.root)
            if n2 is None:
                print("Отменено.")
                return

            op = simpledialog.askinteger("Операция", "1: +\n2: -\n3: *\n4: /", parent=self.root)
            if op is None:
                print("Отменено.")
                return

            if op == 1:
                result = n1 + n2
            elif op == 2:
                result = n1 - n2
            elif op == 3:
                result = n1 * n2
            elif op == 4:
                if n2 == 0:
                    raise ZeroDivisionError("Деление на ноль")
                result = n1 / n2
            else:
                raise ValueError("Неверная операция")

            messagebox.showinfo("Результат", f"Ответ: {result}", parent=self.root)
        except Exception as e:
            print("Ошибка:", e)
            messagebox.showerror("Ошибка", f"Ошибка: {e}", parent=self.root)

    def print_text(self):
        text = simpledialog.askstring("Вывод текста", "Введите текст:", parent=self.root)
        if text:
            messagebox.showinfo("Результат", f"Вы ввели: {text}", parent=self.root)

    def create_dir(self):
        path = filedialog.askdirectory(title="Выберите место для папки", parent=self.root)
        if not path:
            return

        name = simpledialog.askstring("Создать папку", "Имя папки:", parent=self.root)
        if not name:
            return

        try:
            os.mkdir(os.path.join(path, name))
            messagebox.showinfo("Успех", "Папка создана", parent=self.root)
        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка создания: {e}", parent=self.root)

    def delete_dir(self):
        path = filedialog.askdirectory(title="Выберите папку для удаления", parent=self.root)
        if not path:
            return

        if messagebox.askyesno("Подтверждение", f"Удалить папку?\n{path}", parent=self.root):
            try:
                os.rmdir(path)
                messagebox.showinfo("Успех", "Папка удалена", parent=self.root)
            except Exception as e:
                messagebox.showerror("Ошибка", f"Ошибка удаления: {e}", parent=self.root)

    def delete_file(self):
        path = filedialog.askopenfilename(title="Выберите файл для удаления", parent=self.root)
        if not path:
            return

        if messagebox.askyesno("Подтверждение", f"Удалить файл?\n{path}", parent=self.root):
            try:
                os.remove(path)
                messagebox.showinfo("Успех", "Файл удалён", parent=self.root)
            except Exception as e:
                messagebox.showerror("Ошибка", f"Ошибка удаления файла: {e}", parent=self.root)

    def sys_info(self):
        """Отображение информации об ОС с логотипом"""
        info_window = tk.Toplevel(self.root)
        info_window.title("Информация о приложении")
        info_window.geometry("300x400")
        
        try:
            logo_path = resource_path("logo.ico")  # Используем путь к иконке
            logo_image = tk.PhotoImage(file=logo_path)
            logo_label = tk.Label(info_window, image=logo_image)
            logo_label.image = logo_image  # Сохраняем ссылку на изображение
            logo_label.pack(pady=10)
        except Exception as e:
            print(f"Ошибка при загрузке логотипа: {e}")

        # Информация о системе
        info = f"Система: {platform.system()}\n" \
               f"Версия: {platform.version()}\n" \
               f"Каталог: {os.getcwd()}"
        
        info_label = tk.Label(info_window, text=info, font=("Arial", 10), justify="left")
        info_label.pack(pady=10)

    def current_time(self):
        now = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        messagebox.showinfo("Текущее время", f"Сейчас: {now}", parent=self.root)

    def exit_app(self):
        if messagebox.askyesno("Выход", "Закрыть приложение?", parent=self.root):
            self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = MiniOSApp(root)
    root.mainloop()
