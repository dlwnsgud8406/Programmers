def solution(triangle):
    answer = 0
    length = len(triangle)
    sum = [[0]*length for _ in range(length)]
    sum[0][0] = triangle[0][0]

    for x in range(1, length):
        for y in range(0, len(triangle[x])):
            if y == 0:
                sum[x][y] = triangle[x][0] + sum[x-1][0]
            elif x == y:
                sum[x][y] = triangle[x][y] + sum[x-1][y-1]
            else:
                sum[x][y] = triangle[x][y] + max(sum[x-1][y-1], sum[x-1][y])
    answer = max(sum[-1])
    return answer

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))