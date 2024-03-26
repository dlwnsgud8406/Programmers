def solution(dartResult):
    num = ''
    arr = []
    for char in dartResult:
        if char not in 'SDT*#':
            num += char
        else:
            if char == 'S':
                arr.append(int(num))
            elif char == 'D':
                arr.append(int(num) ** 2)
            elif char == 'T':
                arr.append(int(num) ** 3)
            elif char == '*':
                if len(arr) == 1:
                    arr[len(arr)-1] *= 2
                elif len(arr) >= 2:
                    arr[len(arr)-1] *= 2
                    arr[len(arr)-2] *= 2
            elif char == '#':
                arr[len(arr)-1] *= -1
            num = ''
    return sum(arr)
