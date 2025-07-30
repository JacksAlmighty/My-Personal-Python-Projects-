#Jackson Webster
#This program takes user input and gives the user a lot of options 

class Pets:
    def __init__ (self, type, name, age, size, breed):
        self.type = type
        self.name = name
        self.age = age
        self.size = size
        self.breed = breed
    
    def sound(self):
        while True:
            
                if self.type == "cat":
                    print(f"{self.name} makes a Meow noise")
                    break
                
                elif self.type == "dog":
                    print(f"{self.name} makes a Barking noise")
                    break
                
    def info(self):
        print(f"{self.name} is a {self.type} who is {self.age} years old and is a {self.size} pound {self.breed}.")

def add():

    animal_type = input("Do you have a dog or cat?:")
    animal_name = input("What is your animals name?:")
    animal_age = input("How old is your animal?:")
    animal_size = input("How big is your animal?(pounds):")
    animal_breed = input("What breed is your animal?:")
        
    my_pet = Pets(animal_type, animal_name, animal_age, animal_size, animal_breed)
    return my_pet

pets = []

while True:
     

     choice = input("Would you like to add a new pet?(add/view/speak/remove/quite)")

     if choice == "add":
        new_pet =  add()
        pets.append(new_pet)
     
     elif choice == "view":
        if not pets:
            print("no pets found try adding first.")
        else:
            for pet in pets:
                pet.info()
     
     elif choice == "speak":
        if not pets:
            print("no pets found try adding first.")
        else:
            for pet in pets:
                pet.sound()
     
     elif choice == "remove":
         if not pets:
            print("did not find check spelling.")
         else: 
            for i, pet in enumerate(pets):
                print(f"{i + 1}. {pet.name}")
            remove = input(f"Who would you like to remove from the list?")
                
            for pet in pets:
                if pet.name == remove:
                    pets.remove(pet)
                    break
     
     elif choice == "quite":
        print("Goodbye!")
        break
     else:
        print("Invalid input try: (add/view/speak/remove/quite)")
    
          
          
        

    
        
        





            