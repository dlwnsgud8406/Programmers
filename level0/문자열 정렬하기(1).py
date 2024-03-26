def solution(my_string):
    answer = []
    for num in my_string:
        if '0' <=num <= '9':
            answer.append(int(num))
    return sorted(answer)
