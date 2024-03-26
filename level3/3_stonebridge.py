#이분탐색문제로 접근해야함

def minus_check(stones, k):
    state = zero_check(stones, k)
    if state == 1 :
        return 1
    else :
        for i in range(len(stones)):
            if stones[i] > 0 :
                stones[i] -= 1

def zero_check(stones, k):
    zero_count = 0
    for i in range(len(stones)):
        if zero_count == k:
            return 1
        if stones[i] == 0 :  
            zero_count += 1
        else :
            zero_count = 0


def solution(stones, k):
    answer = 0
    if len(stones) == 1:
        return stones[0]
    elif len(stones) == k:
        return 1
    else:
        while minus_check(stones, k) != 1:
            answer += 1
    return answer

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 10))