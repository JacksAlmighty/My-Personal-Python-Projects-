for number in range (1,51):
   
    print(f"{number}, the square of {number} is {number * number}")
while True:
    proceed = input("would you like to continue?(yes/no):").lower()
    if proceed.lower() == "no":
        print("Goodbye!")
        break
    elif proceed == "yes":
        for number in range(1,51):
            if number % 3 == 0 and number % 5 == 0:
                print (f"{number} FizzBuzz")
            elif number % 3 == 0:
                print (f"{number} Fizz")
            elif number % 5 == 0:
                print(f"{number} Buzz")
            else:
                print(number)
    else:
        print("please type 'yes' or 'no'.")
