
def solution(d, budget):
    answer = 0
    if sum(d) <= budget:
        return len(d)
    
    d.sort()
    for i in d:
        if budget >= i:
            answer = answer + 1
            budget = budget-i
        else:
            break
    return answer

#print("solution",solution([1,3,2],9))
print("solution",solution([1,3,2,5,4],9))
print("solution",solution([2,2,3,3],10))

