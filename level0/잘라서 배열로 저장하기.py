def solution(my_str, n):
    answer = []
    string = ''
    for i in range(len(my_str)):
        string += my_str[i]
        if len(string) == n:
            answer.append(string)
            string = ''
    if len(string):
        answer.append(string)
    return answer
