from collections import UserString
from barn import Barn
from horse import Horse
from cat import Cat
from animal import Animal

class Ranch:
    
    def __init__(self) -> None:
        self.barn:Barn = Barn()
        self.menu()
        
    def menu(self) -> None:
        '''
        Takes the user choice as an input and returns different functions
        '''
        print("Welcome to the barn!")
        userChoice = None
        while userChoice != "0":
            self.print_menu()
            userChoice = input("Choice: ")
            print("-"*30)
            
            if userChoice == "1":
                self.add_animal()
                
            elif userChoice == "2":
                self.set_name()
                
            elif userChoice == "3":
                self.remove_animal()
                
            elif userChoice == "4":
                self.print_animals()
                
            elif userChoice == "5":
                pass
                
            elif userChoice == "0":
                print("Goodbye, come back soon!")

            else:
                print("Invalid choice, please try again...")

    def print_menu(self) -> None:
        '''
        prints out a menu to the user
        '''
        print("\nMenu")
        print("-"*30)
        print("1) Add animal")
        print("2) ")
        print("3) Remove animal")
        print("4) List animals in the barn")
        print("5) Make them talk!")
        print("0) Exit")
        print("-"*30)
    
    def add_animal(self) -> None:
        '''
        lets the user add an animal of either the class horse or cat
        '''
        print("\nAdd animal")
        print("-"*30)
        print("What kind of animal?")
        for i, animal in enumerate(self.barn.ANIMALS):
            print(f"{i+1}) {animal.__name__}")

        userInput = int(input("Choice: ")) -1

        if userInput != len(self.barn.ANIMALS):
            animal = self.barn.ANIMALS[userInput].create()
            self.barn.add_animal(animal)
            print("Your Animal was added!")
        
        else:
            print("Wrong option, please choose a number from the list!")
            self.add_animal()
    
    def remove_animal(self) -> None:
        '''
        lets the user remove an animal from the ranch
        '''
        removeAnimal = (input("Choose the animal you wish to remove: "))
		
        if self.barn.remove_animal(removeAnimal) == True:
            print(f"Animal named {removeAnimal} have been removed!")
        
        else:
            print("Djuret existerar inte, vänligen ange ett korrekt namn!")

    def set_name (self) -> None:
        print("Which name would you like to change?")
        userInput = input("Name: ")
        newName = userInput

        return newName

    def print_animals(self) -> None:
        '''
        prints out all animals on the ranch, and shows a message if its empty
        '''
        if len(self.barn.get_animal()) == 0:
            print("There are no animals at the farm!")
        
        for animal in self.barn.get_animal():
            print (animal)
            print("-"*20)

Ranch() #Runs the app