def solution(k):
    answer = 0
    for n in range(1,k+1):
        count = 0
        for i in range(1,n+1):
            if n%i == 0:
                count += 1
        if count > 2 :
            answer += 1
    return answer
