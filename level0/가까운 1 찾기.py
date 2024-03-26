def solution(arr, idx):
    for i in range(len(arr)):
        if arr[i] == 1 and i > idx-1:
            return i
    return -1
