def fibo(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibo(n-1)+fibo(n-2)
   
def solution(n):
    answer = 0   
    #res = fibo(n)

    pr = 0
    ne = 1
    for i in range(2,n+1):
        tmp = pr
        pr = ne
        ne = tmp+pr
    res = ne
    answer = res%1234567
    return answer

print("solution",solution(2))
print("solution",solution(3))
print("solution",solution(4))
print("solution",solution(5))

