import cv2
from keras.models import load_model
import numpy as np
import time
import random
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
ret, frame = cap.read()

def get_prediction():
    
    model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    # cap.release()
    resized_frame = cv2.resize(frame, (224, 224), interpolation=cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    data[0] = normalized_image

    # Make a prediction using the model
    predictions = model.predict(data)

    # Get the class with the highest probability
    predicted_class_index = np.argmax(predictions)
    
    predicted_class = get_user_choice(predicted_class_index)

    # Print the response from the model
    print("Model Predictions:", predictions)
    cap.release()

    return predicted_class


def get_user_choice(predicted_class_index): 
    classes = ["rock", "paper", "scissors", "nothing"]
    if predicted_class_index == 0:
        user_choice = classes[0]
    elif predicted_class_index == 1:
        user_choice = classes[1]
    elif predicted_class_index == 2:
        user_choice = classes[2]
    else:
        user_choice = classes[3]
    return user_choice


def get_computer_choice():
    possible_plays = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(possible_plays)
    return computer_choice

def get_winner(computer_choice, user_choice):
    print(f"Computer's choice: {computer_choice}")
    print(f"You chose: {user_choice}")
    if computer_choice == user_choice: # tie
        print('It is a tie this round')
        return None
    elif computer_choice == 'rock' and user_choice == 'paper': # user win
        print('You won! this round')
        return True
    elif computer_choice == 'rock' and user_choice == 'scissors':# user lost
        print('You lost! this round')
        return False
    elif computer_choice == 'paper' and user_choice == 'scissors':#user win
        print('You won! this round')
        return True
    elif computer_choice == 'paper' and user_choice == 'rock':#user lost
        print('You lost!')
        return False
    elif computer_choice == 'scissors' and user_choice == 'rock':#user win
        print('You won!')
        return True
    elif computer_choice == 'scissors' and user_choice == 'paper':#user lost
        print('You lost! this round')
        return False
    
def play_game():

    user_wins = 0
    computer_wins = 0
    rounds_to_win = 3
    round_counter = 1
    while (user_wins < rounds_to_win) or (computer_wins < rounds_to_win):
        print(f"Round:{round_counter}")
        countdown_duration = 3  # countdown duration in seconds

        #countdown
        print("Get ready! The game will start in:")
        for i in range(countdown_duration, 0, -1):
            print(i)
            time.sleep(1)  # 1 second between countdown numbers

        print("Go")

        
        user_choice = get_prediction()
        computer_choice = get_computer_choice()
        round_winner = get_winner(computer_choice, user_choice)

        if round_winner is False:
            computer_wins += 1
            round_counter += 1  # It's a tie, play the round again
            
        elif round_winner is True: # user wins
            user_wins += 1
            round_counter += 1
            
        else: # user losees 
            round_counter += 1
            
        print("Current Score ")
        print(f" Computer: {computer_wins} | User: {user_wins}")

    
        if user_wins == rounds_to_win:
            print("Congratulations! You won the game!")
            cv2.destroyAllWindows()
            break
        elif computer_wins == rounds_to_win:
            print("Sorry, the computer won the game. Better luck next time!")
            cv2.destroyAllWindows
            break
  
play_game()
