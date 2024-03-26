from collections import Counter
def solution(strArr):
    answer = 0
    arr = []
    for word in strArr:
        arr.append(len(word))
    dict = Counter(arr)
    return max(dict.most_common(1))[1]
