
def solution(str1, str2):
    answer = 0
    st = [chr(a) for a in range(65,91)]

    inter = list()

    str1 = str1.upper()
    li1 = list()
    for i in range(len(str1)-1):
        if str1[i] in st:
            if str1[i+1] in st:
                li1.append(str1[i]+str1[i+1])   

    str2 = str2.upper()
    li2 = list()
    for i in range(len(str2)-1):
        if str2[i] in st:
            if str2[i+1] in st:
                tmp = str2[i]+str2[i+1]
                if tmp in li1:
                    idx = li1.index(tmp)
                    li1.pop(idx)
                    inter.append(tmp)
                else:
                    li2.append(tmp)
    x = len(inter)
    y = x + len(li1)+len(li2)
    if y == 0:
        answer = 65536
    else:
        answer = int(x*65536/y)
    return answer


print("solution",solution("FRANCE","french"))
print("solution",solution("handshake","shake hands"))
print("solution",solution("aa1+aa2","AAAA12"))
print("solution",solution("E=M*C^2","e=m*c^2"))


