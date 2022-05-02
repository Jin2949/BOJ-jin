import sys

n, m = map(int, input().split())
mini = []
matrix = [list(map(str,input())) for _ in range(n)]

for i in range(n - 7):
    for j in range(m - 7):
        white = 0
        black = 0
        for r in range(i, i + 8):
            for c in range(j, j + 8):
                if (r + c)%2 == 0:
                    if matrix[r][c] != 'W':
                        white += 1
                    if matrix[r][c] != 'B':
                        black += 1
                else :
                    if matrix[r][c] != 'B':
                        white += 1
                    if matrix[r][c] != 'W':
                        black += 1
        mini.append(white)
        mini.append(black)

print(min(mini))