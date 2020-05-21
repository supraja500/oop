class object:
    def __init__(self,color,max_speed,acceleration,tyre_friction):
        self.color=color
        self.current_speed=0
        self.is_engine_started=False
        self.nitro=0
        if max_speed>0:
            self.max_speed=max_speed
        else:
            raise ValueError("Invalid value for max_speed")
        if acceleration>0:
            self.acceleration=acceleration
        else:
            raise ValueError("Invalid value for acceleration")
        if tyre_friction>0:
            self.tyre_friction=tyre_friction
        else:
            raise ValueError("Invalid value for tyre_friction")
    
    
    
    
    
    def start_engine(self):
        self.is_engine_started=True
        
                
    
    
     
        
        
            
    
    def sound_horn(self):
        if self.is_engine_started==True:
            print("Peep Peep")
            print("Beep Beep")
        else:
            print("Start the engine to sound_horn")

    def stop_engine(self):
        self.is_engine_started=False
        
  



class RaceCar(object):
    
    
    
    def accelerate(self):
        if self.is_engine_started==True:
            self.current_speed+=self.acceleration
            if self.current_speed>=self.max_speed:
                self.current_speed=self.max_speed
            
        else:
            print("Start the engine to accelerate")
            
    def apply_brakes(self):
        self.current_speed-=self.tyre_friction
        if self.current_speed<self.tyre_friction:
            self.current_speed=0
            return self.current_speed
        else:
            return self.current_speed
        