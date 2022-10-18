class Animal:
    
    def __init__(self, name:str, age:int, weight:float) -> None:
        self.name:str = name
        self.age:int = age
        self.weight:float = weight

    def get_name(self) -> str:
        '''
        Returns the name of an animal
        '''
        return self.name
    
    def set_name(self, newName:str) -> None:
        '''
        Sets the name of an animal
        '''
        self.name = newName
            
    def get_age(self) -> int:
        '''
        Returns the age of an animal
        '''
        return self.age
    
    def set_age(self, newAge:int) -> None:
        '''
        Sets the age of an animal
        '''
        self.age = newAge

    def get_weight(self) -> float:
        '''
        Returns the weight of an animal
        '''
        return self.weight

    def set_weight(self, newWeight:float) -> None:
        '''
        Sets the weight of the animal
        '''
        self.weight = newWeight

    @classmethod
    def create(cls) -> any:
        '''
        Lets the user create a new animal
        '''
        print("\nAdding an animal to the barn")
        animalName = input("Name: ")
        animalAge = int(input("Age: "))
        animalWeight = input("Weight: ")
        return cls(animalName, animalAge, animalWeight)

    def __str__(self) -> str:
        return f'{self.name} is {self.age} years old and weighs {self.weight}'