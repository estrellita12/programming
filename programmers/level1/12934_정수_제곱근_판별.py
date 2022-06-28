def solution(n):
    answer = 0
    n1 = (n**0.5)
    n2 = int(n1)
    if n1>n2 or n1<n2 :
        answer = -1
    else:
        answer = ( (n2+1)**2 )
    return answer
