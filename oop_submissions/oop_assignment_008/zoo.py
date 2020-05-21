class Animal:
    increase_required_food_in_kgs=2
    increase_age_in_month=1
    def __init__(self,age_in_months,required_food_in_kgs,breed):
        if age_in_months>1:
            raise ValueError("Invalid value for field age_in_months: {}".format(age_in_months))
        else:
            self._age_in_months=age_in_months
        if required_food_in_kgs<=0:
           raise ValueError("Invalid value for field required_food_in_kgs: {}".format(required_food_in_kgs))
        else:
            self._required_food_in_kgs=required_food_in_kgs
        self._breed=breed
      
    def grow(self):
        self._required_food_in_kgs+=self.increase_required_food_in_kgs
        self._age_in_months+=self.increase_age_in_month
        
    def make_sound(self):
        print("Buck Buck")
    @property    
    def age_in_months(self):
        return self._age_in_months
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
    @property
    def breed(self):
        return self._breed
class Land_Animal:
    @classmethod    
    def breathe(self):
        print("Breathe in air")
class Water_Animal:
    @classmethod    
    def breathe(self):
        print("Breathe oxygen from water")
class Hunting:
    def hunt(self,zoos):
        if 'Deer' in zoos._inst_list:
            zoos.inst_list.remove('Deer')
        else:
            print("No deers to hunt")
class Deer(Animal,Land_Animal):
    increase_required_food_in_kgs=2
    increase_age_in_month=1
    @classmethod  
    def make_sound(cls):
        print("Buck Buck")
class Lion(Animal,Land_Animal,Hunting):
    increase_required_food_in_kgs=4
    increase_age_in_month=1
    @classmethod      
    def make_sound(cls):
         print("Roar Roar")
class Shark(Animal,Water_Animal):
    increase_required_food_in_kgs=8
    increase_age_in_month=1
    @classmethod  
    def make_sound(cls):
        print("Shark Sound")
    def hunt(self,zoos):
        if 'GoldFish' in zoos._inst_list:
            zoos.inst_list.remove('GoldFish')
        else:
            print("No GoldFish to hunt")
class GoldFish(Animal,Water_Animal):
      increase_required_food_in_kgs=0.2
      increase_age_in_month=1
      @classmethod  
      def make_sound(cls):
          print("Hum Hum")
class Snake(Animal,Land_Animal,Hunting):
      increase_required_food_in_kgs=0.5
      increase_age_in_month=1
      @classmethod  
      def make_sound(cls):
          print("Hiss Hiss")
class Zoo:
    total_list=[]
    def __init__(self):
        self._reserved_food_in_kgs=0
        self._inst_list=[]
    @property
    def inst_list(self):
        return self._inst_list
    @property
    def reserved_food_in_kgs(self):
        return self._reserved_food_in_kgs
        
    def add_food_to_reserve(self,food_1):
        self._reserved_food_in_kgs+=food_1
    def count_animals(self):
        return len(self._inst_list)
    def add_animal(self,animal):
        self.total_list.append(type(animal).__name__)
        self._inst_list.append(type(animal).__name__)
    def feed(self,animal):
        if self._reserved_food_in_kgs>0:
            self._reserved_food_in_kgs-=animal._required_food_in_kgs
            animal.grow()
    @classmethod
    def count_animals_in_all_zoos(cls):
        return (len(cls.total_list))
    @staticmethod
    def count_animals_in_given_zoos(zoos):
        count=0
        for i in zoos:
            count+=i.count_animals()
        return count
            


