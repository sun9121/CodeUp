v, e = map(int, input().split())

parent = [0] * (v+1)

lines = []
result = 0

for _ in range(e):
    a, b, cost = map(int, input().split())

    lines.append((cost,a,b))

lines.sort()
biggest = 0

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b]=a
    else:
        parent[a]=b


for line in lines:
    cost, a, b = line

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        biggest += cost

print(result - biggest)