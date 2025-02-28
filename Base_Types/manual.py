class Manual:
    def __init__(self):
        self.__manual_transmission: bool = True

    @property
    def manual_transmission(self) -> bool:  
        return self.__manual_transmission
