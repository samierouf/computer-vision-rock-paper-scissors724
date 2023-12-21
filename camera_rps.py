import cv2
from keras.models import load_model
import numpy as np
import time
import random 

def get_computer_choice():
    possible_plays = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(possible_plays)
    return computer_choice

def get_prediction(predicted_class_index): 
    if predicted_class_index == 0:
        user_choice = 'rock'
        print(user_choice)
    elif predicted_class_index == 1:
        user_choice = 'paper'
        print(user_choice)
    elif predicted_class_index == 2:
        user_choice = 'scissors'
        print(user_choice)
    else:
        user_choice = 'nothing'
        print(user_choice)
    return user_choice


def get_user_choice():
    model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    countdown_duration = 3

    start_time = time.time()
    elapsed_time = 0


    while elapsed_time < countdown_duration: 
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)

        remaining_time = max(0, int(countdown_duration - elapsed_time))
        print(f"Countdown: {remaining_time} seconds", end='\r')
        elapsed_time = time.time() - start_time
    print(" " * 30, end='\r')


    prediction = model.predict(data)
    predicted_class_index = np.argmax(prediction)


    print("You Chosse ", get_prediction(predicted_class_index))
    cv2.imshow('frame', frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cap.release()

    return predicted_class_index

def get_winner(computer_choice, user_choice):
    if computer_choice == user_choice: # tie
        #print('It is a tie this round')
        return [0,0]
    elif computer_choice == 'rock' and user_choice == 'paper': # user win
        #print('You won! this round')
        return [1,0]
    elif computer_choice == 'rock' and user_choice == 'scissors':# user lost
        #print('You lost! this round')
        return [0,1]
    elif computer_choice == 'paper' and user_choice == 'scissors':#user win
        #print('You won! this round')
        return [1,0]
    elif computer_choice == 'paper' and user_choice == 'rock':#user lost
        #print('You lost!')
        return[0,1]
    elif computer_choice == 'scissors' and user_choice == 'rock':#user win
        #print('You won!')
        return [1,0]
    elif computer_choice == 'scissors' and user_choice == 'paper':#user lost
        #print('You lost! this round')
        return [0,1]



def play_game():
    game_round = 1
    computer_wins = 0
    user_wins = 0
    while True:
        print(f"round {game_round}")
        score = get_winner(get_computer_choice(), get_user_choice())
        user_wins += score[0]
        computer_wins += score[1]
        if computer_wins == 3:
            print(f'Computer wins. You lost.')
            print(f"Computer={computer_wins} : User={user_wins}")
            break
        elif user_wins == 3:
            print(f"You win. computer losses")
            print(f"Computer={computer_wins} : User={user_wins}")
            break
        else:
            game_round += 1

play_game()