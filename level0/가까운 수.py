def solution(array, n):
    array = sorted(array)
    arr = []
    for num in array:
        arr.append(abs(num - n))
    return array[arr.index(min(arr))]
