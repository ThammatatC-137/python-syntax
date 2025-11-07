import numpy as np

def plane3d(Px: np.ndarray, Py: np.ndarray, n: np.ndarray, k: float) -> np.ndarray:
    nx, ny, nz = n
    z = (k - nx * Px - ny * Py) / nz
    return z
if __name__ == '__main__':
    n = np.array([0.57735027, 0.57735027, 0.57735027])
    k = 3
    x, y = 0, 0
    z = plane3d(x, y, n, k)
    print(f'p = ({x}, {y}, {z})')

    print("-" * 20)

    xs = np.linspace(-2, 2, 3)
    ys = np.linspace(-2, 2, 3)
    X, Y = np.meshgrid(xs, ys)
    Z = plane3d(X, Y, n, k)

    for i in range(3):
        for j in range(3):
            print(f'ps = ({X[i,j]}, {Y[i,j]}, {Z[i,j]})')