import sys
input = sys.stdin.readline

def check(arr, n, h):
    for sj in range(1, n + 1):
        j = sj
        for i in range(1, h + 1):
            if arr[i][j] == 1:
                j += 1
            elif arr[i][j - 1] == 1:
                j -= 1
        if j != sj:
            return False
    return True

def dfs(arr, pos, current_cnt, start, max_cnt, total_positions, h):
    if current_cnt == max_cnt:
        return check(arr, len(arr[0]) - 2, h)

    for j in range(start, total_positions):
        ti, tj = pos[j]
        if arr[ti][tj - 1] == 0 and arr[ti][tj] == 0 and arr[ti][tj + 1] == 0:
            arr[ti][tj] = 1
            if dfs(arr, pos, current_cnt + 1, j + 1, max_cnt, total_positions, h):
                return True
            arr[ti][tj] = 0

    return False

def main():
    n, m, h = map(int, input().split())
    arr = [[0] * (n + 2) for _ in range(h + 1)]
    for _ in range(m):
        ti, tj = map(int, input().split())
        arr[ti][tj] = 1

    pos = []
    for i in range(1, h + 1):
        for j in range(1, n):
            if arr[i][j] == 0 and arr[i][j-1] == 0 and arr[i][j+1] == 0:
                pos.append((i, j))
    total_positions = len(pos)

    for max_cnt in range(4):
        if dfs(arr, pos, 0, 0, max_cnt, total_positions, h):
            print(max_cnt)
            return
    print(-1)

if __name__ == "__main__":
    main()
