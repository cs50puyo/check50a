import random

user_wins = 0
computer_wins = 0

while True:
    user = eval(input('scissor (0), rock (1), paper (2): '))

    if user > 2 or user < 0:
        print('You provided an invalid input! Don\'t be a moron!')
    else:
        computer = random.randrange(3)

        if computer == 0:
            computer_choice = 'scissor'
        elif computer == 1:
            computer_choice = 'rock'
        else:
            computer_choice = 'paper'

        if user == 0:
            user_choice = 'scissor'
        elif user == 1:
            user_choice = 'rock'
        else:
            user_choice = 'paper'

        user_won = user == 0 and computer == 2 or \
                    user == 1 and computer == 0 or \
                    user == 2 and computer == 1

        if computer == user:
            result = 'It is a draw.'
        elif user_won:
            user_wins += 1
            result = 'You win.'
        else:
            computer_wins += 1
            result = 'You lose.'

        print(f'The computer is {computer_choice}. You are {user_choice}.')
        print(result)

        if user_wins == 2 or computer_wins == 2:
            break

print('{} has won 2 times.'.format('User' if user_wins == 2 else 'Computer'))
