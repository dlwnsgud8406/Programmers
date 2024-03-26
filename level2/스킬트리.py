def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        index = []
        for s in skill:
            try:
                idx = skill_tree.index(s)
            except ValueError:
                index.append(99999)
            else:
                index.append(idx)
        if index == sorted(index):
            answer += 1
    return answer