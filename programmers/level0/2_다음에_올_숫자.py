
def solution(common):
    # 최소 3개
    answer = 0
    op = common[1] - common[0]
    if common[2] == (common[1] + op):
        answer = common[-1]+op
    else :
        op = common[1]//common[0]
        if common[2] == (common[1] * op):
            answer = common[-1]*op
    return answer


print(solution([1, 2, 3, 4]))
print(solution([2,4,8]))
