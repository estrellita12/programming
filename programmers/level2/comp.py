def test(target,selected,selectedList,n):
    if len(selected) >= n:
        selectedList.append(selected)
        return

    for i in arr:
        tmp = list(selected)
        tmp.append(i)
        test(target,list(tmp),selectedList,n)

arr = [1,2,3]
selected = []
print(test(arr,list(),selected,3))
#print(selected)
