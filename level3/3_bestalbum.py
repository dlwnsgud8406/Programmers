def solution(genres, plays):
    answer = []
    genre_hash = {}
    genre_sum_hash = {}
    for genre in genres:
        genre_hash[genre] = []
        genre_sum_hash[genre] = 0
    for i in range(len(genres)):
        genre_hash[genres[i]].append((plays[i], i))
        genre_sum_hash[genres[i]] += plays[i]
    genre_sum_hash = sorted(genre_sum_hash.items(), key = lambda x:x[1], reverse = True)
    for genre in genre_hash:
        genre_hash[genre].sort(key = lambda x:(-x[0], x[1]))
    
    for genre in genre_sum_hash:
        for i in range(min(len(genre_hash[genre[0]]), 2)):
            answer.append(genre_hash[genre[0]][i][1])

    return answer

genres=["classic", "pop", "classic", "classic", "pop", "hip", "hip"]	
plays=[500, 600, 150, 800, 2500, 1300, 1000]
print(solution(genres, plays))
solution(genres, plays)