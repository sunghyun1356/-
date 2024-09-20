# 모두 다 연결되어있는지를 봐야한다.
# union & find ?
# union & find로 어떤 번호와 연결되어있는것들을 모두 뽑도록 해준다

# 그런데 자기 위에 부분만 되어있는건 어떻게 처리를 할까? 제일 최상단에 있는 놈들이 연결이 되도록 해야한다
# 다른 부분들도 업데이트가 되어야한다. 

def find(x):
    if parent[x-1] == x:
        return x
    else:
        return find(parent[x-1])

def union(a,b):
    a = find(a)
    b = find(b)
    if a < b :
        parent[b-1] = a
    else:
        parent[a-1] = b
        
n = int(input())
parent = list(i for i in range(1,n+1))
pair = int(input())
computers = [[]for _ in range(n)]
for i in range(pair):
    first, second = map(int, input().split())
    union(first, second)
    
cnt = 0

for i in range(n):
    if find(i) == 1:
        cnt +=1
print(cnt-1)

checked = [0 for _ in range(1000000)]


n = int(input())
for i in range(n):
    start, end  = map(int, input().split())
    computers[start][end] = computers[end][start] = 1
