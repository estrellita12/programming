def solution(s):
    answer = ''
    tmp = list(s)
    tmp.sort()
    tmp.reverse()
    for i in tmp:
        answer += i
    return answer
