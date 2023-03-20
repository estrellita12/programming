def solution(num, total):
    answer = []
    n = int((total-((num*(num-1))/2))//num)
    for i in range(num):
        answer.append(n+i)
    return answer


print( solution(3,12) )
print( solution(5,15) )
print( solution(5,5) )

