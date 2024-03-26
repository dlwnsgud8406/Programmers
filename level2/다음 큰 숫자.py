def solution(n):
    binary = bin(n)[2:]
    for num in range(n+1, 1000000):
        next_binary = bin(num)[2:]
        if next_binary.count('1') == binary.count('1'):
            return num
