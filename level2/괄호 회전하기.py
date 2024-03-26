from collections import deque


def check(s):
    while True:
        if "()" in s:
            s = s.replace("()", "")
        elif "{}" in s:
            s = s.replace("{}", "")
        elif "[]" in s:
            s = s.replace("[]", "")
        else:
            return False if s else True


def solution(s):
    answer = 0
    que = deque(s)

    for _ in range(len(s)):
        if check(''.join(que)):
            answer = answer + 1
        que.rotate(-1)
    return answer
