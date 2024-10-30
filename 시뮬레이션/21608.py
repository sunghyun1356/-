# 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 가지 정하는 함수 
# 여러개민면 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리 정하기
# 행의 번호가 가장 작고 열의 번호가 가장 작은 칸으로
### 한번에 ()로 넣고 sort돌리자

n = int(input())
likes = [[] for _ in range(n**2)]
# 해당 상황을 보여주는 그래프
graph = [[1e9]* n for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def check(who, like):
    # 1번째 조건 만족 (빈칸 찾기 - 상하좌우를 체크해준다)
    candidate = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1e9:
                count_like = 0
                count_blank = 0
                for k in range(4):
                    ny = i + dy[k]
                    nx = j + dx[k]
                    if 0<=ny<n and 0<=nx<n:
                        if graph[ny][nx] ==  1e9:
                            count_blank+=1
                        if graph[ny][nx] in like:
                            count_like+=1
                # 빈칸 수, 인접하는 학생의 수,그때의 i,j값
                candidate.append((count_like,i,j,count_blank))
    candidate = sorted(candidate, key = lambda x : (-x[0],-x[3], x[1], x[2]))
    graph[candidate[0][1]][candidate[0][2]] = who



for i in range(n**2):
    info = list(map(int, input().split()))
    likes[info[0]-1] = [info[1]-1,info[2]-1,info[3]-1,info[4]-1]
    check(info[0]-1, likes[info[0]-1])

answer = 0

for i in range(n):
    for j in range(n):
        value = graph[i][j]
        count_like = 0
        for k in range(4):
            ny = i + dy[k]
            nx = j + dx[k]
            if 0<=ny<n and 0<=nx<n:
                if graph[ny][nx] in likes[value]:
                    count_like+=1
        if count_like != 0:
            answer += 10**(count_like-1)
print(answer)