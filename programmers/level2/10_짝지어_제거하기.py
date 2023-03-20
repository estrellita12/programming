def solution(s):
    answer = -1
    stack = list()

    for x in s:
        if not stack:
            stack.append(x)
        else:
            if stack[-1] == x:
                stack.pop()
            else:
                stack.append(x) 

    if len(stack) == 0:
        return 1
    else:
        return 0

            
        
        

    '''
    i = 1
    while True:
        cnt = len(s)
        if cnt <= i:
            break
        if s[i-1] == s[i]:
            tmp = s[i]+s[i]
            s = s.replace(tmp,"")
            i = i - 2
            if i < 0:
                i = 1
        else:
            i = i + 1
    if len(s) == 0:
        answer = 1
    else:
        answer = 0
    '''
    return answer
    
   
       
#print("solutuin",solution("a"))
#print("solutuin",solution("aa"))
#print("solutuin",solution("baa"))
#print("solutuin",solution("abbcca"))
#print("solutuin",solution("baaabbaaab"))
#print("solutuin",solution("baabaaccbbaacbbaaccbbaac"))
#print("solutuin",solution("abcdefggfedcbazbxchertqwvxzsdsd"*2))
print("solutuin",solution("baabaa"))
print("solutuin",solution("cdcd"))
data = "abcdefghijklmnopqrstuvwxyziiiizyxwvutsrqponmlkjihgfedcba"
#print("solutuin",solution(data*2))

