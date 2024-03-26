def solution(m, musicinfos):
    answer = ''
    arr = []
    m = (m.replace('C#', 'c')).replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
    for musicinfo in musicinfos:
        string = ''
        start_time, end_time, name, melody = musicinfo.split(',')
        end_hour, end_minute = map(int, end_time.split(':'))
        start_hour, start_minute = map(int, start_time.split(':'))
        t = (end_hour - start_hour) * 60 + end_minute - start_minute
        melody = (melody.replace('C#', 'c')).replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
        while len(string) < t:
            string += melody
        if len(string) != t:
            string += melody
            string = string[:t]
        if m in string:
            arr.append((name, t))
    arr = sorted(arr, key = lambda x:x[1], reverse = True)
    if not arr:
        return "(None)"
    else:
        return arr[0][0]
    return answer
