from collections import deque #deque 선언
def solution(s):
    answer = True
    check=0
    stack = deque(s) # input을 deque화 하기
    while(stack):
        bracket = stack.popleft()
        if bracket == "(" :
            check = check + 1
        else :
            check = check - 1
        if check < 0 :
            answer = False
            break
    if check > 0 :
        answer = False
    return answer
