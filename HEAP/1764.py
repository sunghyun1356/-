n, m = map(int, input().split())
d = set()
b = set()
for i in range(n):
    d.add(input())
for j in range(m):
    b.add(input())
c = d.intersection(b)
c = sorted(c)
print(len(c))
for i in c:
    print(i)