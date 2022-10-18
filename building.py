class Building:
    '''
    lets the user create new buildings, or get/ set information about them
    '''

    def __init__(self, name:str, length:int, width:int, value:int) -> None:
        self.name:str = name
        self.length:int = length
        self.width:int = width
        self.area:float = self.width * self.length
        self.__value:int = value

    def get_name(self) -> str:
        '''
        Returns the name of a building
        '''
        return self.name
    
    def set_name(self, newName:str) -> None:
        '''
        Sets the name of a building
        '''
        self.name = newName
    
    def get_length(self) -> int:
        '''
        Returns the length of a building
        '''
        return self.length
    
    def set_length(self, newLength:int) -> None:
        '''
        Sets the length of a building
        '''
        self.age = newLength

    def get_width(self) -> int:
        '''
        Returns the width of a building
        '''
        return self.width
    
    def set_width(self, newWidth:int) -> None:
        '''
        Sets the width of a building
        '''
        self.width = newWidth

    def get_area(self) -> float:
        '''
        Returns the area of a building
        '''
        return self.area

    def get_value (self) -> int:
        '''
        returns the value of a building
        '''
        return self.__value

    def set_value(self, newValue) -> int:
        '''
        Sets the value of a building
        '''
        self.__value = newValue

    @classmethod
    def create(cls) -> any:
        '''
        Lets the user create a new building
        '''
        print("\nAdding a building to the ranch")
        buildingName = input("Name: ")
        buildingLength = int(input("Length: "))
        buildingWidth = int(input("Width: "))
        buildingValue = int(input("Value: "))
        return cls(buildingName, buildingLength, buildingWidth, buildingValue)

    def __str__(self) -> str:
        return f'{self.name} is {self.length} meters long and {self.width} meters wide, has an area of {self.area} and is worth {self.get_value()}'