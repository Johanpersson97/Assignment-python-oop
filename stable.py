from animal import Animal
from building import Building

class Stable(Building):
    
    def __init__(self, name: str, length: int, width: int, value: int) -> None:
        super().__init__(name, length, width, value)


    def __str__(self) -> str:
        return f'Stable:\nName: {self.name}\nLength: {self.length}m\nWidth: {self.width}m\nArea: {self.area}m2\nValue: {self.get_value()}kr'