# https://programmers.co.kr/learn/courses/30/lessons/42748
def solution(array, commands):
    answer = []
    
    for ex in commands:
        # ex : 각각의 경우 리스트
        i = ex[0]-1
        j = ex[1]
        k = ex[2]-1
        tmp = array[i:j]
        tmp.sort()
        answer.append(tmp[k])
    
    return answer
