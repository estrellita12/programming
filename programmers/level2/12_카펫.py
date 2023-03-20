

def solution(brown, yellow):
    answer = []

    area = brown+yellow
    for i in range(1,area//2):
        if area%i==0:
            x = int(area//i)
            y = int(area/x)
            if (2*x + 2*y - 4) == brown:
                if x > y:
                    return [x,y]
                else:
                    return [y,x]
    

    return answer

print("solution",solution(10,2))
print("solution",solution(8,1))
print("solution",solution(24,24))
