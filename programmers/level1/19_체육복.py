
def solution(n, lost, reserve):
    answer = n
    for i in range(1,n+1):
        if i in lost and  i in reserve:
            lost.remove(i)
            reserve.remove(i)
            continue

    for i in range(1,n+1):
        if i in lost:
            pr = i-1
            ne = i+1
            if i-1 in reserve:
                reserve.remove(i-1)
            elif i+1 in reserve:
                reserve.remove(i+1)
            else:
                answer = answer - 1
    return answer

print("solution",solution(5,[2,4,5],[1,3,5]))
print("solution",solution(5,[2,4],[1,3,5]))
print("solution",solution(5,[2, 4], [3]))
print("solution",solution(3,[3],[1]))

