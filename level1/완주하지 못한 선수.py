from collections import Counter
def solution(participant, completion):
    return ((Counter(participant) - Counter(completion)).most_common(1)[0][0])


def solution(participant, completion):
    race = {}
    for person in participant:
        try:
            race[person] += 1
        except KeyError:
            race[person] = 1
    for person in completion:
        race[person] -= 1
    for person in race:
        if race[person] != 0:
            return person