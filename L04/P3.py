import numpy as np

def normalize(v: np.ndarray) -> np.ndarray:

    norm_v = np.linalg.norm(v)
    
    if norm_v == 0:
        return np.zeros_like(v)
    
    return v / norm_v

if __name__ == '__main__':
    
    # Example 1: 2D vector
    v = np.array([3, 4])
    u = normalize(v)
    print('u =', u)
    print('u.T @ v =', u.T @ v)
    print('size u=', np.sqrt(u[0]**2 + u[1]**2))
    print("-" * 20)
    
    # Example 2: 3D vector
    v = np.array([3, 4, 2])
    u = normalize(v)
    print('u =', u)
    print('u.T @ v =', u.T @ v)
    print('size u=', np.sqrt(u[0]**2 + u[1]**2 + u[2]**2))
    print("-" * 20)
    
    # Example 3: 4D vector
    v = np.array([3, 4, 2, 5])
    u = normalize(v)
    print('u =', u)
    print('u.T @ v =', u.T @ v)
    print('size u=', np.sqrt(u[0]**2 + u[1]**2 + u[2]**2 + u[3]**2))
    print("-" * 20)