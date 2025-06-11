import random

rand = random.randint(1, 100)
while True:
    try:
        num = int(input('Enter number between 1 and 100: '))
        if num == rand:
            print("Congratulations! you've guessed right number")
            break
        elif num > rand and num <= 98:
            print("Too high")
        elif num < rand and num >= 1:
            print("Too small")
        else:
            print("Invalid number!")

    except ValueError:
        print('Enter valid number')

