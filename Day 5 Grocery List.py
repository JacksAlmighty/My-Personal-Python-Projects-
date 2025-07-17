grocery_list = []


while True:
    try:
        option = input ("Would you like to add to your list, remove from your list, or see your list?(add,remove,see,quit)").lower().strip()
        if option == "add":
            item=input("What would you like to add? one at a time please:")
            grocery_list.append(item)
            print(f"This is your list: {','.join(grocery_list)}\n")
       
        elif option == "remove":
            item=input("What would you like to remove? one at a time please:").lower().strip()
            grocery_list.remove(item)
            print(f"This is your list: {','.join(grocery_list)}\n")
       
        elif option == "see":
            print(f"This is your list: {','.join(grocery_list)}\n")
       
        elif option == "quit":
            print("Goodbye!")
            break
        else:
            print(f"This is your list: {','.join(grocery_list)}\n")
    except ValueError:
       
        print(f"this is your list {grocery_list}, make sure you didnt miss spell anything. Try again")