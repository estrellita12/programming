
def solution(priorities, location):
    answer = 0

    flag = location
    while len(priorities) > 0:
        mm = max(priorities)
        tmp = priorities.pop(0)
        if mm > tmp:
            priorities.append(tmp)
        else:
            answer = answer + 1
            if flag == 0:
                break
        flag = flag - 1
        if flag < 0:
            flag = flag + len(priorities)
        #print(priorities,flag)
    return answer

#print("solution",solution([2,1],0))
print("solution",solution([2, 1, 3, 2],2))
print("solution",solution([1, 1, 9, 1, 1, 1],0))

