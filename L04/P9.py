import numpy as np

class Sphere:
    def __init__(self, C, r, col=(128,128,128)):
        self.C = C
        self.r = r
        self.color = col
    def ray(self, O, V):
        self.O = O
        self.V = V

        a = np.dot(self.V - self.O, self.V - self.O)
        b = 2 * np.dot(self.O - self.C, self.V - self.O)
        c = np.dot(self.O - self.C, self.O - self.C) - self.r**2 
    
        value = b**2 - 4*a*c
        if value < 0:
            return np.inf
        sqrt = np.sqrt(value)
        
        if value > 0:
            t = (-b-sqrt)/(2*a)
            return t
        elif value == 0:
            t = -b/(2*a)
            return t
        
          
if __name__ == '__main__':
    s1 = Sphere(np.array((0, 0, 80)), 20, (220, 180, 40))
    O = np.array((0,0,0))
    V1 = np.array((-40, 0, 50))
    t = s1.ray(O, V1)
    print('t = {:.3f}'.format(t))
    V2 = np.array((0, 0, 50))
    t = s1.ray(O, V2)
    print('t = {:.3f}'.format(t))
    V3 = np.array((10, 0, 50))
    t = s1.ray(O, V3)
    print('t = {:.3f}'.format(t))