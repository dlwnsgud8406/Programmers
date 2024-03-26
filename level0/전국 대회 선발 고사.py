def solution(rank, attendance):
    arr = []
    for i in range(len(attendance)):
        if attendance[i]:
            arr.append((rank[i], i))
    arr = sorted(arr, key = lambda x:x[0])
    while len(arr) > 3:
        arr.pop()
    return 10000 * arr[0][1] + 100 * arr[1][1] + arr[2][1]        
