def solution(a, b, c):
    answer = 0
    if a == b == c:
        answer = (3*a) * (3*(a**2)) * (3*(a**3))
    elif a == b != c or a != b == c or a == c != b:
        answer = (a + b + c) * (a**2 + b**2 + c**2)
    else:
        answer = a+b+c
    return answer
