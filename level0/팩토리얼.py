import math
def solution(n):
    for i in range(1, 11):
        if math.factorial(i) == n:
            return i
        elif math.factorial(i) > n:
            return i - 1
