def solution(s):
    answer = True
    for char in s:
        if 65<=ord(char)<=122:
            return False
        if len(s) != 4 and len(s) != 6:
            return False
    return answer
