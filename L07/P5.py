def P5_wer(ref, test):
    ref = list(ref)
    test = list(test)
    n = len(ref)
    m = len(test)

    # dp[i][j] = min operations to convert ref[:i] -> test[:j]
    dp = [[0]*(m+1) for _ in range(n+1)]

    # initialize base case
    for i in range(n+1):
        dp[i][0] = i  # delete all
    for j in range(m+1):
        dp[0][j] = j  # insert all

    # fill dp table
    for i in range(1, n+1):
        for j in range(1, m+1):
            if ref[i-1] == test[j-1]:
                dp[i][j] = dp[i-1][j-1]  # no operation
            else:
                substitute = dp[i-1][j-1] + 1
                insert = dp[i][j-1] + 1
                delete = dp[i-1][j] + 1
                dp[i][j] = min(substitute, insert, delete)

    # minimal operations
    min_ops = dp[n][m]
    wer = min_ops / n

    return (wer, min_ops)

if __name__ == "__main__":
    wer, n = P5_wer("grit", "greet")
    print("wer = {}, n = {}".format(wer, n))
