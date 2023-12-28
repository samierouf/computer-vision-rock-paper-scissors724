# Computer Vision RPS
This project implements a simple Rock-Paper-Scissors game using a computer vision model to predict the user's gesture through a webcam.

## Prerequisites

Python 3.8
Required Python packages: `cv2`, `numpy`, `keras`, `time`, `random`
Download the versions of the packages in the requirements.txt file


## Instalation
### packages/pre
Install the required packages using the following command:

```bash
pip install -r requirements.txt
```
## Clonening the repo
using the folwing clone the repo
```bash
git clone https://github.com/samierouf/computer-vision-rock-paper-scissors724.git
```
## Usage instructions
1) Run the game (camera_rps.py) and allow permission to your pc's camera.
  
2) The game starts with a countdown.

3) Show your hand gesture to the webcam during the countdown.

4) The computer will randomly choose a gesture.

5) The winner of the round will be determined based on the classic Rock Paper Scissors rules.

6) The game continues until one player (computer or user) wins three rounds.

## Trouble shooting
If there is trouble running the project it may be due to the package versions you are using, there us a lot of conflict between packages if you use there latest version so use the version in the requirements.txt file.
The project has issues distinguishing between paper and scissors gestures. This is not the fault of the code it is more so to do with the model and the images used to train them (keras_model.h5 and lables.xt) so you can use better model and lables by making them yourselves using teachable-machine [teachable-machine](https://teachablemachine.withgoogle.com/) if you want. 
If you are on mac keras_model.h5 and lables.txt have a habbit of becoming keras_model.h5.icloud and lables.txt.icloud which causes issues when trying to run the code to solve this issue open the location of where the project files are located in finder and press the icloud logo next to them to download them.

## File structure of the project
RPS-Template.py: is a file to test if evrything is working ok and ask for permison for python to acsess the camera.
manual_rps.py: is a file that allows you to play the rock paper scissore aganinst the comuter by requring the user to type out there choice instead of using the camera recognision.
keras_model.h5: is the pretrained model
lables.txt: contain the lables used to predict
requirements.txt: file contains the packages and the coressponding versions
camera_rps.py: is the file that contains the code used for playin the computer vison rock paper scissors game.
