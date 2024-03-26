def solution(myStr):
    answer = []
    string = ''
    for char in myStr:
        if char in 'abc':
            if len(string):
                answer.append(string)
            string = ''
        else:
            string += char
    if len(string):
        answer.append(string)
    if not len(answer):
        answer = ['EMPTY']
    return answer
