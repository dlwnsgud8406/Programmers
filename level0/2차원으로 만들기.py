def solution(num_list, n):
    answer = []
    count = 0
    while count < len(num_list):
        arr = []
        for i in range(n):
            arr.append(num_list[count])
            count += 1
        answer.append(arr)
    return answer
