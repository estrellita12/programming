
def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    sIdx = 0
    eIdx = len(people)-1
    while sIdx <= eIdx:
        print(people,sIdx,eIdx)
        answer = answer + 1
        if sIdx < eIdx:
            if limit - people[sIdx] >=  people[eIdx]:
                eIdx = eIdx - 1
        sIdx = sIdx + 1
    answer = sIdx
    return answer

print("solution",solution([50],100))
print("solution",solution([70, 50, 80, 50],100))
#print("solution",solution([40, 60, 50, 50],100))
#print("solution",solution([70, 80, 50],100))
#print("solution",solution([40, 50, 60, 70, 80, 90, 100]*5,130))
#print("solution",solution([40, 40, 40, 120, 120, 90, 100]*5,130))


