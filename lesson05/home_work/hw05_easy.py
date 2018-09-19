import os
import time
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
def my_mkdir(prefix ,n):
    n += 1
    try:
        for i in range(1, n):
            i = str(i)
            if not os.path.exists(prefix + i):
                os.mkdir(prefix + i)
            else:
                print(prefix + i + ' папка уже создана')
    except OSError as e:
        print(e)
my_mkdir('dir_', 9)
time.sleep(3)
def my_deletedir(prefix, n):
    n += 1
    try:
        for i in range(1, n):
            i = str(i)
            if os.path.exists(prefix + i):
                os.rmdir(prefix + i)
            else:
                raise ValueError
    except OSError as e:
        print(e)
my_deletedir('dir_', 9)



# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
print([d for d in os.listdir(os.curdir) if os.path.isdir(d)])
# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
