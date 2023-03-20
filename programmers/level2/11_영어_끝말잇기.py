
def solution(n, words):
    answer = [0,0]
    
    res1 = ""; res2 = words[0]
    for i in range(1,len(words)):
        per = (i%n)+1
        nth = (i//n)+1
        print(per,"번째 사람의",nth,"번쨰 차례",words[i])
        res1 = res2
        res2 = words[i]
        if words.index(res2) < i:
            return [per,nth]
        if res1[-1] != res2[0]:
            return [per,nth]
        
    return answer


print("solution",solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print("solution",solution(5,["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print("solution",solution(2,["hello", "one", "even", "never", "now", "world", "draw"]))
