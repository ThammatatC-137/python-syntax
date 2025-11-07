import numpy as np
def innerprod(x: np.ndarray, y: np.ndarray) -> np.number:
    return np.dot(x.conj(), y)
if __name__ == '__main__':
    # Invocation example 1: Real numbers
    v = np.array([3, 4, 5, 6])
    u = np.array([1, -1, 0, 2.5])
    p = innerprod(v, u)
    print(f'⟨v | u⟩ = {p}')
    
    p = innerprod(u, v)
    print(f'⟨u | v⟩ = {p}')
    print("-" * 20)

    # Invocation example 2: Complex numbers
    v_c = np.array([3 + 5j, -4j, 0, 1 - 1j, 6 + 9j])
    u_c = np.array([2 - 1j, -1.2, 7 + 8j, 3 - 5j, 1.1 + 2j])
    p = innerprod(v_c, u_c)
    print(f'⟨v | u⟩ = {p}')
    
    p = innerprod(u_c, v_c)
    print(f'⟨u | v⟩ = {p}')