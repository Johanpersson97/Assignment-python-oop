from animal import Animal
from building import Building
from cat import Cat
from horse import Horse
from stable import Stable
from house import House
from garage import Garage
from machine_hall import Machine_hall

class Barn:

    ANIMALS:list = [Cat, Horse]
    BUILDINGS:list = [Stable, House, Garage, Machine_hall]

    def __init__(self) -> None:
        self.animals:list = [
        Cat("Igun", 2, 4.6),
        Cat("Agda", 2, 3.1),
        Cat("Jinx", 1, 3.0),
        Cat("Yatzy", 1, 2.6),
        Horse("Qasino", 13, 590),
        Horse("Corneo", 13, 700),
        Horse("Lilla", 8, 450),
        Horse("Prinsessan", 5, 400)
        ]

        self.buildings:list = [
        Stable("Stable", 20, 15, 1000000),
        House("House", 16, 8, 1200000),
        Garage("Garage", 12, 9, 500000),
        Machine_hall("Machine hall", 20, 15, 400000)
        ]


    def add_animal(self, animal:any) -> None:
        '''
        Appends an animal to the list
        '''
        self.animals.append(animal)


    def get_animal(self) -> list:
        '''
        Returns a list of animals in the barn 
        '''
        return self.animals


    def edit_animal(self, editAnimal:str, newName:str, newAge:int, newWeight:float) -> bool:
        '''
        lets the user edit an already existing animal
        '''
        for animal in self.animals:
            if animal.get_name() == editAnimal:
                animal.set_name(newName)
                animal.set_age(newAge)
                animal.set_weight(newWeight)
                print("Success!")
                return True
        return False


    def remove_animal(self, removeAnimal:str) -> bool:
        '''
        Removes an animal from the list
        '''
        for animal in self.animals:
            if animal.get_name() == removeAnimal:
                self.animals.remove(animal)
                return True
        return False


    def search_animal(self, searchString:str) -> list:
        '''
        Takes the users search as an argument and returns a list if the user 
        '''
        foundAnimals = []
        for animal in self.animals:
            if searchString in animal.name:
                foundAnimals.append(animal)

        return foundAnimals


    def add_building(self, building:any) -> None:
        '''
        appends a building to the list
        '''
        self.buildings.append(building)


    def get_building(self) -> list:
        '''
        returns a list of buildings
        '''
        return self.buildings


    def edit_building(self, editBuilding, newName:str, newLength:int, newWidth:int, newValue:int) -> bool:
        '''
        Lets the user edit an existing building
        '''
        for building in self.buildings:
            if building.get_name() == editBuilding:
                building.set_name(newName)
                building.set_length(newLength)
                building.set_width(newWidth)
                building.set_value(newValue)
                print("-"*20)
                print("Success!")
                return True
        return False


    def remove_building(self, removeBuilding:str) -> bool:
        '''
        Takes removeBuilding as an argument and removes it if it exists in the list of buildings.
        '''
        for building in self.buildings:
            if building.get_name() == removeBuilding:
                self.buildings.remove(building)
                return True
        return False