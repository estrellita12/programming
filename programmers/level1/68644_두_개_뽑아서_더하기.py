# https://programmers.co.kr/learn/courses/30/lessons/68644?language=python3
def solution(numbers):
    answer = []
    
    for i in range(len(numbers)):
        # i 번째 수와 j번째 수
        for j in range(i+1,len(numbers)):
            res = numbers[i]+numbers[j]
            # set를 사용 할 수도 있다
            if res not in answer:
                answer.append(res)
    answer.sort()
    
    return answer
