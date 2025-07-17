while True:
  user_input = input("Hello enter a number here whole numbers only:(Type q to break)")
  if user_input.lower()  == "q":
    print("Thanks for using my program! Goodbye!")
    break
 
  try:
    number = int(user_input)
    if number % 2 == 0:
      print ("Even number")
    else:
      print("Odd number")
  except ValueError:
    print("Please enter only whole numbers such as, 3, 4, 5, 6")
