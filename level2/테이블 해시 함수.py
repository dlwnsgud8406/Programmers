def solution(board, col, row_begin, row_end):
    answer = 0
    step3_list = []

    # Step 2
    board.sort(key=lambda x: (x[col - 1], -x[0]))

    # Step 3
    for i in range(row_begin, row_end + 1):
        current_sum = 0
        for num in board[i - 1]:
            current_sum += num % i
        step3_list.append(current_sum)

    for num in step3_list:
        answer ^= num

    return answer
