def solution(tickets):
    answer = []
    n = len(tickets)
    visited = [0] * n

    def dfs(airport, path):
        if len(path) == n + 1:
            answer.append(path)
            return
        for i, ticket in enumerate(tickets):
            if airport == ticket[0] and not visited[i]:
                visited[i] = True
                dfs(ticket[1], path + [ticket[1]])
                visited[i] = False

    dfs("ICN", ["ICN"])
    answer.sort()
    return answer[0]
