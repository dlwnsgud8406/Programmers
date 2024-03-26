def solution(answers):
    student_1 = [1, 2, 3, 4, 5] * 2000
    student_2 = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    student_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    score = [0] * 3
    top = []
    for i in range(len(answers)):
        if answers[i] == student_1[i]:
            score[0] += 1
        if answers[i] == student_2[i]:
            score[1] += 1
        if answers[i] == student_3[i]:
            score[2] += 1
    for i in range(3):
        if max(score) == score[i]:
            top.append(i+1)
    return top
