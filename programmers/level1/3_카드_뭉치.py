def solution(cards1, cards2, goal):
    answer = "Yes"
    for s in goal:
        if len(cards1)>0 and cards1[0] == s:
            cards1.pop(0)
        elif len(cards2)>0 and cards2[0] == s:
            cards2.pop(0)
        else:
            answer = "No"
            return answer

    return answer

print("solution",solution(["i", "drink", "water"],["want", "to"],["i", "want", "to", "drink", "water"]))
print("solution",solution(["i", "water", "drink"],["want", "to"],["i", "want", "to", "drink", "water"]))

