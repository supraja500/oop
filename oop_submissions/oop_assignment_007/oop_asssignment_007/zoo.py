class Deer:
    def __init__(self,age_in_months,required_food_in_kgs,breed):
        #self.age_in_months=age_in_months
        self.required_food_in_kgs=required_food_in_kgs
        self.breed=breed
        
        if age_in_months>1:
            raise ValueError("Invalid value for field age_in_months: {}".format(age_in_months))
        else:
            self.age_in_months=age_in_months
            
            
    def grow(self):
        self.required_food_in_kgs=self.required_food_in_kgs+2
        self.age_in_months=self.age_in_months+1
        
    
    def make_sound(self):
        print("Buck Buck")
    def breathe(self):
        print("Breathe in air")
       
class Lion(Deer):
    def __init__(self,age_in_months,required_food_in_kgs,breed):
        super().__init__(age_in_months,required_food_in_kgs,breed)
    def grow(self):
        self.required_food_in_kgs=self.required_food_in_kgs+4
        self.age_in_months=self.age_in_months+1
    
    def make_sound(self):
        print("Roar Roar")
    
    def breathe(self):
        print("Breathe in air")
        
class Shark(Lion):
    def __init__(self,age_in_months,required_food_in_kgs,breed):
        super().__init__(age_in_months,required_food_in_kgs,breed)
    
    def grow(self):
        self.required_food_in_kgs=self.required_food_in_kgs+8
        self.age_in_months=self.age_in_months+1
    
    def make_sound(self):
        print("Shark Sound")
    
    def breathe(self):
        print("Breathe oxygen from water")

