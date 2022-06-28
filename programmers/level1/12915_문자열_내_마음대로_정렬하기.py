def solution(strings, n):
    answer = []
        
            for i in range(len(strings)):
                    for j in range(i+1,len(strings)):
            if strings[i][n] > strings[j][n]:
                tmp = strings[i]
                strings[i] = strings[j]
                strings[j] = tmp
            elif strings[i][n] == strings[j][n]:
                if strings[i] > strings[j]:
                    tmp = strings[i]
                    strings[i] = strings[j]
                    strings[j] = tmp
    answer = strings
    
    
    return answer
