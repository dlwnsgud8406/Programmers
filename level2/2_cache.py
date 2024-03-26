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

cacheSize = 3
# cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
cities = ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]

# cacheSize = 2
# cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]

# cacheSize = 5
# cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]

# cacheSize = 2
# cities = ["Jeju", "Pangyo", "NewYork", "newyork"]

# cacheSize = 0
# cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]

print(solution(cacheSize, cities))