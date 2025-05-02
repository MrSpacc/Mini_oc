import os
import sys
import time
import platform
import datetime

# Функция для корректного определения путей в EXE и скрипте
def resource_path(relative_path):
    """Возвращает корректный путь для ресурсов при работе в EXE."""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

# Основной код (без изменений)
print('Ты попал в mini_os от SPACY, и она рада тебя видеть!')
while True:
    try:
        what = int(input('1- калькулятор\n2- вывод текста\n3- насрать текстом\n4- создать директорию\n5- удалить папку\n6- удалить файл\n7- узнать информацию об ОС\n8- нынешние время\n0- выйти\n> '))
        
        if what == 1:
            number1 = int(input('Введите 1 число: '))
            number2 = int(input('Введите 2 число: '))
            kak = int(input('1- сложить\n2- вычесть\n3- умножить\n4- поделить\n> '))
            if kak == 1:
                print('Ответ: ', number1 + number2)
            elif kak == 2:
                print('Ответ: ', number1 - number2)
            elif kak == 3:
                print('Ответ: ', number1 * number2)
            else:
                print('Ответ: ', number1 / number2)
        elif what == 2:
            text = input('Введите текст который хотите вывести: ')
            print('Ваш текст: ', text)
        elif what == 3:
            print('Я насрал, я молодец :-)')
        elif what == 4:
            put_dir = input('Введите путь куда сохранить папку: ')
            name_dir = input('Введите название: ')
            os.chdir(put_dir)
            os.mkdir(name_dir)
            print('Папка создана!')
        elif what == 5:
            what_remove = input('Введите путь к папке: ')
            os.rmdir(what_remove)
            print('Папка удалена!')
        elif what == 6:
            file_remove = input('Введите путь к файлу: ')
            os.remove(file_remove)
            print('Файл удален!')
        elif what == 7:
            print('ОС: SPACY OS (на базе', platform.system(), ')')
            print('Рабочий каталог:', os.getcwd())
        elif what == 8:
            print(datetime.datetime.now())
        elif what == 0:
            print('Выход...')
            time.sleep(1)
            sys.exit()
    except ValueError:
        print('Ошибка: введите число!')
    except Exception as e:
        print('Произошла ошибка:', e)

# Дополнительный код для PyInstaller
if __name__ == '__main__':
    # Проверка, что скрипт запущен как EXE
    if hasattr(sys, '_MEIPASS'):
        print('\nРежим: EXE (собран PyInstaller)')
    else:
        print('\nРежим: Python-скрипт')

    # Пример использования resource_path (если нужны файлы рядом с EXE)
    # data_file = resource_path('data.txt')