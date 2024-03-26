def solution(n, words):
    p = [words[0][0]]
    for i, w in enumerate(words):
        if w not in p and p[-1][-1] == w[0]:
            p.append(w)
        else:
            return [i % n + 1, (i//n)+1]
    return [0, 0]


n = 3 
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]

# n = 5
# words = ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]

# n = 2
# words = ["hello", "one", "even", "never", "now", "world", "draw"]
print(solution(n, words))