def solution(n):
    answer = 0
    
    tmp=''
    while n != 0:
        tmp += str(n%3)
        n = n//3
        
    for i in range(0,len(tmp)):
        #print(i,3**i,tmp[len(tmp)-i-1])
        answer+= ( 3**i*(int(tmp[len(tmp)-i-1])) )
    
    return answer
