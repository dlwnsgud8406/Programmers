import math
def solution(n, stations, w):
    answer = 0
    count = 0
    route=[]
    route = [0] * n
    for i in range(len(stations)):
        route[stations[i]-1] = -1
        if stations[i]-w-1 < 0 :
            route[stations[i]+w-1] = -1
        elif stations[i]+w-1 > len(route)-1 :
            route[stations[i]-w-1] = -1 
        else:
            route[stations[i]-w-1] = -1
            route[stations[i]+w-1] = -1
    print(route)
    for i in range(len(route)):
        if route[i] == -1 :
            print("count : ", count)
            answer = answer + math.ceil(count/(1+2*w))
            count=0
        else:
            count += 1
    print(answer)

    return answer

N = 16
stations = [9]
W = 2
solution(N, stations, W)