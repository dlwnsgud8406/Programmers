def solution(x, y, n):
    dp = [float('inf')] * (1000001)
    dp[x] = 0
    for i in range(x, y):
        if dp[y] != float('inf'):
            return dp[y]
        for value in (i + n, i * 2, i * 3):
            if value > 1000000:
                continue
            dp[value] = min(dp[value], dp[i] + 1)

    return dp[y] if dp[y] != float('inf') else -1
