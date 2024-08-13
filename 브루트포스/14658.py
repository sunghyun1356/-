n, m, l, k = map(int, input().split())
stars = []

for _ in range(k):
    x, y = map(int, input().split())
    stars.append((y, x))

max_stars = 0

stars.sort()

# 별 하나당 별 하나씩 연결해서 그게 속하는지 판단해준다
for i in range(k):
    for j in range(k):
        top_left_y = stars[i][0]
        top_left_x = stars[j][1]
        count = 0

        for star in stars:
            if top_left_y <= star[0] <= top_left_y + l and top_left_x <= star[1] <= top_left_x + l:
                count += 1

        max_stars = max(max_stars, count)

print(k - max_stars)

