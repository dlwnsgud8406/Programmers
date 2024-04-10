def solution(players, callings):
    # players의 요소와 해당 인덱스를 매핑하는 딕셔너리 생성
    index_map = {player: i for i, player in enumerate(players)}

    for calling in callings:
        idx = index_map[calling]

        # 바로 앞 요소의 인덱스 계산 (원형 리스트로 간주)
        prev_idx = (idx - 1) % len(players)

        # players 리스트 내에서 요소 위치 교환
        players[idx], players[prev_idx] = players[prev_idx], players[idx]

        # 인덱스 맵 업데이트
        index_map[players[prev_idx]] = prev_idx
        index_map[players[idx]] = idx

    return players
