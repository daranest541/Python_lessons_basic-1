import random
# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
random_list = random.sample(range(1, 20), 10)
print(random_list)
l2 = [i ** 2 for i in random_list]
print(l2)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

def fruit_to_list(fruit_str):
    try:
        if ',' in fruit_str:
            return [f.strip() for f in fruit_str.split(',')]
        else:
            raise ValueError
    except ValueError:
        print('некоректный ввод данных')
        exit()


fruit1_str = input('Введите первый список фруктов через запятую: ')
#fruit1_str = 'apple, banana, qiwi, orange'
l1 = fruit_to_list(fruit1_str)
fruit2_str = input('Введите второй список фруктов через запятую: ')
#fruit1_str = 'banana, orange, pear'
l2 = fruit_to_list(fruit1_str)

res_list = [f for f in l1 if f in l2]
print(res_list)


# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

random_list2 = random.sample(range(-100, 100), 10)
print(random_list2)
new_list = [i for i in random_list2 if (i % 3 == 0) and i > 0 and i % 4 != 0]
print(new_list)