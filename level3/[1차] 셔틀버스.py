def solution(n, t, m, timetable):
    answer = 0

    timetable_min = [int(time[:2])*60 + int(time[3:]) for time in timetable]
    timetable_min.sort()

    bustime_min = [9*60 + t*i for i in range(n)]

    idx = 0
    for bus in bustime_min:
        crew = 0
        while crew < m and idx < len(timetable_min) and timetable_min[idx] <= bus:
            idx += 1
            crew += 1
        if crew < m:
            answer = bus
        else:
            answer = timetable_min[idx-1] - 1

    return str(answer//60).zfill(2) + ":" + str(answer%60).zfill(2)
