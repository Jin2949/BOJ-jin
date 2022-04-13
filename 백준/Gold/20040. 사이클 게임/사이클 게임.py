def find(x):
    if x!= parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)
    parent[max(x, y)] = min(x, y)


n,m = map(int,input().split())
parent = [x for x in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    if find(a) == find(b):
        print(i+1)
        break
    union(a,b)
else:
    print(0)

