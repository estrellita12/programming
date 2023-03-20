
def solution(s):
    answer = ''
    li = list(map(int,s.split(" ")))
    
    minimum = li[0]
    maximum = li[0]
    for x in li:
        if x > maximum:
            maximum = x
        if x < minimum:
            minimum = x
    answer = str(minimum)+" "+str(maximum)
    return answer

print("solution",solution("1 2 3 4"))
print("solution",solution("-1 -2 -3 -4"))
print("solution",solution("1 -2 -3 -4"))

