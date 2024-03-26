def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    for computer in range(n):
        if visited[computer] == False:
            DFS(n, computers, computer, visited)
            answer += 1

    return answer


def DFS(n, computers, computer, visited):
    visited[computer] = True
    for connect in range(n):
        if connect != computer and computers[computer][connect] == 1:
            if not visited[connect]:
                DFS(n, computers, connect, visited)
