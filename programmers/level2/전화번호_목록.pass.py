import re
def solution3(phone_book):
    answer = True
    s = " ".join(phone_book)
    s = " "+s
    for x in phone_book:
        res = re.findall("( "+x+")[0-9]*",s)
        if len(res) >= 2:
            return False
    return answer

def solution2(phone_book):
    answer = True
    for i in range(len(phone_book)):
        for j in range(i+1,len(phone_book)):
            res = phone_book[j].find(phone_book[i])
            if res == 0:
                return False
    return answer

def solution(phone_book):
    answer = True
    dc = dict()
    for x in phone_book:
        if x[0] not in dc.keys():
            dc[x[0]] = list()
        dc[x[0]].append(x)

    print(dc)
    return answer
 

print("solution",solution(["119", "97674223", "1195524421"]))
print("solution",solution(["123","456","789"]))
print("solution",solution(["12","123","1235","567","88"]))

