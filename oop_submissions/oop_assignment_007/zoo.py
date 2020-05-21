class Deer:
    def __init__(self,age_in_months,required_food_in_kgs,breed):
        self._breed=breed
        
        if age_in_months>1:
            raise ValueError("Invalid value for field age_in_months: {}".format(age_in_months))
        else:
            self._age_in_months=age_in_months
        if required_food_in_kgs<10:
            raise ValueError("Invalid value for field required_food_in_kgs: {}".format(required_food_in_kgs))
        else:
            self._required_food_in_kgs=required_food_in_kgs

            
            
    def grow(self):
        self._required_food_in_kgs=self._required_food_in_kgs+2
        self._age_in_months=self._age_in_months+1
        
    def make_sound(self):
        print("Buck Buck")
    def breathe(self):
        print("Breathe in air")
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
    @property
    def age_in_months(self):
        return self._age_in_months
    @property
    def breed(self):
        return self._breed
        
       
class Lion(Deer):
    def __init__(self,age_in_months,required_food_in_kgs,breed):
        self._breed=breed
        
        if age_in_months>1:
            raise ValueError("Invalid value for field age_in_months: {}".format(age_in_months))
        else:
            self._age_in_months=age_in_months
        if required_food_in_kgs<10:
            raise ValueError("Invalid value for field required_food_in_kgs: {}".format(required_food_in_kgs))
        else:
            self._required_food_in_kgs=required_food_in_kgs
        
        
    def grow(self):
        self._required_food_in_kgs=self._required_food_in_kgs+4
        self._age_in_months=self._age_in_months+1
    
    def make_sound(self):
        print("Roar Roar")
    
    def breathe(self):
        print("Breathe in air")
    @classmethod   
    def hunt(cls):
        pass
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
    @property
    def age_in_months(self):
        return self._age_in_months
    @property
    def breed(self):
        return self._breed
        
class Shark(Lion):
    def __init__(self,age_in_months,required_food_in_kgs,breed):
        self._breed=breed
        if age_in_months>1:
            raise ValueError("Invalid value for field age_in_months: {}".format(age_in_months))
        else:
            self._age_in_months=age_in_months
        if required_food_in_kgs<10:
            raise ValueError("Invalid value for field required_food_in_kgs: {}".format(required_food_in_kgs))
        else:
            self._required_food_in_kgs=required_food_in_kgs
        
    def grow(self):
        self._required_food_in_kgs=self._required_food_in_kgs+8
        self._age_in_months=self._age_in_months+1
    
    def make_sound(self):
        print("Shark Sound")
    
    def breathe(self):
        print("Breathe oxygen from water")
        
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
    @property
    def age_in_months(self):
        return self._age_in_months
    @property
    def breed(self):
        return self._breed

class GoldFish(Shark):
    def __init__(self,age_in_months,required_food_in_kgs,breed):
        self._breed=breed
        if age_in_months>1:
            raise ValueError("Invalid value for field age_in_months: {}".format(age_in_months))
        else:
            self._age_in_months=age_in_months
        if required_food_in_kgs<=0:
            raise ValueError("Invalid value for field required_food_in_kgs: {}".format(required_food_in_kgs))
        else:
            self._required_food_in_kgs=required_food_in_kgs
    def grow(self):
        self._required_food_in_kgs=self._required_food_in_kgs+0.2
        self._age_in_months=self._age_in_months+1
    
    def make_sound(self):
        print("Hum Hum")

    def breathe(self):
        print("Breathe oxygen from water")
        
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
    @property
    def age_in_months(self):
        return self._age_in_months
    @property
    def breed(self):
        return self._breed
class Snake(GoldFish):
    def __init__(self,age_in_months,required_food_in_kgs,breed):
        self._breed=breed
        if age_in_months>1:
            raise ValueError("Invalid value for field age_in_months: {}".format(age_in_months))
        else:
            self._age_in_months=age_in_months
        if required_food_in_kgs<=0:
            raise ValueError("Invalid value for field required_food_in_kgs: {}".format(required_food_in_kgs))
        else:
            self._required_food_in_kgs=required_food_in_kgs
    def grow(self):
        self._required_food_in_kgs=self._required_food_in_kgs+0.5
        self._age_in_months=self._age_in_months+1
   
    def make_sound(self):
        print("Hiss Hiss")
    
    def breathe(self):
        print("Breathe in air")
    
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
    @property
    def age_in_months(self):
        return self._age_in_months
    @property
    def breed(self):
        return self._breed
        
class Zoo:
    def __init__(self):
        self.reserved_food_in_kgs=0
        self.count=0
        #self.age_in_months=1
        
        
    def add_food_to_reserve(self,food1):
        self.reserved_food_in_kgs=self.reserved_food_in_kgs+food1
        return self.reserved_food_in_kgs
        
    def add_animal(self,animal):
        self.count=self.count+1
        
        
    def count_animals(self):
        return self.count
        
    
            
    @classmethod
    def count_animals_in_all_zoos(self):
        pass
    @staticmethod
    def count_animals_in_given_zoos(self):
        pass
    

"""
from zoo import Zoo
zoo = Zoo()
print(zoo.reserved_food_in_kgs)

zoo.add_food_to_reserve(10000000)
print(zoo.reserved_food_in_kgs)
#10000000
gold_fish = GoldFish(age_in_months=1, breed="Nemo", required_food_in_kgs=0.5)
zoo.add_animal(gold_fish)
print(zoo.count_animals())
print(zoo.reserved_food_in_kgs)
#10000000
print(zoo.feed(gold_fish))
print(zoo.reserved_food_in_kgs)
#9999999.5
print(gold_fish.age_in_months)
nehru_zoological_park = Zoo()
zoo.add_food_to_reserve(10000000)
lion = Lion(age_in_months=1, breed="African Lion", required_food_in_kgs=15)
nehru_zoological_park.add_animal(lion)
nehru_zoological_park.count_animals()
Zoo.count_animals_in_all_zoos()
Zoo.count_animals_in_given_zoos([zoo])
from zoo import Deer
deer = Deer(age_in_months=1, breed="ELK", required_food_in_kgs=10)
nehru_zoological_park.add_animal(deer)
nehru_zoological_park.count_animals()

print(lion.hunt(nehru_zoological_park))
print(nehru_zoological_park.count_animals())

print(lion.hunt(nehru_zoological_park)) # Prints

"""       

    