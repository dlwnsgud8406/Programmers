# mycode
# def solution(k, tangerine):
#     answer = 0
#     tangerine = sorted(tangerine, key=lambda x: (-tangerine.count(x), tangerine.index(x)))
#     while(len(tangerine) > k):
#         tangerine.pop()
#     answer = len(set(tangerine))
#     return answer
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
# k = 6
# tangerine = [1, 3, 2, 5, 4, 5, 2, 3]

# k = 4
# tangerine = [1, 3, 2, 5, 4, 5, 2, 3]

k = 2
tangerine = [1, 1, 1, 1, 2, 2, 2, 3]

print(solution(k, tangerine))