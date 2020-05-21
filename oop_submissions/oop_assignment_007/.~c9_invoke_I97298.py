class Deer:
    def __init__(self,age_in_months,required_food_in_kgs,breed):
        #self.age_in_months=age_in_months
        self.required_food_in_kgs=required_food_in_kgs
        self.breed=breed
        if age_in_months==1:
            self.age_in_months=age_in_months
        else:
            raise ValueError("Invalid value for field age_in_months: {}".format(age_in_months))
            
    def grow(self):
        self.required_food_in_kgs=self.required_food_in_kgs+2
        return self.required_food_in_kgs
    def make_sound(self):
        return "Buck Buck"
    def breath(self):
        return "Breath in air"
        
class Lion(Deer):
    def grow(self):
        self.required_food_in_kgs=self.required_food_in_kgs+2
        return self.required_food_in_kgs
    def make_sound(self):
        return "Roar Roar"
    def breath(self):
        return ""
    
    