def laplace_smooth(counting, alpha):
    M = len(counting)
    N = sum(counting)
    denom = N + alpha * M
    return [(count + alpha) / denom for count in counting]

if __name__ == "__main__":
    counting = [0, 8, 20, 4, 12]
    res = laplace_smooth(counting, 0.1)
    print(res)
