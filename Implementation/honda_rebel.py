from Base.motorcycle import Motorcycle
from Base_Types.manual import Manual
from Base_Types.automatic import Automatic  

class HondaRebel1100(Motorcycle, Manual, Automatic):
    def __init__(self, is_dct: bool = False):  
        Motorcycle.__init__(self, "Honda Rebel 1100", 1084, 4)  
        
        self.__is_dct: bool = is_dct  
        if self.__is_dct:
            Automatic.__init__(self)  
        else:
            Manual.__init__(self)  

        self.__cruiser_style: bool = True
        self.__torque_control: bool = True  

    @property
    def cruiser_style(self) -> bool:
        return self.__cruiser_style

    @property
    def torque_control(self) -> bool:
        return self.__torque_control

    @property
    def is_dct(self) -> bool:
        return self.__is_dct

    def switch_transmission(self):
        """Switch between Manual and Automatic (DCT)"""
        self.__is_dct = not self.__is_dct  
        if self.__is_dct:
            Automatic.__init__(self)
        else:
            Manual.__init__(self)
