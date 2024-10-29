graph = [list(map(int, input().split())) for _ in range(19)]

def check_left_right(y, x, value):
    fx, sx = x - 1, x + 1
    number = 1
    while fx >= 0 and graph[y][fx] == value:
        fx -= 1
        number += 1
    while sx < 19 and graph[y][sx] == value:
        sx += 1
        number += 1
    return number == 5

def check_up_down(y, x, value):
    fy, sy = y - 1, y + 1
    number = 1
    while fy >= 0 and graph[fy][x] == value:
        fy -= 1
        number += 1
    while sy < 19 and graph[sy][x] == value:
        sy += 1
        number += 1
    return number == 5

def check_diagonal(y, x, value):
    fy, fx = y - 1, x - 1
    sy, sx = y + 1, x + 1
    number = 1
    leftmost_y, leftmost_x = y, x
    while fy >= 0 and fx >= 0 and graph[fy][fx] == value:
        fy -= 1
        fx -= 1
        number += 1
        leftmost_y, leftmost_x = fy + 1, fx + 1
    while sy < 19 and sx < 19 and graph[sy][sx] == value:
        sy += 1
        sx += 1
        number += 1
    if number == 5:
        return [True, leftmost_y, leftmost_x]

    # Top-right to bottom-left
    ay, ax = y - 1, x + 1
    by, bx = y + 1, x - 1
    number = 1
    leftmost_y, leftmost_x = y, x
    while ay >= 0 and ax < 19 and graph[ay][ax] == value:
        ay -= 1
        ax += 1
        number += 1
    while by < 19 and bx >= 0 and graph[by][bx] == value:
        by += 1
        bx -= 1
        number += 1
        leftmost_y, leftmost_x = by - 1, bx + 1
    if number == 5:
        return [True, leftmost_y, leftmost_x]

    return None

temp = False
for i in range(19):
    if temp:
        break
    for j in range(19):
        if graph[i][j] == 1:
            if check_up_down(i, j, 1) or check_left_right(i, j, 1):
                print(1)
                print(i + 1, j + 1)
                temp = True
                break
            diagonal_result = check_diagonal(i, j, 1)
            if diagonal_result and diagonal_result[0]:
                print(1)
                print(diagonal_result[1] + 1, diagonal_result[2] + 1)
                temp = True
                break
                
        elif graph[i][j] == 2:
            if check_up_down(i, j, 2) or check_left_right(i, j, 2):
                print(2)
                print(i + 1, j + 1)
                temp = True
                break
            diagonal_result = check_diagonal(i, j, 2)
            if diagonal_result and diagonal_result[0]:
                print(2)
                print(diagonal_result[1] + 1, diagonal_result[2] + 1)
                temp = True
                break

if not temp:
    print(0)
