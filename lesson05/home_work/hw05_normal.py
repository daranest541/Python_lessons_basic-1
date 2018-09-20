import sys
import os
# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

if __name__ == '__main__' and len(sys.argv) > 1:
    def change_directory():
        try:
            path = input("Введите путь к директории в которую хотите перейти: ")
            os.chdir(path)
            print('Вы перешли в директорию ' + os.getcwd())
        except OSError as e:
            print(e)
            exit()


    def show_current_tree():
        print('Список папок и файлов в директории: ' + os.getcwd() + '\n')
        for file in os.listdir(os.curdir):
            if os.path.isdir(file):
                print("/" + file)
            else:
                print(file)

    def delete_dir():
        try:
            path = input("Введите директорию в которую хотите удалить: ")
            if os.path.exists(path):
                os.rmdir(path)
                print('Директория ' + path + ' успешно удалена')
            else:
                print('Директории ' + path + ' не существует')
        except OSError as e:
            print(e)

    def make_directory():
        try:
            path = input("Введите имя новой директории: ")
            if os.path.exists(path):
                print('Директория ' + path + ' уже существует')
            else:
                os.mkdir(path)
                print('Директория ' + path + ' успешно создана')
        except OSError as e:
            print(e)

    if sys.argv[1] == "cd":
        change_directory()

    if sys.argv[1] == "show_tree":
        show_current_tree()

    if sys.argv[1] == "delete_dir":
        delete_dir()

    if sys.argv[1] == "make_dir":
        make_directory()
else:
    print('Скрипт запущен без аргументов или импортирован как библиотека')