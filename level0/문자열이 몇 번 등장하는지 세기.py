def solution(myString, pat):
    arr = []
    for i in range(len(myString)-len(pat) + 1):
        arr.append(myString[i:len(pat)+i])
    return arr.count(pat)
