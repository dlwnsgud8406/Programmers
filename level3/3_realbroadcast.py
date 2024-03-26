import math

def solution(n, stations, w):
    lastCover = 0
    stationI = 0
    result = 0
    install = 0

    while(lastCover < n):
        if (stationI >= len(stations)):
            install = math.ceil((n - lastCover)/(2*w+1))
            result += install
            lastCover += install*(2*w+1)
        elif (lastCover < stations[stationI] - w - 1):
            install = math.ceil((stations[stationI] - w -1 -lastCover)/(2*w+1))
            result += install
            lastCover += install*(2*w+1)
        elif (lastCover >= stations[stationI] - w - 1):
            lastCover = stations[stationI] + w
            stationI += 1
    return result