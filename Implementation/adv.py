from Base.motorcycle import Motorcycle
from Base_Types.automatic import Automatic

class ADV(Motorcycle, Automatic):
    def __init__(self, engine_cc: float, valve_count: int):
        Motorcycle.__init__(self, "Honda ADV 160", engine_cc, valve_count) 
        Automatic.__init__(self)
        
        self.__keyless_ignition: bool = True
        self.__off_road_capable: bool = True

    @property
    def off_road_capable(self) -> bool:  
        return self.__off_road_capable

    @property
    def keyless_ignition(self) -> bool: 
        return self.__keyless_ignition
