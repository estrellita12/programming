# https://programmers.co.kr/learn/courses/30/lessons/42840
def solution(answers):
    answer = []
    s1list = [1,2,3,4,5]
    s2list = [2,1,2,3,2,4,2,5]
    s3list = [3,3,1,1,2,2,4,4,5,5]
    score = [0,0,0]
    for i in range(len(answers)):
        if s1list[i%5] == answers[i]:
            score[0]+=1
        if s2list[i%8] == answers[i]:
            score[1]+=1
        if s3list[i%10] == answers[i]:
            score[2]+=1
    maxData = max(score)
    for i in range(3):
        if score[i]==maxData:
            answer.append(i+1)
    
    return answer
