# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

alph = 'abcdefghijklmnopqrstuvwxyz'

first_letter = input('Введите первую букву: ')
second_letter = input('Введите вторую букву: ')

first_num = alph.find(first_letter) + 1
second_num = alph.find(second_letter) + 1

x = second_num - first_num - 1


print("Позиция первой буквы в алфавите: ", first_num)
print("Позиция второй буквы в алфавите: ", second_num)
print("Количество букв между: ", x)
