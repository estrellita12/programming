def cut(x,y):
    return (x-1)+(x*(y-1))

def solution(M, N):
    if M > N:
        answer = cut(N,M)
    else:
        answer = cut(M,N)
    return answer


print(solution(2,2))
print(solution(2,5))
print(solution(1,1))

