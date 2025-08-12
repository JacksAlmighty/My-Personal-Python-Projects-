#Jackson Webster
#8/11/2025
#Randome Word Guessing game

import random
from random import shuffle


class Words:
    def __init__(self):

        self.easy = ["part", "cart","when","hard","easy","crab"]
        self.medium = ["harder","tatoo", "creamy","excelent","amazing"]
        self.hard = ["indubitably","anomaly","accolade","acrimony","quintessential","cacophony"]

    def get_word(self, difficulty):
        
        if difficulty == "easy":
            word = random.choice(self.easy)
        elif difficulty == "medium":
            word = random.choice(self.medium)
        elif difficulty == "hard":
            word = random.choice(self.hard)
        else:
            return None
       
        letters = list(word)
        random.shuffle(letters)
        shuffled_word = ''.join(letters)
        print(shuffled_word)
        return word

random_words = Words()

def main():
    print("Hello welcome to my random word guessing game!\n")
    
    

    while True: 
        
        difficulty = input("What would you like the difficulty to be?\n Easy \n Medium \n Hard \n").lower().strip()
        
        
        if difficulty == "easy":
            original_word = random_words.get_word(difficulty)
            while True:
                guess = input("Guess:")
                if guess == original_word:
                    print("Correct!")
                    play_again = input("Would you like to play again(Yes/No)\n").lower().strip()
                    if play_again == "yes":
                        break
                    elif play_again == "no":
                        print("Thanks for playing!")
                        return
                    
                
                else:
                    print("Incorrect")
                                
        
        elif difficulty == "medium":
            original_word = random_words.get_word(difficulty)
            while True:
                guess = input("Guess:")
                if guess == original_word:
                    print("Correct!")
                    play_again = input("Would you like to play again(Yes/No)\n").lower().strip()
                    if play_again == "yes":
                        break
                    elif play_again == "no":
                        print("Thanks for playing!")
                        return
                else:
                    print("Incorrect")
            
        
        
        elif difficulty == "hard":
            original_word = random_words.get_word(difficulty)
            while True:
                guess = input("Guess:")
                if guess == original_word:
                    print("Correct!")
                    play_again = input("Would you like to play again(Yes/No)\n").lower().strip()
                    if play_again == "yes":
                        break
                    elif play_again == "no":
                        print("Thanks for playing!")
                        return
                else:
                    print("Incorrect")
            
        else:
            print("Invalid input")
                
        
        
main()
