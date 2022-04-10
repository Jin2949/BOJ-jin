from itertools import combinations

N, M = map(int, input().split())
matrix = [list(map(int,input().split())) for _ in range(N)]

home = []
chicken = []
for i in range(N):
    for j in range(N):
        if matrix[i][j]==1:
            home.append((i,j))
        elif matrix[i][j]==2:
            chicken.append((i,j))

rlt = 99999
for chi in combinations(chicken,M):
    total = 0
    for h in home:
        cnt = 999
        for c in range(M):
            cnt = min(cnt,abs(chi[c][0]-h[0]) + abs(chi[c][1]-h[1]))
        total += cnt
    rlt = min(rlt,total)
print(rlt)



