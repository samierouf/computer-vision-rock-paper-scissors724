import random


def get_computer_choice():
    possible_plays = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(possible_plays)
    return computer_choice

def get_user_choice():
    print("Rock, Paper or Scissors")
    user_choice = input('Pick one: ')
    return user_choice

def get_winner(computer_choice, user_choice):
    if computer_choice == 'rock' and user_choice == 'rock':
        print('It is a tie')
    elif computer_choice == 'rock' and user_choice == 'paper':
        print('You won!')
    elif computer_choice == 'rock' and user_choice == 'scissors':
        print('You lost!')
    elif computer_choice == 'paper' and user_choice == 'paper':
        print('It is a tie')
    elif computer_choice == 'paper' and user_choice == 'scissors':
        print('You won!')
    elif computer_choice == 'paper' and user_choice == 'rock':
        print('You lost!')
    elif computer_choice == 'scissors' and user_choice == 'scissors':
        print('It is a tie')
    elif computer_choice == 'scissors' and user_choice == 'rock':
        print('You won!')
    elif computer_choice == 'scissors' and user_choice == 'paper':
        print('You lost!')



def play():
    get_winner(get_computer_choice(), get_user_choice())


play()