class Animal:
    
    def __init__(self, name:str, age:int, weight:float) -> None:
        self.name:str = name
        self.age:int = age
        self.weight:float = weight

    def get_name(self) -> str:
        return self.name
    
    def set_name(self, newName:str) -> None:
        self.name.append(newName)
            
    def get_age(self) -> int:
        return self.age
    
    def set_age(self, newAge:int) -> None:
        self.age.append(newAge)

    @classmethod
    def create(cls) -> any:
        print("\nAdding an animal to the barn")
        animalName = input("Name: ")
        animalAge = int(input("Age: "))
        animalWeight = input("Weight: ")
        return cls(animalName, animalAge, animalWeight)

    def __str__(self) -> str:
        return f'{self.name} is {self.age} years old and weighs {self.weight}'