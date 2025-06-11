import random

emojis = {'r':'🪨', 'p':'🧻', 's':'✂️'}
choices = ('r', 'p', 's')

while True:
    user_choice = input('Rock, Paper, or Scissor? (r/p/s): ')
    if user_choice not in choices:
        print('Invalid Input!')
    else:
        computer_choose = random.choice(choices)
        print(f'You choose {emojis[user_choice]}\n \
              Computer choose {emojis[computer_choose]}')
        if (user_choice == 'r' and computer_choose == 's' or
            user_choice == 'p' and computer_choose == 'r' or
            user_choice == 's' and computer_choose == 'p'):
            print('You won!')
        else:
            print('You loose!')
        while True:
            should_continue = input('Want to play again? (y/n): ').lower()
            if should_continue == 'n':
            break
        elif should_continue == 'y':
            continue
        else:
            print('Invalid Input!')

