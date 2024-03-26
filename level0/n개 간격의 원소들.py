import math
def solution(num_list, n):
    answer = []
    for i in range(0, math.ceil(len(num_list)/n)):
        answer.append(num_list[i*n])
    return answer
