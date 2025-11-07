import numpy as np


def innerprod(x, y):
    return np.dot(x, y)

class Face:
    def __init__(self, A, B, C, col=(128, 128, 128)):
        self.A = A
        self.B = B
        self.C = C
        self.color = col

        BA = self.B - self.A
        CA = self.C - self.A
        
        cross_product = np.cross(BA, CA)
        norm = np.linalg.norm(cross_product)
        

        if norm == 0:
            self.normal = np.array([0., 0., 0.])
            self.k = 0
            self.is_degenerate = True
        else:
            self.normal = cross_product / norm
   
            self.k = innerprod(self.normal, self.A)
            self.is_degenerate = False

    def ray(self, O, V):
        if self.is_degenerate:
            return np.inf


        ray_direction = V - O
        
        # Check if ray is parallel to the plane
        denominator = innerprod(self.normal, ray_direction)
        
        # Using a small tolerance to handle floating point inaccuracies
        if np.abs(denominator) < 1e-6:
            return np.inf
        
        numerator = self.k - innerprod(self.normal, O)
        t = numerator / denominator
        
        # If t is negative, the intersection is behind the camera
        if t < 0:
            return np.inf
        
        # Step 4: Determine if the intersection lies within the face boundaries
        Q = O + t * ray_direction

        # Inside-outside test using cross products
        test1 = innerprod(np.cross(self.B - self.A, Q - self.A), self.normal) >= 0
        test2 = innerprod(np.cross(self.C - self.B, Q - self.B), self.normal) >= 0
        test3 = innerprod(np.cross(self.A - self.C, Q - self.C), self.normal) >= 0
        
        # If all three tests pass, the point is inside the triangle
        if test1 and test2 and test3:
            return t
        else:
            return np.inf

if __name__ == '__main__':
    # Invocation example based on the user's request.
    f1 = Face(np.array((0, 20, 80)),
              np.array((-20, -10, 80)),
              np.array((20, -10, 80)),
              (240, 200, 100))
              
    O = np.array((0, 0, 0))

    # Test case 1: Ray misses the triangle
    V1 = np.array((-40, 0, 50))
    t = f1.ray(O, V1)
    print('t = {:.3f}'.format(t))

    # Test case 2: Ray hits the triangle
    V2 = np.array((0, 0, 50))
    t = f1.ray(O, V2)
    print('t = {:.3f}'.format(t))