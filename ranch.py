from barn import Barn

class Ranch:
    '''
    Main class that runs the program
    '''
    def __init__(self) -> None:
        self.barn:Barn = Barn()
        self.menu()


    def menu(self) -> None:
        '''
        Takes the user choice as an input and then runs different functions depending on the choice
        '''
        print("Welcome to the ranch!")
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
                    print("-"*30)

                    if userChoice == "1":
                        self.add_animal()

                    elif userChoice == "2":
                        self.edit_animal()

                    elif userChoice == "3":
                        self.print_animals()

                    elif userChoice == "4":
                        self.remove_animal()

                    elif userChoice == "5":
                        self.menu()

                    elif userChoice == "0":
                        print("Goodbye, come back soon!")
                        exit()
                    else:
                        print("Invalid choice, please try again...")

            elif userChoice == "2":
                userChoice = None
                while userChoice != "0":

                    self.print_building_menu()
                    userChoice = input("Choice: ")
                    print("-"*30)

                    if userChoice == "1":
                        self.add_building()

                    elif userChoice == "2":
                        self.edit_building()

                    elif userChoice == "3":
                        self.print_buildings()

                    elif userChoice == "4":
                        self.remove_building()

                    elif userChoice == "5":
                        self.menu()
                    
                    elif userChoice == "0":
                        print("Goodbye, come back soon!")
                        exit()

                    else:
                        print("Invalid choice, please try again...")
                
            elif userChoice == "3":
                self.search_animal()
                
            elif userChoice == "0":
                print("Goodbye, come back soon!")

            else:
                print("Invalid choice, please try again...")


    def print_menu(self) -> None:
        '''
        prints out a menu to the user
        '''
        print("\nMenu:")
        print("-"*30)
        print("1) Animal menu")
        print("2) Building menu")
        print("3) Search animal")
        print("0) Exit")
        print("-"*30)


    def print_animal_menu(self) -> None:
        print("\nAnimal Menu:")
        print("-"*30)
        print("1) Add animal")
        print("2) Edit animal")        
        print("3) List animals")
        print("4) Remove animal")
        print("5) Main menu")
        print("0) Exit")
        print("-"*30)


    def print_building_menu(self) -> None:
        print("\nBuilding Menu:")
        print("-"*30)
        print("1) Add building")
        print("2) Edit building")
        print("3) List buildings")
        print("4) Remove building")
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
        
        try: 
            userInput = int(input("Choice: ")) -1
            
            if userInput != len(self.barn.ANIMALS):
                try: 
                    animal = self.barn.ANIMALS[userInput].create()
                    self.barn.add_animal(animal)
                    print("Your Animal was added!")

                except IndexError:
                    print("Please choose a valid number!")
                    self.add_animal()
            
            else:
                print("Wrong option, please choose a number from the list!")
                self.add_animal()

        except ValueError:
            print("Plese enter an integer!")
            self.add_animal()


    def edit_animal(self) -> None:
        '''
        lets the user choose an animal to edit, then change their name, age and weight
        '''

        print("Which animal would you like to edit?")
        editAnimal = input("Name: ")

        newName:str = input("Change name: ")
        newAge:int = int(input("Change Age: "))
        newWeight:float = input("Change weight: ")

        if self.barn.edit_animal(editAnimal, newName, newAge, newWeight) == True:
            print("The animal has been edited!")


    def remove_animal(self) -> None:
        '''
        lets the user remove an animal from the ranch
        '''
        removeAnimal = (input("Choose the animal you wish to remove: "))
		
        if self.barn.remove_animal(removeAnimal) == True:
            print(f"Animal named {removeAnimal} have been removed!")
        
        else:
            print("That animal doesn't exist, please choose again")


    def search_animal(self) -> None:
        '''
        Asks the user for a string and searches if theres any animal with the given input, 
        if there is, prints out the animals that matches the search
        '''
        searchString = input("Please enter search String: ")
        searchResult = self.barn.search_animal(searchString)

        if len(searchResult) == 0:
            print("Couldn't find any animals...")

        else:
            print("Found animal/s: ")
            print("-"*20)
            for animal in searchResult:
                print(animal)
                print("-"*20)


    def print_animals(self) -> None:
        '''
        prints out all animals on the ranch, and shows a message if its empty
        '''
        if len(self.barn.get_animal()) == 0:
            print("There are no animals at the farm!")
        
        for animal in self.barn.get_animal():
            print (animal)
            print("-"*20)


    def add_building(self) -> None:
        '''
        lets the user add a building to the ranch
        '''
        print("\nAdd building")
        print("-"*30)
        print("What kind of building?")
        for i, building in enumerate(self.barn.BUILDINGS):
            print(f"{i+1}) {building.__name__}")
        
        try: 

            userInput = int(input("Choice: ")) -1

            if userInput != len(self.barn.BUILDINGS):
                try:
                    building = self.barn.BUILDINGS[userInput].create()
                    self.barn.add_building(building)
                    print("Your Building was added!")
                except IndexError:
                    print("Please choose a valid number!")
                    self.add_building()
            
            else:
                print("Wrong option, please choose a number from the list!")
                self.add_building()

        except ValueError:
            print("Plese enter an integer!")
            self.add_building()

    def edit_building(self) -> None:
        '''
        Lets the user edit a building
        '''
        print("Which building would you like to edit?")
        editBuilding = input("Name: ")

        newName:str = input("Change name: ")
        newLength:int = int(input("Change length: "))
        newWidth:float = input("Change width: ")
        newValue:int = int(input("Change the value: "))

        if self.barn.edit_building(editBuilding, newName, newLength, newWidth, newValue) == True:
            print("The building has been edited!")


    def remove_building(self) -> None:
        '''
        Lets the user remove a building
        '''
        removeBuilding = (input("Choose the building you wish to remove: "))
		
        if self.barn.remove_building(removeBuilding) == True:
            print(f"Building named {removeBuilding} has been removed!")
        
        else:
            print("That building doesn't exist, please choose again")


    def print_buildings(self) -> None:
        '''
        prints information about the buildings for the user
        '''
        if len (self.barn.get_building()) == 0:
            print("There are no buildings on the Ranch!")

        for building in self.barn.get_building():
            print(building)
            print("-"*20)

Ranch() #Runs the app