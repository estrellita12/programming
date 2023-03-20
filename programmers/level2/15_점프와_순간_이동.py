
def solution(n):
    ans = 0
    while True:
        if n%2==0:
            n = n//2
        else:
            ans = ans+1
            n = n-1
        if n <= 0:
            break
    return ans

print("solution",solution(5000))

