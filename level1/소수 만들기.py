from itertools import combinations


def solution(nums):
    answer = 0
    nums = list(combinations(nums, 3))
    for arr in nums:
        cd = []
        Sum = sum(arr)
        for i in range(1, Sum + 1):
            if Sum / i == int(Sum / i):
                cd.append(i)
        if len(cd) == 2:
            answer += 1
    return answer
