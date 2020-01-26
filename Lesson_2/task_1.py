# Напишите программу, доказывающую или проверяющую,
#  что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n — любое натуральное число.
# https://drive.google.com/file/d/1OR58czGhjEdGSdMBXpH3Bf83UOoYDgpE/view?usp=sharing

n = int(input('Введите число: '))
a = 0
for i in range(1, n+1):
    a += i
m = n * (n + 1) // 2
print(a)
print(m)