def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]

    compare1 = [0] * len(sticker)
    compare1[0], compare1[1] = sticker[0], max(sticker[0], sticker[1])
    for i in range(2, len(sticker) - 1):
        compare1[i] = max(compare1[i - 1], compare1[i - 2] + sticker[i])

    compare2 = [0] * len(sticker)
    compare2[0], compare2[1] = 0, sticker[1]
    for i in range(2, len(sticker)):
        compare2[i] = max(compare2[i - 1], compare2[i - 2] + sticker[i])

    return max(max(compare1), max(compare2))