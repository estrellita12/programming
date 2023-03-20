def solution(s):
    answer = []

    data = s
    cnt = 0
    loop = 0
    while len(data) > 1:
        cnt = cnt + data.count("0")
        data = data.replace("0","")
        b = bin(len(data))[2:]
        data = b
        loop = loop + 1
    answer = [loop,cnt]
    return answer


print("solution",solution("110010101001"))
print("solution",solution("01110"))
print("solution",solution("1111111"))

