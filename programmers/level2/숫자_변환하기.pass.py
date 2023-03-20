from itertools import permutations

def comp(target,n,selected,selectedList):
    #print( list(permutations(arr,n)) )
    #cnt = int(fac(len(arr))/fac(len(arr)-n))
    #print("cnt",cnt)
    if len(selected) >= n:
        selectedList.append(selected)
        return
    for i in target:
        tmp = list(selected)
        tmp.append(i)
        comp(target,n,list(tmp),selectedList)

def oper(t,x,n):
    if t == 1:
        return x+n
    elif t == 2:
        return x*2
    elif t == 3:
        return x*3
    
def solution2(x, y, n):
    answer = 0
    k = 0
    while True:
        k = k + 1
        selected = list()
        comp([3,2,1],k,list(),selected)
        flag = False
        for arr in selected:
            tot = x;
            for op in arr:
                tot = oper(op,tot,n)
            print("횟수 : ",k, ", arr",arr,"tot",tot)
            if tot == y:
                #print("횟수 : ",k, ", arr",arr)
                return k
            if tot < y :
                flag = True
        if not flag:
            return -1
            break
    return answer

def test(ori,dst,n):
    nex = ori
    flag = True
    if ori > n :
        flag = False
        nex = ori - n
        if nex == dst:
            return nex
    if ori % 3 == 0 :
        flag = False
        if nex > ori/3:
            nex = int(ori/3)
            if nex == dst:
                return nex
    if ori % 2 == 0 :
        flag = False
        if nex > ori/2:
            nex = int(ori/2)
            if nex == dst:
                return nex

    if flag:
        return 0
    return nex


def solution(x, y, n):
    answer = 0
    #while True:
    ne = y
    cnt = 0;

    #while True:
    for k in range(1000):
        cnt = cnt + 1;
        #ne = test(ne,x,n)
        pr = ne
        if pr > n:
            ne = ne - n
        if pr % 3 == 0:
            if pr/3 < ne:
                cnt = cnt + pr//3
                ne = 0
        

        print("cnt",cnt,"res",ne)
        if ne == x:
            return cnt
        elif ne < x:
            return -1
    return answer



#print("solution",solution(10,40,5))
#print("solution",solution(10,40,30))
#print("solution",solution(2,5,4))
#print("solution2",solution(10,10000,30))
print("solution",solution(1,28,1))

