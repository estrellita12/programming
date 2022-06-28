def solution(id_list, report, k):
    answer = []
        report = list(set(report))

            arr = dict()
    for i in id_list:
        arr[i]=[0,list()]

    for str in report:
        user = str.split(" ");
        arr[user[1]][0] = arr[user[1]][0]+1
        arr[user[1]][1].append(user[0])

    answer = dict()
    for i in id_list:
        answer[i] = 0

    for j in arr.values():
        if j[0] >= k :
            for r in j[1]:
                answer[r] = answer[r] + 1

    return list(answer.values())
