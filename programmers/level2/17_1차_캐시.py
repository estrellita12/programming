
def solution(cacheSize, cities):
    answer = 0

    qu = list()
    for c in cities:
        c = c.upper()
        if c in qu:
            answer = answer + 1
            idx = qu.index(c)
            qu.pop(idx)
            qu.append(c)
        else:
            answer = answer + 5
            qu.append(c)
            if len(qu) > cacheSize:
                qu.pop(0)
        print(qu)

    return answer

#print("solution",solution(3,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print("solution",solution(3,["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
#print("solution",solution(2,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
#print("solution",solution(5,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
#print("solution",solution(2,["Jeju", "Pangyo", "NewYork", "newyork"]))
#print("solution",solution(0,["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
#print("solution",solution(1,["Jeju","jeju"]))

