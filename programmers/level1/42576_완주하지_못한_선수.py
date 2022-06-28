# https://programmers.co.kr/learn/courses/30/lessons/42576?language=python3
# 효율성 테스트 실패!!!!
def solution(participant, completion):
    answer = ''
    '''
    for name in completion:
        participant.remove(name)
    answer = participant[0]
    '''
    for name in participant:
        if participant.count(name) != completion.count(name):
            answer = name
            break
    return answer
