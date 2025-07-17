#Jackson Webster
#7/15/2025
#This program takes user input and writes it into a file


file_name = input("Write the name of your file add '.txt' at the end\n")

contents = input("What would you like to write in your file?\n")

try:
    with open(file_name, 'w') as file:
        file.write(contents)

    print(f"This is what is in your file \n{contents}")


except Exception as e:
    print(f"an error has occured: {e}")