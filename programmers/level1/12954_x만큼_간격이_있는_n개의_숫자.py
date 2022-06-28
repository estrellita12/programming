def solution(x, n):
    answer = []
    for i in range(0,n):
        if i==0:
            answer.append(x)
        else :
            answer.append(answer[i-1]+x)
    return answer

print(solution(2,5)) #[2,4,6,8,10]
print(solution(-4,2)) #[-4,-8]


