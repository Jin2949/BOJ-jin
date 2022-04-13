def find(x):
    if x!= parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    x= find(x)
    y= find(y)
    parent[max(x,y)]= min(x,y)

N = int(input())
M = int(input())

parent = [x for x in range(N+1)]

for i in range(1,N+1):
    lst = list(map(int,input().split()))
    for j in range(1,len(lst)+1):
        if lst[j-1]:
            union(i,j)

trip_lst = list(map(int,input().split()))
result = set([find(i) for i in trip_lst])

if len(result) != 1:
    print('NO')
else:
    print('YES')


