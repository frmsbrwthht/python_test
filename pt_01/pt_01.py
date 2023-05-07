year = int(input("Введите номер года: "))

is_leap_year = (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)

if is_leap_year:
    print("Год ", year, " является високосным")
else:
    print("Год ", year, " не является високосным")