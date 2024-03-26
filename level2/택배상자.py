def solution(order):
    answer = 0
    arr = []
    count = 1
    while count != len(order) + 1:
        arr.append(count)
        while arr and arr[-1] == order[answer]:
            answer += 1
            arr.pop()
        count += 1
    return answer
