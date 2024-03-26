def solution(numbers):
    arr = [i for i in range(10)]
    for i in range(len(numbers)):
        arr.pop(arr.index(numbers[i]))
    return sum(arr)
