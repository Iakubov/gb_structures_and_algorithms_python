# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
import sys


def getsize(*args):
    mem_sum = 0
    for i in args:
        mem_sum += sys.getsizeof(i)
    return print(f'Объекты занимают {mem_sum} байт в памяти')

# Вариант 1

alph = 'abcdefghijklmnopqrstuvwxyz'

first_letter = input('Введите первую букву: ')
second_letter = input('Введите вторую букву: ')

first_num = alph.find(first_letter) + 1
second_num = alph.find(second_letter) + 1

x = second_num - first_num - 1


print("Позиция первой буквы в алфавите: ", first_num)
print("Позиция второй буквы в алфавите: ", second_num)
print("Количество букв между: ", x)


getsize(alph, first_letter, second_letter, first_num, second_num, x)  # Этот вариант занял у меня 259 байт в памяти

# Вариант 2

first_letter = ord(input('Введите первую букву: '))
second_letter = ord(input('Введите вторую букву: '))

first_letter = first_letter - ord('a') + 1
second_letter = second_letter - ord('a') + 1


print("Позиция первой буквы в алфавите: ", first_letter)
print("Позиция второй буквы в алфавите: ", second_letter)
print("Количество букв между: ", abs(first_letter-second_letter)-1)


def getsize(*args):
    mem_sum = 0
    for i in args:
        mem_sum += sys.getsizeof(i)
    return print(f'Объекты занимают {mem_sum} байт в памяти')


getsize(first_letter, second_letter)  # Этот вариант занял у меня 56 байт в памяти

# Вариант под номером 2. Занял наименьшее кол-во памяти.
# Так как в нем используется в разы меньше переменных, чем в первом варианте.

