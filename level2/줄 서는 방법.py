from collections import deque
def solution(n, k):
    answer = []
    Case = [i for i in range(1, n+1)]
    factorial = []
    factorial = deque(factorial)
    tmp = 1
    for i in range(1, n):
        tmp *= i
        factorial.appendleft(tmp)

    for denom in factorial:
        q = int((k - 1) // denom)
        answer.append(Case.pop(q % len(Case)))

    answer.extend(Case)

    return answer
