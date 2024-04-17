def solution(scores):
    answer = 0
    target_a, target_b = scores[0]
    target_score = target_a + target_b

    # 첫번째 점수에 대해서 내림차순,
    # 첫 번째 점수가 같으면 두 번째 점수에 대해서 오름차순으로 정렬합니다.
    scores.sort(key=lambda x: (-x[0], x[1]))
    maxb = 0

    for a, b in scores:
        if target_a < a and target_b < b:
            return -1

        if b >= maxb:
            maxb = b
            if a + b > target_score:
                answer += 1

    return answer + 1


def solution(scores):
    hr, cor = scores[0]
    scores.sort(key=lambda x: (sum(x)))
    for i in range(len(scores)):
        if sum(scores[i]) >= hr + cor:
            del scores[:i]
            break

    scores.sort()
    scores_copy = scores.copy()
    length = len(scores_copy)
    cnt = 0

    for i in range(length):
        for j in range(i + 1, length):
            if scores_copy[i][0] < scores_copy[j][0] and scores_copy[i][1] < scores_copy[j][1]:
                if (scores[i - cnt][0], scores[i - cnt][1]) == (hr, cor):
                    return -1
                scores.pop(i - cnt)
                cnt += 1
                break

    scores.sort(key=lambda x: sum(x), reverse=True)

    for i in range(len(scores)):
        if scores[i][0] + scores[i][1] == hr + cor:
            return i + 1
