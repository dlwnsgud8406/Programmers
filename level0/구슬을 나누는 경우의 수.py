def solution(balls, share):
    answer = 0
    case_up = case_down = 1
    count = share
    for i in range(count):
        case_up *= balls
        case_down *= share
        balls -= 1
        share -= 1
    return case_up / case_down
