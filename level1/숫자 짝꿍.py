def solution(X, Y):
    answer = []
    dict = {}
    for char in X:
        if char in dict:
            pass
        else:
            dict[char] = min(X.count(char), Y.count(char))
    print(dict)
    for arr in dict:
        while dict[arr] != 0:
            dict[arr] -= 1
            print(dict)
            answer.append(arr)
    answer = sorted(answer, reverse = True)
    if not len(answer):
        return ('-1')
    elif max(map(int, answer)) == 0:
        return ('0')
    else:
        return (''.join(answer))
print(solution('1000000002', '20200'))
