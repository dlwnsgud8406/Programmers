def solution(menu, order, k):
    answer = 0
    store = []
    room = []
    current_time = 0
    for i in range(len(order)):
        current_time = max(i * k, current_time)
        coffee_time = current_time + menu[order[i]]
        store.append((i*k, coffee_time))
        current_time = coffee_time

      # 각 구간의 시작과 종료 지점에 이벤트 추가
    for start, end in store:
        room.append((start, 'start'))
        room.append((end, 'end'))

    # 이벤트를 시간 순으로 정렬
    room.sort(key = lambda x:(x[0], x[1]))

    current_overlap = 0

    # 이벤트를 순회하면서 겹치는 구간의 수 계산
    for time, event_type in room:
        if event_type == 'start':
            current_overlap += 1
            answer = max(answer, current_overlap)
        elif event_type == 'end':
            current_overlap -= 1

    return answer
