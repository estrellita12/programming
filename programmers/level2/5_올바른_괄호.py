def solution(s):
    answer = False
    
    res = 0
    for x in s:
        if x == "(":
            res = res + 1
        elif x == ")":
            res = res - 1
         
        if res < 0:
            answer = False
            return answer
    if res == 0:
        answer = True
        return answer
    return answer

print("solution",solution("()()"))
print("solution",solution("(())()"))
print("solution",solution(")()("))
print("solution",solution("(()("))
