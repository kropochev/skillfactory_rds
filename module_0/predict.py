import random

count = 0
number = random.randint(1, 99)
print("Загадано число от 1 до 99")

while True:
    predict = int(input())
    count += 1
    if number == predict:
        break  # выход из цикла, если угадали
    elif number > predict:
        print(f"Угадываемое число больше {predict} ")
    elif number < predict:
        print(f"Угадываемое число меньше {predict} ")

print(f"Вы угадали число {number} за {count} попыток.")