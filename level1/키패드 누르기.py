dict = {'1': [3, 0], '2' : [3, 1], '3' : [3, 2], '4' : [2, 0], '5' : [2, 1], '6' : [2, 2], '7' : [1, 0], '8' : [1, 1], '9' : [1, 2], '0' : [0, 1] }
def solution(numbers, hand):
    answer = ''
    left_cursor = [0, 0]
    right_cursor = [0, 2]
    numbers = list(map(str, numbers))
    for num in numbers:
        if int(num) == 1 or int(num) == 4 or int(num) == 7:
            answer += 'L'
            left_cursor = dict[num]
        elif int(num) == 3 or int(num) == 6 or int(num) == 9:
            answer += 'R'
            right_cursor = dict[num]
        else:
            x, y = dict[num]
            left_distance = (abs(x- left_cursor[0]) + abs(y - left_cursor[1]))
            right_distance = (abs(x - right_cursor[0]) + abs(y - right_cursor[1]))
            if left_distance < right_distance:
                answer += 'L'
                left_cursor = dict[num]
            elif left_distance > right_distance:
                answer += 'R'
                right_cursor = dict[num]
            else:
                if hand == 'left':
                    answer += 'L'
                    left_cursor = dict[num]
                elif hand == 'right':
                    answer += 'R'
                    right_cursor = dict[num]
    return answer
