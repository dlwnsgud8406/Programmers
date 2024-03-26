def solution(id_pw, db):
    answer = ''
    for user in db:
        if user[0] == id_pw[0]:
            if user[1] == id_pw[1]:
                answer = 'login'
                return answer
            else:
                answer = 'wrong pw'
                break
        else:
            answer = 'fail'
    return answer
