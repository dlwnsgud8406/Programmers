def solution(arr):
    answer = [[]]

    for length in arr:
        while len(arr) > len(length):
            length.append(0)
        while len(arr) < len(length):
            arr.append([0] * len(length))
    return arr
