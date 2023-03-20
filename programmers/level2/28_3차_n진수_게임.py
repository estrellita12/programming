import math

def chnum(n,k):
    res = ""
    while True:
        tmp = n%k
        if tmp >= 10:
            tmp = chr(tmp+55)
        res = str(tmp)+res
        n = n//k
        if n<=0:
            break
    return res

def solution(n, t, m, p):
    answer = ''
    idx = 0
    s = ""
    for i in range(t):
        nth = p+(i*m)
        while True:
            if nth <= len(s):
                #print(nth,s,s[nth-1])
                answer += s[nth-1]
                break
            s = s+chnum(idx,n)
            idx = idx + 1
    return answer

print("solution",solution(2,4,2,1))
print("solution",solution(16,16,2,1))
print("solution",solution(16,16,2,2))

