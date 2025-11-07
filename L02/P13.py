def est_prob(counting):
    total = sum(counting)
    if total == 0:
        return [0.0 for _ in counting]
    return [count / total for count in counting]

if __name__ == "__main__":
    counting = [0, 8, 20, 4, 12]
    res = est_prob(counting)
    print(res)
