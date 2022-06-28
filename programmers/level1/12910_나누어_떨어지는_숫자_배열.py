def solution(arr, divisor):
    answer = []
    
    for tmp in arr:
        if tmp%divisor == 0:
            answer.append(tmp)
    answer.sort()
    
    if len(answer)==0:
        answer.append(-1)
        
    return answer
