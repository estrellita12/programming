def solution(survey, choices):
    answer = ''
    chk = {'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    for i in range(len(survey)):
        if choices[i] < 4:
            score = 4 - choices[i]
            chk[survey[i][0]] = chk[survey[i][0]] + score
        else:
            score = choices[i] - 4
            chk[survey[i][1]] = chk[survey[i][1]] + score
        #print(survey[i],choices[i],score)
        #print(chk)

    st = [["R","T"],["C","F"],["J","M"],["A","N"]]
    for x,y in st:
        if chk[x] >= chk[y]:
            answer = answer + x
        else :     
            answer = answer + y

    return answer

print("solution",solution(["AN", "CF", "MJ", "RT", "NA"],   [5, 3, 2, 7, 5]))
print("solution",solution(["TR", "RT", "TR"],[7, 1, 3]))




