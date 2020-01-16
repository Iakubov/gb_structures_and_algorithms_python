# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

alph = 'abcdefghijklmnopqrstuvwxyz'

letter_num = int(input('Введите номер буквы: '))

letter = alph[letter_num - 1]

print('Ваша буква: ', letter)