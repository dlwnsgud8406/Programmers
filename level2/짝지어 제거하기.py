def solution(s):
    stack = []

    for i in s:
        if len(stack) == 0:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    if len(stack) == 0:
        return 1
    else:
        return 0

    # 현재 인덱스와 다음인덱스가 같으면 둘다 pop시킴을 반복