from collections import Counter
def solution(s):
    answer = ''
    arr = Counter(s)
    for key, value in arr.items():
        if value == 1:
            answer += key
    return ''.join(sorted(answer))