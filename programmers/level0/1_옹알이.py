
def solution(babbling):
    db = ["aya", "ye", "woo", "ma"]
    answer = 0
    for data in babbling:
        for k in db:
            data = data.replace(k," ",1)
            #print("data",data)
        data = data.replace(" ","")
        if not data:
            answer = answer + 1
    return answer


print(solution(["ayaaya"]))
print(solution(["aya", "yee", "u", "maa", "wyeoo"]))
print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]))
