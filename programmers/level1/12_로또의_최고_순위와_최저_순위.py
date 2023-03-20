def solution(lottos, win_nums):
    answer = []
    minScore = 7
    for num in lottos:
        if num in win_nums :
            minScore = minScore - 1
    maxScore = minScore - lottos.count(0)
    if minScore >= 7:
        minScore = 6
    if maxScore >= 7:
        maxScore = 6
    answer = [maxScore,minScore]
    return answer


#print("solution",solution([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19]))
#print("solution",solution([0, 0, 0, 0, 0, 0],[38, 19, 20, 40, 15, 25]))
#print("solution",solution([45, 4, 35, 20, 3, 9],[20, 9, 3, 45, 4, 35]))
print("solution",solution([21, 10, 11, 46, 5, 36],[20, 9, 3, 45, 4, 35]))


