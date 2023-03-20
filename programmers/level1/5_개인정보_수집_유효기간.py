
def isNext( st, target ):
    stDay = st[2] + (st[1]*28) + (st[0]*12*28)
    targetDay = target[2] + (target[1]*28) + (target[0]*12*28)
    if stDay < targetDay:
        return True
    else:
        return False

def solution(today, terms, privacies):
    answer = []

    today = list(map(int,today.split(".")))
    #print("today",today)

    td = dict();
    for arr in terms:
        x = arr.split(" ")
        td[x[0]] = int(x[1])
    #print("terms",terms)
    #print("td",td)

    for i in range(len(privacies)):
        x = privacies[i].split(" ")
        date = list(map(int, x[0].split(".")))
        policy = x[1]
        date[2] = date[2] + (td[policy]*28)
        if not isNext(today,date):
            answer.append(i+1)
                    
    return answer


print("solution",solution("2022.05.19",["A 6", "B 12", "C 3"],["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
print("solution",solution("2020.01.01",["Z 3", "D 5"],["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))
#print("solution",solution("2022.12.19",["A 6", "B 12", "C 20"],["2021.05.02 A", "2021.07.01 B", "2022.12.19 C", "2022.02.20 C"]))
#print("solution",solution("2020.01.01",["Z 3", "D 20"],["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))
