from collections import Counter
def solution(array, n):
    dict = Counter(array)
    return dict[n]
