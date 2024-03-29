def solution(today, terms, privacies):
    answer = []
    terms_hash = {}
    for term in terms:
        kind, duration = term.split(' ')
        terms_hash[kind] = int(duration) * 28

    today_year, today_month, today_day = map(int, today.split('.'))
    today_days = (today_year * 12 + today_month) * 28 + today_day

    for i in range(len(privacies)):
        date, kind = privacies[i].split(' ')
        year, month, day = map(int, date.split('.'))
        privacy_days = (year * 12 + month) * 28 + day + terms_hash[kind]
        if today_days >= privacy_days:
            answer.append(i + 1)
    return answer
