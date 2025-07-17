# Program: Phone Book Manager
# Author: Jackson
# Date: July 12, 2025
# Description: Lets the user add, remove, and view contacts in a phone book.



phone_book = {
"jackson": "231-360-9414",
"isabele": "720-201-0431",
"dad": "720-201-0861",
"mom": "720-201-0852"
}

while True:
    user_input = input(f"Hello would you like to remove a number, add a number, or see your phone book?:(type q to quit):").strip().lower()
    
    if user_input == "q":
        print("Goodbye!")
        break
    
    elif user_input == "see":
        for key, value in phone_book.items():
            print(f"- {key}:{value}")
    
    elif user_input == "add":
        key = input("What name would you like to add?")
        value = input ("What is their phone number?")
        phone_book[key]= value
        
    
    elif user_input =="remove":
        remove = input (f"What number would you like to remove?{', '.join(phone_book)}\n").strip().lower()
        
        if remove in phone_book:
            del phone_book[remove]
            
        else:
            print("Was not found")

















    