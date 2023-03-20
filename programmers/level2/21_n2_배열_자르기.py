def solution(n, left, right):
    '''
    answer = []
    for i in range(1,n+1):
        li = list()
        for j in range(1,n+1):
            x = j
            if x < i:
                x = i
            li.append(x)
        #print(li)
        answer.extend(li)
    answer = answer[left:right+1]
    return answer
    '''

    answer = []
    for x in range(left,right+1):
        i = x//n + 1
        j = x%n + 1
        #print("i",i,"j",j,"x",x)
        answer.append( j if i<j else i)
    return answer
 
    

print("solution",solution(3,2,5))
print("solution",solution(4,7,14))

