
def solution(N, stages):
    #answer = [i for i in range(1,N+1)]
    answer = []
    fail = dict()
    for n in range(1,N+1):
        # n번 스테이지의 실패율
        clear = sum(1 for i in stages if i > n )
        stop = stages.count(n)
        if clear+stop != 0:
            fail[n] = float(stop/(clear+stop))
        else:
            fail[n] = float(0)
    failList = sorted(fail.items(),key=lambda x:(x[1],-x[0]), reverse=True)
    answer = [x[0] for x in failList]
    return answer

print("solution",solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))
print("solution",solution(4,[4,4,4,4,4]))
