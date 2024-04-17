from collections import Counter


def solution(id_list, report, k):
    answer = []
    report_hash = {id_list[i]: set() for i in range(len(id_list))}
    is_reported = []
    report = list(set(report))

    for rep in report:
        a, b = rep.split(' ')
        report_hash[a].add(b)
        is_reported.append(b)

    filter_counter = Counter({key: value for key, value in Counter(is_reported).items() if value >= k})
    for name in report_hash:
        count = 0
        for key, value in filter_counter.items():
            if key in report_hash[name]:
                count += 1
        answer.append(count)

    return answer
