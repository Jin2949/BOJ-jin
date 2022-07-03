def solution(N, stages):
    dict = {}
    rlt = []
    stages.sort()

    a = 0
    cnt = 0


    for i in range(1, N+2):
        dict[i] = 0

    for k in stages:
        dict[k] += 1

    count = 0
    for j in range(1, N+1):
        if len(stages) - count:
            rlt.append(dict[j]/(len(stages)-count))
            count += dict[j]


    while True:
        if len(rlt) != N:
            rlt.append(0)
        else:
            break



    answer = []
    check = 0

    while True:
        answer.append(rlt.index(max(rlt)) + 1)

        rlt[rlt.index(max(rlt))] = -1
        check += 1
        if check == len(rlt):
            break
    return answer