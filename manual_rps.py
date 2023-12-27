import random


def get_computer_choice(): # function randomly chooses a choice for the computer
    possible_plays = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(possible_plays)
    return computer_choice

def get_user_choice(): # function that asks for the user to input their choice
    print("Rock, Paper or Scissors")
    user_choice = input('Pick one: ')
    user_choice = user_choice.lower()
    return user_choice

def get_winner(computer_choice, user_choice): # compare the user and computers choices to determin winner
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



def play(): # function calls the previous function to play the game
    get_winner(get_computer_choice(), get_user_choice())


play()
