a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

total = sum(range(a, b + 1)) if a <= b else sum(range(b, a + 1))
print(f"Сумма чисел от {a} до {b} включительно: {total}")