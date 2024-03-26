def solution(picture, k):
    answer = []
    for i in range(len(picture)):
        string = ''
        for char in picture[i]:
            string += char * k
        for j in range(k):
            answer.append(string)
    return answer
