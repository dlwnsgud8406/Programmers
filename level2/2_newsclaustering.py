
def check(str1):
    del_number = []
    for i in range(len(str1)):
        if str1[i][0:1] > 'z' or str1[i][0:1] < 'a':
            del_number.append(i)
        elif str1[i][1:2] > 'z' or str1[i][1:2] < 'a':
            del_number.append(i)
    for i in range(len(del_number)):
        str1.pop(del_number[i]-i)
    return str1
        
def solution(str1, str2):
    answer = 0
    clustering1 = []
    clustering2 = []
    union = []
    intersection = []
    i = 0
    j = 0
    str1 = str1.lower()
    str2 = str2.lower()

    for clustering in str1:
        clustering1.append(str1[i:i+2])
        i+=1
    for clustering in str2:
        clustering2.append(str2[j:j+2])
        j +=1

    clustering1.pop()
    clustering2.pop()
    clustering1 = check(clustering1)
    clustering2 = check(clustering2)
    if len(clustering1) == 0 and len(clustering2) == 0:
        return 65536
    temp = clustering1.copy()
    union = clustering1.copy()

    for i in clustering2:
        if i not in temp:
                union.append(i)
        else:
                temp.remove(i)

    for i in clustering2:
        if i in clustering1:
                clustering1.remove(i)
                intersection.append(i)
    
    answer = 65536 *(len(intersection)/len(union))
    return int(answer)


str1 = "E=M*C^2"
str2 = "e=m*c^2"

# str1 = "handshake"
# str2 = "shake hands"

# str1 = "aa1+aa2"
# str2 = "AAAA12"

# str1 = "FRANCE"
# str2 = "french"

print(solution(str1, str2))
