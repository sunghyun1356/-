def check(eggs):
    cnt = 0
    for e in eggs:
        if e[0] <= 0:
            cnt +=1
    return cnt

def solution(depth, arr):
    global answer
    if depth == n:
        answer = max(answer, check(arr))
        return
    if arr[depth][0] <= 0:
        solution(depth+1, arr)
    else:
        isBroken = True
        for i in range(n):
            if depth != i and arr[i][0] > 0:
                isBroken = False
                arr[depth][0] -= arr[i][1]
                arr[i][0] -= arr[depth][1]
                solution(depth + 1, arr)
                arr[depth][0] += arr[i][1]
                arr[i][0] += arr[depth][1]
        if isBroken:
            solution(n, arr)
n = int(input())
egg = [list(map(int, input().split()))for _ in range(n)]
answer = 0
solution(0, egg)
print(answer)