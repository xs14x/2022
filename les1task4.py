# Задание 4
# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.


a = int(input("Введите целое положительное число"))
b = a % 10
print(b)
while a >= 1:
    a = a // 10
    print(a)
    if a > b:
        b = a % 10
    if a > 9:
        continue
    else:
        print("Максимальное цифра в числе ", b)





# while(a > 0):
#     a = a // 10
#     print(a)
# print("Количество цифр равно:", a)
