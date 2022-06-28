def solution(n):
    answer = []
    
    while n!= 0:
        answer.append( n%10 )
        n = n//10
        
    '''
    tmp = list(str(n))
    tmp.sort()
    tmp.reverse()
    for i in tmp:
        answer.append( int(i) )
    '''

    
    return answer
