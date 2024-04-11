diamond = {"diamond": 1, "iron": 1, "stone": 1}
iron = {"diamond": 5, "iron": 1, "stone": 1}
stone = {"diamond": 25, "iron": 5, "stone": 1}


def solution(picks, minerals):
    answer = 0

    diamond_tool, iron_tool, stone_tool = picks

    minerals = [minerals[i:i + 5] for i in range(0, len(minerals), 5)][:sum(picks)]
    minerals.sort(key=lambda x: (x.count('diamond'), x.count('iron'), x.count('stone')), reverse=True)

    for mineral in minerals:
        if diamond_tool > 0:
            for name in mineral:
                answer += diamond[name]
            diamond_tool -= 1

        elif iron_tool > 0:
            for name in mineral:
                answer += iron[name]
            iron_tool -= 1

        elif stone_tool > 0:
            for name in mineral:
                answer += stone[name]
            stone_tool -= 1

    return answer
