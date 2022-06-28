def solution(n):
    answer = 0
    
    for t in range(2,n+1):
        flag = False
        tmp = int( t**0.5 )
        for i in range(2,tmp+1):
            if t%i == 0:
                flag = True
                break
        if flag == False:
            answer+=1
        
    
    return answer
