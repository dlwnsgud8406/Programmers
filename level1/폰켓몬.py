def solution(nums):
    length = len(list(set(nums)))
    return min((len(nums))//2, length)