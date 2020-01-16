# https://drive.google.com/file/d/1mMdCpTrWY7BgpOekTOWyxl1DBElzeg2P/view?usp=sharing
# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

number = int(input("Введите трёхзначное число: "))

a = number // 100
b = number % 100 // 10
c = number % 10

x = a * b * c
y = a + b + c

print("Произведение чисел = ", x)
print("Сумма чисел = ", y)
