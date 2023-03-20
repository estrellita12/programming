def solution(n):
    answer = 0
    for x in range(1,n+1):
        tot = 0
        for y in range(x,n+1):
            tot = tot + y
            if tot == n:
                print(x,y,tot)
                answer += 1
                break
            if tot > n:
                break
                
    return answer

print("solution",solution(15))

