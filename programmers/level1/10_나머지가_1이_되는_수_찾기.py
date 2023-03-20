def solution(n):
    answer = 0
    
    for i in range(2,n):
        if n%i==1:
            answer = i
            return answer

print("solution", solution(10))
print("solution", solution(12))

