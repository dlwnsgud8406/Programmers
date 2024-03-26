from math import gcd

def solution(arrayA, arrayB):
    arrayA, arrayB = list(set(arrayA)), list(set(arrayB))
    
    def find_gcd(arr):
        value = 0
        for i in range(len(arr)):
            value = gcd(value, arr[i])
        return value
    
    def check_gcd(arr, value):
        for i in range(len(arr)):
            if arr[i] % value == 0:
                return 0
        return value
    
    answer1, answer2 = find_gcd(arrayA), find_gcd(arrayB)
    answer1, answer2 = check_gcd(arrayB, answer1), check_gcd(arrayA, answer2)
    
    if not (answer1 or answer2):
        return 0
    else:
        return max(answer1, answer2)
    