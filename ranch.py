from collections import UserString
from email.charset import add_alias
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
        Takes the user choice as an input and then runs different functions
        '''
        print("Welcome to the barn!")
        userChoice = None
        while userChoice != "0":
            self.print_menu()
            userChoice = input("Choice: ")
            print("-"*30)
            
            if userChoice == "1":
                userChoice = None
                while userChoice != "0":
                    self.print_animal_menu()
                    userChoice = input("Choice: ")
                    if userChoice == "1":
                        self.add_animal()

                    elif userChoice == "2":
                        self.edit_animal()

                    elif userChoice == "3":
                        self.remove_animal()

                    elif userChoice == "4":
                        self.print_animals()

                    elif userChoice == "5":
                        self.menu()
                    
                    elif userChoice == "0":
                        print("Goodbye, come back soon!")

            elif userChoice == "2":
                self.print_building_menu()
                
            elif userChoice == "3":
                pass
                
            elif userChoice == "4":
                pass
                
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
        print("1) Animal menu")
        print("2) Building menu")
        print("3) ")
        print("0) Exit")
        print("-"*30)

    def print_animal_menu(self) -> None:
        print("\nAnimal Menu")
        print("-"*30)
        print("1) Add animal")
        print("2) Edit animal")
        print("3) Remove animal")
        print("4) List animals in the barn")
        print("5) Main menu")
        print("0) Exit")
        print("-"*30)

    def print_building_menu(self) -> None:
        print("\nAnimal Menu")
        print("-"*30)
        print("1) Add building")
        print("2) Edit building")
        print("3) Remove building")
        print("4) List buildings")
        print("5) Main menu")
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
            print("That animal doesn't exist, please choose again")

    def edit_animal (self) -> None:
        '''
        lets the user choose an animal to edit, then change their name, age and weight
        '''
        print("Which name would you like to change?")
        editAnimal = input("Name: ")

        newName = input("Change name: ")
        newAge = int(input("Change Age: "))
        newWeight = input("Change weight: ")

        if self.barn.edit_animal(editAnimal, newName, newAge, newWeight) == True:
            print("The animal has been edited!")

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