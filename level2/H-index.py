def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for idx, citation in enumerate(citations):
        if idx >= citation:
            return idx
    return len(citations)
