# На вход программе подаются 3 целых числа и записываются в переменные first, second и third соответственно.
first = int(input("Введите первое целое число:")) # str переводим в int
second = int(input("Введите второе целое число:")) # str переводим в int
third = int(input("Введите третье целое число:")) # str переводим в int
# Ваша задача написать условную конструкцию (из if, elif, else), которая выводит кол-во одинаковых чисел среди 3-х введённых.
if first == second == third:
    print('Вывод: 3')
elif first == second or first == third or second == third:
    print('Вывод 2')
else:
    print('Вывод 0')


# Если все числа равны между собой, то вывести 3
# Если хотя бы 2 из 3 введённых чисел равны между собой, то вывести 2
# Если равных чисел среди 3-х вообще нет, то вывести 0