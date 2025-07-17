print ("Hello Welcome to my calculator")


while True:
   
    option = input ("Would you like to devide, add, subtract, multiply or quit?:").lower().strip()
   
    try:
        if option == "devide":
            number_1 =  float(input(f"What number would you like to {option} with?:"))
            number_2 =  float(input(f"What number would you like to be {option}?:"))
   
            divide = number_2 / number_1


            print (f"{number_2} divided by {number_1} is {round( divide, 2)}. Thank you for using my calculator! come again!")
       
        elif option == "multiply":
            number_1 =  float(input(f"What number would you like to {option} with?:"))
            number_2 =  float(input(f"What number would you like to be {option}?:"))
   
            multiply = number_2 * number_1


            print (f"{number_2} multiplied by {number_1} is {round( multiply, 2)}. Thank you for using my calculator! come again!")
       
        elif option == "subtract":
            number_1 =  float(input(f"What number would you like to {option} with?:"))
            number_2 =  float(input(f"What number would you like to be {option}?:"))
   
            subtract = number_2 - number_1


            print (f"{number_2} subtracted by {number_1} is {round( subtract, 2)}. Thank you for using my calculator! come again!")
       
        elif option == "add":
            number_1 =  float(input(f"What number would you like to {option} with?:"))
            number_2 =  float(input(f"What number would you like to be {option}?:"))
   
            add= number_2 + number_1


            print (f"{number_2} added to {number_1} is {round( add, 2)}. Thank you for using my calculator! come again!")
       
        elif option == "quit":
            print("Goodbye")
            break
       
        else:
            print("invalid option try again")
    except ValueError:
            print("Invalid input try again")
