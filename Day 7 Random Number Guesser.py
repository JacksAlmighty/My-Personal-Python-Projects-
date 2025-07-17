#Jackson Webster
#7/14/25
#This code will have you play a randome number generator with the computer

import random
start = input("Would you like top play my game?(Yes/No)\n").lower().strip()
guesses = 0

while True:
    
    random_number = random.randint(1,100)
    print("Can you guess the number I am thinking of between 1 and 100 within 10 guesses?")
    while True:
        try:
            
            guess = int(input(f"You are on guess {guesses}\n"))
                
            guesses = guesses + 1
                
            if guess > 100 or guess < 0:
                    print("It has to be between 1 and 100!\n")
                    
            elif guess < random_number:
                    print("Higher\n")
                    
            elif guess > random_number:
                    print(f"Lower\n")
                    
            elif guess == random_number:
                    print(f"Correct! Goodjob! It took you {guesses} guesses!")
                    break
                
            if guesses > 10:
                print("You lose!")
                break
            
            elif start == "no":
                print("Goodbye!")
                break
        except ValueError:
            print("Invalid Input")
    
    play_again = input("Would you like to play again?(Yes/No)\n").lower().strip()
                        
    if play_again == "yes":
        guesses = 0
        continue
    #I have to reset the guesses or else it will fail you on your first guess            
    #loops again so it can restart
    elif play_again == "no":
        print("Thank for playing!")
        break
    else:
        print("Invalid input")
                    

