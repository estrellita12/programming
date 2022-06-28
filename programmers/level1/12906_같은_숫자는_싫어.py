# https://programmers.co.kr/learn/courses/30/lessons/12906
def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(1,len(arr)):
        if arr[i]!=answer[-1]:
            answer.append(arr[i])
    return answer
