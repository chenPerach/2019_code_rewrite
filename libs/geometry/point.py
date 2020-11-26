import math
class vector:
    def __init__(self,x:float,y:float):
        self.x
        self.y
    
    def __add__(self,vec:vector):
        return vector(self.x - vec.x,self.y - vec.y)
    
    def size(self):
        return math.sqrt(math.pow(self.x,2) + math.pow(self.y,2))

    def normelize(self):
        angle = math.atan2(x=self.x,y=self.y)
        return vector(math.cos(angle),math.sin(angle))
    
    def slope(self):
        return float(y/x)
    
    def __sub__(self,vec:vector):
        return vector(self.x - vec.x,self.y - vec.y)
