def find_set(x):
    if x != parent[x]:
        parent[x] = find_set(parent[x])
    return parent[x]

def union(x,y):
    parent[find_set(y)] = find_set(x)

n, m = map(int,input().split())
parent = [i for i in range(n+1)]

for _ in range(m):
    check, a, b = map(int,input().split())
    if check:
        if find_set(a)==find_set(b):
            print('YES')
        else:
            print('NO')
    else:
        union(a,b)

