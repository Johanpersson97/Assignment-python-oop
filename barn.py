from animal import Animal
from cat import Cat
from horse import Horse

class Barn:

    ANIMALS = [Cat, Horse]
    
    def __init__(self) -> None:
        self.animals:list = []
        
    def add_animal(self, animal:any) -> None:
        self.animals.append(animal)

    def get_animal(self) -> list:
        return self.animals

    def remove_animal(self, removeAnimal:str) -> bool:
        for animal in self.animals:
            if animal.get_name() == removeAnimal:
                self.animals.remove(animal)
                return True
        return False