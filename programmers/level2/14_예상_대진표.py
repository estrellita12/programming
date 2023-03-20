
def solution(n,a,b):
    answer = 0
    i = 0
    while True:
        i = i + 1
        a = (a+1)//2
        b = (b+1)//2
        #print(i,"회차 당시","A",a,"번 경기장","B",b,"번 경기장")
        if a == b:
            answer = i
            break
    return answer


print("solution",solution(8,4,7))

