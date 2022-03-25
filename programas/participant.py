def solution(participant, completion):
    temp = 0
    dic = {}

    for p in participant:
        dic[hash(p)] = p

        temp += int(hash(p))

    for com in completion:
        temp -= hash(com)

    return dic[temp]

