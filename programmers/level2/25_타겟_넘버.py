'''
def comp(arr,tot,li):
    if len(arr)<=0: 
        li.append(tot)
        return
    tmp = arr.pop()
    comp(list(arr),tot-tmp,li)
    comp(list(arr),tot+tmp,li)
               
def solution(numbers, target):
    answer = 0
    #res = int(( sum(numbers) - target ) / 2 )
    li = list()
    comp(numbers,0,li)

    answer = li.count(target)   
     
    return answer
'''

def comp(arr,target,depth=0):
    answer = 0
    if depth == len(arr):
        print("depth",depth,"else",arr)
        if sum(arr) == target:
            return 1
        else: 
            return 0
    else:
        answer += comp(list(arr),target,depth+1)
        arr[depth] = arr[depth]*-1
        answer += comp(list(arr),target,depth+1)
        return answer
               
def solution(numbers, target):
    answer = 0
    #res = int(( sum(numbers) - target ) / 2 )
    li = list()
    answer = comp(numbers,target)
    return answer


'''
def solution(numbers, target):
    answer = 0
    leaves = [0]
    for num in numbers:
        tmp = []
        for parent in leaves:
            tmp.append(parent + num)
            tmp.append(parent - num)
        print(tmp)
        leaves = tmp
    for leaf in leaves:
        if leaf == target:
            answer += 1
    return answer
'''
#print("solution",solution([1, 1, 1, 1, 1],3))
print("solution",solution([4, 1, 2, 1],4))

