import sys
input = sys.stdin.readline


# 각각의 상태를 저장해놓고 그 상태가 반복되면 반환하도록 해야겠다
# -> 계속 for문을 돌려야한다는 것에서 뭔가 하자가 있다.
# 부르트포스로 풀 수가 없다 -> 시간복잡도 위반


def change(bulb, num):
    global n
    for i in range(num-1, num+2):
        if 0<=i<n:
            bulb[i] = 1 - bulb[i]

def go(bulb, second):
    global n
    ans = 0
    
    for i in range(1,n):
        if bulb[i-1] != second[i-1]:
            change(bulb, i)
            ans +=1
    for i in range(n):
        if bulb[i] != second[i]:
            return False, ans
    return True, ans

MAX_SIZE = 100000
n = int(input())

first = list(map(int, input()))
second = list(map(int, input()))


