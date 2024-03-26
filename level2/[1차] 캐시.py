def solution(cacheSize, cities):
    answer = 0
    cache = []
    if cacheSize == 0:
        return 5*len(cities)
    else:
        for i in range(len(cities)):
            if cities[i].lower() not in cache:
                if len(cache) < cacheSize:
                    cache.append(cities[i].lower())
                elif len(cache) == cacheSize:
                    cache.pop(0)
                    cache.append(cities[i].lower())
                answer += 5
            else:
                cache.pop(cache.index(cities[i].lower()))
                cache.append(cities[i].lower())
                answer += 1
    return answer
