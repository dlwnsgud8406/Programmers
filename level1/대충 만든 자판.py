def solution(keymap, targets):
    answer = []
    hash_map = {}
    for i in range(65, 92):
        min_index = 101
        for key in keymap:
            try:
                index = key.index(chr(i))
            except ValueError:
                pass
            else:
                if min_index > index:
                    min_index = index
                    hash_map[chr(i)] = index + 1
    for target in targets:
        movements = 0
        for char in target:
            try:
                movement = hash_map[char]
            except KeyError:
                answer.append(-1)
                movements = -1
                break
            else:
                movements += movement
        if movements == -1:
            continue
        else:
            answer.append(movements)


    return answer