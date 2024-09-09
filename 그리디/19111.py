n, l = map(int, input().split())
pound = []
for _ in range(n):
    start, end = map(int, input().split())
    pound.append(start)
    pound.append(end)
pound.sort()

last = 0
result = 0
for i in range(0,len(pound),2):
    start = pound[i]
    if last > start:
        start = last
    end = pound[i+1]
    depth = end - start

    value = depth // l 
    left = depth % l
    if left > 0:
        result += value + 1
        last = start + (value+1) * l
    else:
        result += value
        last = end

print(result)