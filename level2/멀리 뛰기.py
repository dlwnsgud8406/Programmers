def solution(num):
    return (solution(num-1) + solution(num-2)) if num > 2 else num
