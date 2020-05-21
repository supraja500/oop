from car import Car

class Truck(Car):
    sound="Honk Honk"
    def __init__(self,color,max_speed,acceleration,tyre_friction,max_cargo_weight):
        super().__init__(color,max_speed,acceleration,tyre_friction)
        self._total_load=0
        
        if max_cargo_weight>0:
            self._max_cargo_weight=max_cargo_weight
        else:
            raise ValueError("Invalid value for cargo_weight")
    
    def load(self,load_1):
        if load_1>0:
            self.load_1=load_1
        else:
            raise ValueError("Invalid value for cargo_weight")
        if self._current_speed>0:
            print("Cannot load cargo during motion")
        else:
            if self._total_load+load_1>=self._max_cargo_weight:
                print("Cannot load cargo more than max limit: {}".format(self._max_cargo_weight))
            else:
                 self._total_load+=load_1
    def unload(self,load_1):
        if load_1>0:
            if self._current_speed>0:
                print("Cannot unload cargo during motion")
            else:
                self._total_load-=load_1
        else:
            raise ValueError("Invalid value for cargo_weight")
        
    @property
    def max_cargo_weight(self):
        return self._max_cargo_weight
            
            
            
            

    