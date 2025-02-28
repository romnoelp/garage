class Motorcycle: 
    def __init__(self, brand: str, engine_cc: float, valve_count: int):
        self.__brand = brand
        self.__engine_cc = engine_cc
        self.__valve_count = valve_count
        
    @property
    def brand(self): 
        return self.__brand
    
    @brand.setter
    def brand(self, new_brand: str):
        self.__brand = new_brand
        
    @property
    def engine_cc(self):
        return self.__engine_cc
    
    @engine_cc.setter
    def engine_cc(self, new_cc: float):
        if new_cc > 0:
            self.engine_cc = new_cc
        else:
            raise ValueError("Engine CC must be greater than 0")
    
    @property
    def valve_count(self):
        return self.__valve_count
    
    @valve_count.setter
    def valve_count(self, new_valve_count: int):
        if new_valve_count >= 1:
            self.__valve_count = new_valve_count
        else:
            raise ValueError("Lower valve count bikes are outdated")
        
    