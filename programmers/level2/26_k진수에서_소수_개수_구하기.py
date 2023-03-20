def chnum(n,k):
    res = ""
    while n>=1:
        res = str(n%k)+res
        n = n//k
    return res

def solution(n, k):
    answer = 0
    res = chnum(n,k)
    li = res.split("0")
    for x in li:
        if not x or x == "1":
            continue
        x = int(x)
        cnt = 0
        for p in range(1,int(x**(1/2))+1):
            if x%p==0:
                cnt = cnt+1
            if cnt > 1:
                break
        if cnt == 1:
            answer = answer + 1
    return answer

print("solution",solution(437674,3))
print("solution",solution(110011,10))
#print("solution",solution(1000000,4))
#print("solution",solution(5,8))

