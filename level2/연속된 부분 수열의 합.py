def solution(sequence, k):
    answer = []
    count = 0
    interval_sum = 0
    end = 0
    if k in sequence:
        return [sequence.index(k), sequence.index(k)]
    for start in range(len(sequence)):
        while interval_sum < k and end < len(sequence):
            interval_sum += sequence[end]
            end += 1
        if interval_sum == k and start < end:
            answer.append([start, end-1])
        interval_sum -= sequence[start]
    answer = sorted(answer, key = lambda x:(x[1]-x[0]))
    return answer[0]
