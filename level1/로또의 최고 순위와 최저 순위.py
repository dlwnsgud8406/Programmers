def solution(lottos, win_nums):
    count = 0
    lucky = 0
    for num in lottos:
        if num == 0:
            lucky += 1
        else:
            try:
                win_nums.remove(num)
                count += 1
            except ValueError:
                pass
    return [min(7 - (count + lucky), 6), min(7 - count, 6)]
