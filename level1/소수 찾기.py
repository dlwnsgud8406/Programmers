def solution(n):
    answer = 0
    arr= [True for i in range(n+1)]
    for i in range(2, int(n ** (1 / 2)) + 1):
        if arr[i] == True:
            j = 2
            while i * j <= n:
                arr[i*j] = False
                j += 1
    for i in range(2,n+1):
        if arr[i]:
            answer+=1
    return answer
