def solution(t, p):
    answer = 0
    for i in range(len(t) - len(p) + 1):
        if int(t[i : len(p) + i]) <= int(p):
            print(int(t[i : len(p) + i]))
            answer += 1
    return answer
print(solution("3141592", "271"))
