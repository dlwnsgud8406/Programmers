from collections import Counter
def solution(k, tangerine):
    answer = 0
    counter = Counter(tangerine)
    counter = sorted(counter.values())
    counts = 0
    while counts < k:
        counts += counter.pop()
        answer += 1
    return answer
