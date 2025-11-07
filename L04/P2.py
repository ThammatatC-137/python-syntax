import numpy as np

def marrange(A: np.ndarray, B: np.ndarray) -> np.ndarray:

    return A.reshape(-1, 1) * B.reshape(1, -1)

if __name__ == '__main__':

    X = np.array([1, 2, 3])
    Y = np.array([0.5, 1, 5, 10])

    Z = marrange(X, Y)
    print(Z)