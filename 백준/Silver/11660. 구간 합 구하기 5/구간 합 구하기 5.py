import sys

n, m = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(n):
    for j in range(1,n):
        matrix[i][j] = matrix[i][j-1] + matrix[i][j]

for _ in range(m):
    total = 0
    x1,y1,x2,y2 = map(int, sys.stdin.readline().split())
    for i in range(x1-1,x2):
        total += matrix[i][y2-1]
        if y1 > 1:
            total -= matrix[i][y1-2]
    print(total)