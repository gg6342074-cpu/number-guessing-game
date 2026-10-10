from random import randint
res = randint(0, 100)
number = int(input("Угадайте число: "))
while True:
    if number == res:
        print("Вы угадали число!")
        break
    elif number > res:
        print("Введите число меньше!")
        number = int(input("Угадайте число: "))
    elif number < res:
        print("Введите число больше!")
        number = int(input("Угадайте число: "))