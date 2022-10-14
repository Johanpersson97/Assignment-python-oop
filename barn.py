from animal import Animal
from cat import Cat
from horse import Horse

class Barn:

    ANIMALS:list = [Cat, Horse]
    
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

    def remove_animal(self, removeAnimal:str) -> bool:
        '''
        Removes an animal from the list
        '''
        for animal in self.animals:
            if animal.get_name() == removeAnimal:
                self.animals.remove(animal)
                return True
        return False