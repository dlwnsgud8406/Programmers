def solution(n, l, r):
    answer = 0
    bits = ["1"]
    for i in range(20):
        temp_str = ""
        for bit in bits[-1]:
            if bit == "1":
                temp_str += "11011"
            elif bit == "0":
                temp_str += "00000"

        bits.append(temp_str)
        print(bits)

solution(1, 2, 3)
