def solution(myString, pat):
    answer = ''
    arr = []
    for char in myString:
        answer += char
        if answer[len(answer)-len(pat):len(answer)] == pat:
            arr.append(answer)
    return (max(arr))
