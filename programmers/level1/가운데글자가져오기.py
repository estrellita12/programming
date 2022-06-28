# https://programmers.co.kr/learn/courses/30/lessons/12903
def solution(s):
    answer = ''
    size = len(s);
    if len(s)%2==0:
        answer += s[(size//2)-1]
        answer += s[(size//2)]
    else:
        answer += s[(size//2)]
    return answer
