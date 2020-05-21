from car import Car
import math
class RaceCar(Car):
    
    def __init__(self,color,max_speed,acceleration,tyre_friction):
        super().__init__(color,max_speed,acceleration,tyre_friction)
        self._nitro=0
        self.default=0
        
    def accelerate(self):
        super().accelerate()
        if self._nitro>0:
            self.default=self.acceleration*0.3
            self._current_speed=math.ceil(self._current_speed+self.default)
            self._nitro-=10
            if self._current_speed>self._max_speed:
                self._current_speed=self._max_speed
    def apply_brakes(self):
        if self._current_speed>=self._max_speed/2:
            self._nitro+=10
        super().apply_brakes()
        
    @property
    def nitro(self):
        return self._nitro  
    
    sound="Peep Peep\nBeep Beep"
    


    

    
    
    
 