# Задание 3
# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = int(input('Введите любое число'))
a = str(str(n) + str(n))
# print(a)
a = int(a)
# print(a)
b = str(str(n) + str(n) + str(n))
# print(b)
b = int(b)
# print(b)
result = n + a + b
print(result)