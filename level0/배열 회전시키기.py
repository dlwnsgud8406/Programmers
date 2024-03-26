from collections import deque
def solution(numbers, direction):
    numbers = deque(numbers)
    if 'right' in direction:
        numbers.rotate(1)
    elif 'left' in direction:
        numbers.rotate(-1)
    return list(numbers)
print(solution([1,2,3], 'right'))
