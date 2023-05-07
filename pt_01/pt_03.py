number = input("Введите шестизначное число: ")
if len(number) != 6:
    print("Некорректный ввод! Число должно быть шестизначным.")
else:
    first_sum = int(number[0]) + int(number[1]) + int(number[2])
    last_sum = int(number[3]) + int(number[4]) + int(number[5])
    if first_sum == last_sum:
        print(f"Число {number} является счастливым!")
    else:
        print(f"Число {number} не является счастливым.")