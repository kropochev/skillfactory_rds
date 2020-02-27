import random

count = 0
number = random.randint(1, 99)
print("Загадано число от 1 до 99")

for count in range(1, 100):  # более компактный вариант счетчика
    predict = random.randint(1, 100)  # предполагаемое число
    if number == predict:
        break  # выход из цикла, если угадали
    elif number > predict:
        print(f"Угадываемое число больше {predict} ")
    elif number < predict:
        print(f"Угадываемое число меньше {predict} ")

print(f"Вы угадали число {number} за {count} попыток.")