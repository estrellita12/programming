from itertools import combinations, permutations

def isPrime(n):
    flag = True
    for i in range(2,(n//2)+1):
        if n%i==0:
            flag = False
    return flag


def solution(nums):
    answer = 0
    combi = list(combinations(nums, 3))
    for x in combi:
        res = isPrime(sum(x))
        if res:
            answer = answer + 1
    return answer


print("solution",solution([1,2,3,4]))

