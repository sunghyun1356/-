import sys
from itertools import combinations
input = sys.stdin.readline

n, m, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]


# 적들이 움직일 때 만약에 y좌표가 n보다 작을 때만 추가해준다
def move(enemies):
    new_enemies = []
    for y, x in enemies:
        if y + 1 < n:
            new_enemies.append((y + 1, x))
    return new_enemies

# d의 거리에 따라 각각을 넣어준다
def enemy_check(y, x, enemies, d):
    target_enemy = None
    min_dist = d + 1
    for i, j in enemies:
        dist = (n - i) + abs(x - j)
        if dist <= d:
            if dist < min_dist:
                min_dist = dist
                target_enemy = (i, j)
            elif dist == min_dist and j < target_enemy[1]:
                target_enemy = (i, j)
    return target_enemy

# 적들 위치를 저장해 놨다가 적들이 남아있을때 각각의 궁수에 대해서 적을 체크하고 공격하고 죽은 애들은 빼준다.
def simulate(archers):
    enemies = [(i, j) for i in range(n) for j in range(m) if graph[i][j] == 1]
    count = 0
    while enemies:
        attacked = set()
        for archer in archers:
            target = enemy_check(n, archer, enemies, d)
            if target:
                attacked.add(target)
        count += len(attacked)
        enemies = [e for e in enemies if e not in attacked]
        enemies = move(enemies)
    return count

def main():
    maximum_count = 0
    for archers in combinations(range(m), 3):
        maximum_count = max(maximum_count, simulate(archers))
    print(maximum_count)

if __name__ == "__main__":
    main()
