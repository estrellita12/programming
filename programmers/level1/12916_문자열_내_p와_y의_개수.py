# https://programmers.co.kr/learn/courses/30/lessons/12916
def solution(s):
    answer = True
    
    pnum = s.count("p") + s.count("P")
    ynum = s.count("y") + s.count("Y")

    if pnum != ynum :
        answer = False

    return answer
