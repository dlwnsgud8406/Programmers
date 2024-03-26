def solution(s):
    answer = []
    receive = ''
    for i in range(len(s)):
        try:
            cur = receive.rindex(s[i])
        except ValueError:
            answer.append(-1)
        else:
            answer.append(i - cur)

        receive += s[i]
    return answer

print(solution('foobar'))
