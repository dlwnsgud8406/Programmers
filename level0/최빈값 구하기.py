from collections import Counter
def solution(array):
    arr = Counter(array).most_common(2)
    if len(arr) > 1 and arr[0][1] == arr[1][1]:
        return -1
    else:
        return arr[0][0]
