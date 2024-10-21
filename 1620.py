n,m = map(int, input().split())
poket = {}
poket_reverse = {}
for i in range(n):
    p = input()
    poket[p] = i+1
    poket_reverse[i+1] = p
order = []
for j in range(m):
    order = input()
    if order.isdigit():
        index = int(order)
        if index in poket_reverse:
            print(poket_reverse[index])
    else:
        if order in poket:
            print(poket[order])

