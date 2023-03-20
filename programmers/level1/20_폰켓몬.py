
def solution(nums):
    answer = 0

    have = len(nums)//2
    arr = set(nums)
    if have > len(arr):
        answer = len(arr)
    else:
        answer = have
    return answer


print("solution",solution([3,1,2,3]))
print("solution",solution([3,3,3,2,2,4]))
print("solution",solution([3,3,3,2,2,2]))

