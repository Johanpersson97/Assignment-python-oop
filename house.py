from building import Building

class House(Building):
    pass

    def __init__(self, name: str, length: int, width: int, value: int) -> None:
        super().__init__(name, length, width, value)


    def __str__(self) -> str:
        return f'House:\nName: {self.name}\nLength: {self.length}m\nWidth: {self.width}m\nArea: {self.area}m2\nValue: {self.get_value()}kr'