
def solution(sizes):
    answer = 0

    width = []
    height = []
    for w,h in sizes:
        if w >= h:
            width.append(w)
            height.append(h)
        else:
            width.append(h)
            height.append(w)
             
    answer = max(width)*max(height)
    return answer


print("solution",solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print("solution",solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
print("solution",solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))
