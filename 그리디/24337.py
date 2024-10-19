n, a, b = map(int, input().split())
building = [0] * n

if a > b:
    if a + b > n:
        for i in range(a):
            building[i] = i + 1
        for j in range(b - 1):
            building[n - j - 1] = j + 1
    elif a + b < n:
        for i in range(a):
            building[i] = i + 1
        for j in range(b):
            building[n - j - 1] = j + 1
        for k in range(n):
            if building[k] == 0:
                building[k] = 1
    else:
        for i in range(a):
            building[i] = i + 1
        for j in range(b - 1):
            building[n - j - 1] = j + 1
        building[a] = building[a - 1]

elif a < b:
    if a + b < n:
        for j in range(b):
            building[n - j - 1] = j + 1
        for i in range(a):
            building[i] = i + 1
        for k in range(n):
            if building[k] == 0:
                building[k] = 1
    elif a + b > n:
        for j in range(b):
            building[n - j - 1] = j + 1
        for i in range(n - b):
            building[i] = i + 1
    else:
        for j in range(b):
            building[n - j - 1] = j + 1
        for i in range(a - 1):
            building[i] = i + 1
        building[a - 1] = building[a]

else:
    if a + b < n:
        for i in range(a):
            building[i] = i + 1
        for j in range(b):
            building[n - j - 1] = j + 1
        for k in range(n):
            if building[k] == 0:
                building[k] = 1
    elif a + b > n:
        for i in range(a):
            building[i] = i + 1
        for j in range(b):
            building[n - j - 1] = j + 1
    else:
        for i in range(a):
            building[i] = i + 1
        for j in range(b):
            building[n - j - 1] = j + 1
if a < 0 or b <0 or a>n or b>n:
    print(-1)
else:
    print(" ".join(map(str, building)))
