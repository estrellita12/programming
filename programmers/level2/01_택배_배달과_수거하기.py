def solution(cap, n, deliveries, pickups):
    answer = 0
    deIdxLi = []; pkIdxLi = []
    for i in range(n-1,-1,-1):
        if deliveries[i] != 0:
            deIdxLi.append(i)
        if pickups[i] != 0:
            pkIdxLi.append(i)

    goList = []; goBox = 0
    if len(deIdxLi) > 0:
        goList.append(deIdxLi[0]+1)
        goBox = cap
        for i in deIdxLi:
            goBox = goBox - deliveries[i]
            while goBox < 0:
                goList.append(i+1)
                goBox = goBox + cap

    backList = []; backBox = 0
    if len(pkIdxLi) > 0:
        backList.append(pkIdxLi[0]+1)
        for i in pkIdxLi:
            backBox = backBox + pickups[i]
            while backBox > cap:
                backList.append(i+1)
                backBox = backBox - cap

    cnt = len(goList)
    if len(goList) < len(backList):
        cnt = len(backList)

    for i in range(cnt):    
        score = 0
        if i < len(goList):
            if score < goList[i]:
                score = goList[i]
        if i < len(backList):
            if score < backList[i]:
                score = backList[i]
        answer = answer + (score*2)
    return answer

print("solution",solution(4,5,[1, 0, 3, 1, 2],[0, 3, 0, 4, 0]))
print("solution",solution(4,5,[0, 0, 0, 0, 0],[0, 0, 0, 0, 1]))
print("solution",solution(2,7,[1, 0, 2, 0, 1, 0, 2] ,[0, 2, 0, 1, 0, 2, 0]))
print("solution",solution(4,11,[1, 0, 3, 0,0,0,1, 2,0,0,0],[0, 3, 0,0,0,0, 4, 0,1,1,1]))
