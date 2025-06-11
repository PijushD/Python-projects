import random

number_to_guess = random.randint(1, 100)

while True:
    try:
        user_input = int(input('Guess a number between 1 and 100: '))
        if user_input > number_to_guess:
            print('Too high')
        elif user_input < number_to_guess:
            print('Too small')
        else:
            print("Congratulations! you've guessed right number")
            break

    except ValueError:
        print('Invalid number')

