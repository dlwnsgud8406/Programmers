def solution(name, yearning, photo):
    answer = []
    dict = {}
    for i in range(len(name)):
        dict[name[i]] = yearning[i]
    for arr in photo:
        score = 0
        for n in arr:
            try:
                score += dict[n]
            except KeyError:
                pass
        answer.append(score)

    return answer
print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may"],["kein", "deny", "may"], ["kon", "coni"]]))
