from animal import Animal

class Cat(Animal):
    
    def __init__(self, name:str, age:int, weight:float) -> None:
        super().__init__(name, age, weight)
        
    def talk(self) -> str:
        return f"Meow"

    def __str__(self) -> str:
        return f"Cat: \nName: {self.name}\nAge: {self.age}\nWeight (kgs): {self.weight}"