from barn import Barn
from horse import Horse
from cat import Cat
from animal import Animal

class Farm:
    
    def __init__(self) -> None:
        self.barn = Barn()
        self.menu()
        self.animal:Animal = Animal()
        
    def menu(self) -> None:
        print("Welcome to the barn!")
        userChoice = None
        while userChoice != "0":
            self.print_menu()
            userChoice = input("Choice: ")
            
            if userChoice == "1":
                self.add_animal()
                
            elif userChoice == "2":
                pass
                
            elif userChoice == "3":
                self.remove_animal()
                
            elif userChoice == "4":
                self.print_animals()
                
            elif userChoice == "5":
                self.let_them_talk()
                
            elif userChoice == "0":
                print("Goodbye, come back soon!")
            else:
                print("Invalid choice, please try again...")

    def print_menu(self) -> None:
        print("\nMenu")
        print("-"*30)
        print("1) Add animal")
        print("2) ")
        print("3) Remove animal")
        print("4) List animals in the barn")
        print("5) Make them talk!")
        print("0) Exit")
        
    def add_animal(self) -> None:
        print("\nAdd animal")
        print("-"*30)
        print("What kind of animal?")
        for i, animal in enumerate(self.barn.ANIMALS):
            print(f"{i+1}) {animal.__name__}")
        
        userInput = int(input("Choice: ")) -1
        
        animal = self.barn.ANIMALS[userInput].create()
        
        self.barn.add_animal(animal)
        print("Your Animal was added!")
    
    def remove_animal(self) -> None:
        removeAnimal = (input("Choose the animal you wish to remove: "))
		
        if self.barn.remove_animal(removeAnimal) == True:
            print(f"Animal named {removeAnimal} have been removed!")
    
    def print_animals(self) -> None:
        if len(self.barn.get_animal()) == 0:
            print("There are no animals at the farm!")
            
        for animal in self.barn.get_animal():
            print (animal)
            print("-"*20)
    
    def let_them_talk(self) -> None:
        for animal in self.barn.get_animal():
            print(f"{animal.get_name()}: {animal.talk()}")

Farm()