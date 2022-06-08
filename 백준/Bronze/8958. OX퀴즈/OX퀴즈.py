import sys

n = int(input())

for _ in range(n):
    lst = input()
    score = 0
    total = 0
    for i in lst:
        if i == 'O':
            score += 1
            total += score
        elif i == 'X':
            score = 0
    print(total)
