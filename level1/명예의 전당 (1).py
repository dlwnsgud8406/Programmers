def solution(k, score):
    answer = []
    hall_of_fame = []
    for i in range(len(score)):
        hall_of_fame.append(score[i])
        if len(hall_of_fame) > k:
            hall_of_fame.pop(hall_of_fame.index(min(hall_of_fame)))
        answer.append(min(hall_of_fame))

    return answer
