num = int(input('Введите число:'))
digit1 = num // 100
digit2 = (num // 10) % 10
digit3 = num % 10
sum_digits = digit1 + digit2 + digit3
print("Сумма цифр числа " + str(num) + " равна " + str(sum_digits))
