#from itertools import permutations # 순열
from itertools import combinations # 조합

def solution(clothes):
    answer = 0
    dc = dict()
    for c,t in clothes:
        if t in dc.keys():
            dc[t] = dc[t]+1
        else:
            dc[t] = 1
    answer = 1
    for x in dc:
        answer = answer * (dc[x]+1) 
    answer = answer - 1
    '''
    arr = list(dc.values())
    answer = sum(arr)
    for i in range(2,len(arr)+1):
        for j in list(combinations(arr,i)):
            print(j)
            cnt = 1
            for k in j:
                cnt = cnt * k
            answer = answer + cnt
    '''
 
    return answer


print("solution",solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print("solution",solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))
print("solution",solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"],["blue_sunglasses", "face"]]))
