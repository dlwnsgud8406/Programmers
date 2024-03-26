import math

def solution(arr):
    answer = arr[0]
    for n in arr:
        answer = int((n*answer) / math.gcd(n, answer))

    return answer
