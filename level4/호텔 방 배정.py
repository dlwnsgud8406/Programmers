from collections import deque
def solution(k, room_number):
    answer = []
    room = deque([i+1 for i in range(k)])
    # print(room)
    for i in room_number:
        if i not in room:
            answer.append(room.popleft())
        else:
            room.remove(i)
            answer.append(i)
    return answer

print(solution(4, [4,4,4,4]))