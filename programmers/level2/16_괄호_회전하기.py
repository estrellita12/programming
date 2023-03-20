
def chk(s):
    dc = dict()
    dc['{'] = "}" 
    dc['['] = "]" 
    dc['('] = ")"
 
    li = list()
    for x in s:
        if not li:
            li.append(x)
        else:
            if li[-1] in dc and dc[li[-1]] == x:
                    li.pop()
            else:
                li.append(x)
    if len(li) == 0:
        return True
    else:   
        return False

def solution(s):
    answer = 0
    for i in range(len(s)):
        s = s[1:]+s[0]   
        if chk(s):
            answer = answer + 1
   
    return answer

#print("solution",solution("{{({})}}"))
print("solution",solution("[](){}"))
print("solution",solution("}]()[{"))
print("solution",solution("[)(]"))
print("solution",solution("}}}"))

