class Automatic: 
    def __init__(self):
        self.__auto_transmission: bool = True  
    @property 
    def auto_transmission(self) -> bool: 
        return self.__auto_transmission
