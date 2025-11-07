import math

def calculate_exp_series():
    x_input = input("x: ")
    m_input = input("M: ")
    x = float(x_input)
    M = int(m_input)
    s = 1.0
    x_power = 1.0
    n_factorial = 1.0
    for n in range(1, M + 1):
        x_power *= x
        n_factorial *= n
        s += x_power / n_factorial
    print("s = {:.5f}".format(s))

if __name__ == '__main__':
    calculate_exp_series()