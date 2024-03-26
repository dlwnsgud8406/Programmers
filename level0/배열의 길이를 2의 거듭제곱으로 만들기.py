def solution(arr):
    current_num = 1
    blank = []
    while current_num < len(arr):
        current_num *= 2
    blank = [0] * (current_num - len(arr))
    arr.extend(blank)
    return arr
