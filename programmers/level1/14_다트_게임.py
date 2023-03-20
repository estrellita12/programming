import re

def solution(dartResult):
    answer = 0
    '''
    ch  = re.sub("[1-9]", lambda m: " "+str(m.group()),dartResult)
    chList = list(filter(None,ch.split(" ")))
    print(chList);
    '''

    scoreList = []
    bonusList = {"S":1,"D":2,"T":3}
    num = re.compile('^[0-9]*')
    for s in dartResult:
        ch = num.match( dartResult )
        score = int(ch.group())
        end = ch.end()
        score =  score ** int(bonusList[dartResult[end]])
        end = end + 1
        if len(dartResult) > end:
            opt = dartResult[end]
            if opt == "*":
                score = score * 2
                if len(scoreList) > 0:
                    scoreList[-1] = scoreList[-1] * 2
                end = end + 1
            elif opt == "#":
                score = score * -1
                end = end + 1
        scoreList.append(score)
        dartResult = dartResult[end:]
        #print(scoreList, dartResult)
        if len(dartResult) <= 0:
            break
    answer = sum(scoreList)
    return answer

#print("solution",solution("10D#2D*3T"))
print("solution",solution("1S2D*3T"))
print("solution",solution("1D2S#10S"))
print("solution",solution("1D2S0T"))
print("solution",solution("1S*2T*3S"))
print("solution",solution("1D#2S*3S"))
print("solution",solution("1T2D3D#"))
print("solution",solution("1D2S3T*"))

