def getNum(n):
    cnt = 1
    for i in range(1,n//2+1):
        if n%i == 0:
            cnt = cnt+1
    if cnt%2 == 1:
        return n*-1
    else:
        return n


def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        answer = answer + getNum(i)
    return answer



print("solution",solution(13,17))
print("solution",solution(24,27))


