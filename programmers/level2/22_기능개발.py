import math
def solution(progresses, speeds):
    answer = []

    dd = 0
    for i in range(len(progresses)):
        res = 100 - progresses[i]
        day = math.ceil(res/speeds[i])
        if dd < day:
            dd = day
            answer.append(1)
        else:
            res = answer.pop()
            answer.append(res+1)


    return answer

print("solution",solution([93],[1]))
print("solution",solution([93,99],[1,1]))
print("solution",solution([93, 30, 55],[1, 30, 5]))
print("solution",solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))

