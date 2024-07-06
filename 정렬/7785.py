n = int(input())
heap = set()
for i in range(n):
    a, b = input().split()
    if b == "enter":
        heap.add(a)
    else:
        heap.discard(a)
heap = sorted(list(heap), reverse=True)
for i in heap:
    print(i)
