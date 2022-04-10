from collections import deque

N,M = map(int, input().split()) #N*N 매트릭스, M번의 구름이동
matrix = [list(map(int,input().split())) for _ in range(N)]

cloud = deque([(N-2,0),(N-2,1),(N-1,0),(N-1,1)])
dr,dc = [0,-1,-1,-1,0,1,1,1],[-1,-1,0,1,1,1,0,-1]
ddr,ddc = [-1,-1,1,1],[-1,1,1,-1]
for _ in range(M):
    new_cloud = deque()
    d, move = map(int, input().split())
    d = d - 1


    for i in range(len(cloud)):
        r,c = cloud[i]
        rr,cc = (r+dr[d]*move)%N, (c+dc[d]*move)%N
        matrix[rr][cc] = matrix[rr][cc]+1
    #구름 +1씩해줘

    for _ in range(len(cloud)):
        r, c = cloud.popleft()
        rr, cc = (r + dr[d] * move) % N, (c + dc[d] * move) % N
        cloud.append((rr,cc))
        for i in range(4):
            rr, cc = (r + dr[d] * move) % N, (c + dc[d] * move) % N
            rrr,ccc = rr+ddr[i], cc+ddc[i]
            if 0<=rrr<N and 0<=ccc<N and matrix[rrr][ccc]:
                matrix[rr][cc]= matrix[rr][cc]+1


    for i in range(N):
        for j in range(N):
            if matrix[i][j] >=2 and (i,j) not in cloud:
                matrix[i][j] -=2
                new_cloud.append((i,j))
    cloud = new_cloud
rlt = 0
for i in range(N):
    for j in range(N):
        rlt += matrix[i][j]
print(rlt)




