numbers = []
while True:
    user_input = input("Введите число (или любой символ для завершения): ")
    try:
        num = float(user_input)
        numbers.append(num)
    except ValueError:
        break

if numbers:
    print(f"Минимальное число: {min(numbers)}")
    print(f"Максимальное число: {max(numbers)}")
else:
    print("Не введено ни одного числа.")