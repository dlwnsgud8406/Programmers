def solution(spell, dic):
    string = ''.join(sorted(spell))
    for word in dic:
        string2 = ''.join(sorted(list(word)))
        if string in string2:
            return 1
    return 2
