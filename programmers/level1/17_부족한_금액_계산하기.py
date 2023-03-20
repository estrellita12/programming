
def solution(price, money, count):
    answer = -1
    res = int(count*((price*2)+((count-1)*price))/2)
    answer = res - money
    if answer <= 0:
        answer = 0
    return answer


print("solution",solution(3,20,4))

