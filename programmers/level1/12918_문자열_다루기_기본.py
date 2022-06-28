def solution(s):
    answer = True
    
    if not (len(s) == 4 or len(s) == 6):
        answer = False
    
    for t in s:
        if t not in ['0','1','2','3','4','5','6','7','8','9']:
            answer = False
    
    return answer
