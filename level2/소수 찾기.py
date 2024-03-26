from itertools import permutations
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def solution(numbers):
    answer = 0
    num_arr = []
    arr = []
    for i in range(1, len(numbers)+1):
        num_arr.extend(list(set(permutations(list(numbers), i))))
    for n in num_arr:
        arr.append(int(''.join(n)))
    for num in list(set(arr)):
        if isPrime(num):
            answer += 1
    return answer
