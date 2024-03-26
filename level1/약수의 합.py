def solution(n):
    answer = 0
    arr = []
    for i in range(1, n+1):
        if n / i == int(n/i):
            arr.append(i)

    return sum(arr)
