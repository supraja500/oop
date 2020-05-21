import  math
class ComplexNumber:
    
    
    def __init__(self,real_part=0,imaginary_part=0):
        
        
        if type(real_part) is str and type(imaginary_part) is str:
            raise ValueError("Invalid value for real and imaginary part")
        elif type(real_part) is str:
            raise ValueError("Invalid value for real part")
        elif type(imaginary_part) is str:
            raise ValueError("Invalid value for imaginary part")
        else:
            self.real_part=real_part
            self.imaginary_part=imaginary_part
                    

        
    def conjugate(self):
         return ComplexNumber(self.real_part,-self.imaginary_part)
        
    
    def __add__(self,other):
        return ComplexNumber(self.real_part+other.real_part,self.imaginary_part+other.imaginary_part)
    
    def __sub__(self,other):
        return ComplexNumber(self.real_part-other.real_part,self.imaginary_part-other.imaginary_part)
  
    def __mul__(self, other):
        return ComplexNumber(self.real_part*other.real_part - self.imaginary_part*other.imaginary_part,
                       self.imaginary_part*other.real_part + self.real_part*other.imaginary_part)
    
    def __truediv__(self, other):
        sr, si, oR, oi = self.real_part, self.imaginary_part,other.real_part, other.imaginary_part
        r = float(oR**2 + oi**2)
        return ComplexNumber((sr*oR+si*oi)/r, (si*oR-sr*oi)/r)
    def __abs__(self):
        return round(math.sqrt(self.real_part**2 + self.imaginary_part**2),3)
    
    def __eq__(self, other):
        return self.real_part == other.real_part and self.imaginary_part == other.imaginary_part

    def __str__(self):
        return "{}{:+}i".format(self.real_part,self.imaginary_part)  
        
        
        
        
    

