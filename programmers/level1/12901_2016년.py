def solution(a, b):
    answer = ''
    dayList = ["THU","FRI","SAT","SUN","MON","TUE","WED"]
    lastList = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    total = 0
    for i in range(a):
        total += lastList[i]
    total += b
    answer = dayList[total%7]
    return answer
