import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import cv2
from keras.models import load_model
import numpy as np
import random
import time

class RFP:
    def __init__(self):
        self.model = load_model('keras_model.h5 2', compile=False)
        self.labels = open('labels.txt', 'r').readlines()
        # CAMERA can be 0 or 1 based on default camera of your computer.
        self.cap = cv2.VideoCapture(0)
        self.user_wins = 0 
        self.computer_wins = 0

    def get_prediction(self):
        counter = 3
        print("Please show your choice in")
        while counter > 0:
            print(counter)
            cv2.waitKey(1000)
            counter -= 1
        print("Show your hand now")
        
        end = time.time() + 1
        while time.time() < end:
            
            ret, frame = self.cap.read()
            
            if not ret:
                break
            
            # Make the image a numpy array and reshape it to the models input shape.
            data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
            # Resize the raw image into (224-height,224-width) pixels.
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            # Show the image in a window
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            cv2.imshow('frame', frame)
            prediction = self.model.predict(data)
            
            best_prediction = self.labels[np.argmax(prediction[0])]
            
            for i in ["Rock", "Paper", "Scissors", "Nothing"]:
                if i in best_prediction:
                    self.user_choice = i
            
            if cv2.waitKey(1) == 27:
                break
        
        print(self.user_choice)
        return self.user_choice

    def get_computer_choice(self):
        computer_choice = random.choice(choices[:-1])
        return computer_choice

    def get_winner(self, computer_choice, user_choice):
        if computer_choice == user_choice:
            winner = "Both"
            
        elif computer_choice == "Rock":
            if user_choice == "Paper":
                winner = "User"
            else:
                winner = "Computer"
        elif computer_choice == "Paper":
            if user_choice == "Scissors":
                winner = "User"
            else:
                winner = "Computer"
        else:
            if user_choice == "Rock":
                winner = "User"
            else:
                winner = "Computer"
        
        return winner

#It calls all the functions and runs the game
def play(choices):
    game = RFP()
    while game.user_wins < 3 or game.computer_wins < 3:
        computer_choice = game.get_computer_choice()
        user_choice = game.get_prediction()
        win = game.get_winner(computer_choice, user_choice)
    
        if win == "Computer":
            game.computer_wins += 1
        elif win == "User":
            game.user_wins += 1
    
    if game.user_wins == 3:
        print("Congratulations! You win.")
    elif game.computer_wins == 3:
        print("Unfortunately, you lost!")

# After the loop release the cap object
    game.cap.release()
# Destroy all the windows
    cv2.destroyAllWindows()

if __name__ == '__main__':
    choices = ['rock', 'paper', 'scissors', 'nothing']
    play(choices)
