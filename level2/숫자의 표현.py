def solution(n):
    answer = 0
    count = 1
    sum = 0
    i = 1
    while(i<n+1):
        while(sum<n):
            sum += count
            count += 1
        if sum == n:
            answer += 1
        sum = 0
        count = 1 + i
        i += 1
    return answer
