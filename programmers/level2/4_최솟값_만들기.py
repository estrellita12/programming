def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    tot = 0
    for i in range(len(A)):
        tot = tot + ( A[i]*B[i] )
    answer = tot
    return answer
print("solution",solution([1, 4, 2],[5, 4, 4]))
print("solution",solution([1,2],[3,4]))


