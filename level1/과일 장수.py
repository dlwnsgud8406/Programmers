def solution(k, m, score):
    answer = 0
    score = sorted(score, reverse = True)
    for i in range(len(score) // m):
        arr = score[m*i:m*i+m]
        answer += (min(arr) * len(arr))
    return answer
