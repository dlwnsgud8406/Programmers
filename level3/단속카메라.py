def solution(routes):
    answer = 0
    routes.sort(key = lambda x:x[1])
    start_position = -30001
    
    for route in routes:
        if route[0] > start_position:
            answer += 1
            start_position = route[1]
        
    return answer