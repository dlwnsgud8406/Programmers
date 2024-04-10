def solution(k, d):
    answer = 0
    round_square = d ** 2

    x = 0
    while x <= d:
        max_v = int((round_square - x ** 2) ** 0.5)
        rest = max_v % k
        answer += (max_v - rest) / k + 1
        x += k


    return answer
