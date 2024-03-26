
def solution(n, s):
    answer = []
    if s // n == 0:
        answer.append(-1)
    else :
        while (n):
            answer.append(s // n)
            s = s - s // n
            n = n - 1
    print(answer)
    return answer

solution(4,9)

# 3,9 .  => 27 

# 3, 8 => 3 3 2