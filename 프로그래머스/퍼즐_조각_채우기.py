"""문제 설명
테이블 위에 놓인 퍼즐 조각을 게임 보드의 빈 공간에 적절히 올려놓으려 합니다. 게임 보드와 테이블은 모두 각 칸이 1x1 크기인 정사각 격자 모양입니다. 이때, 다음 규칙에 따라 테이블 위에 놓인 퍼즐 조각을 게임 보드의 빈칸에 채우면 됩니다.

조각은 한 번에 하나씩 채워 넣습니다.
조각을 회전시킬 수 있습니다.
조각을 뒤집을 수는 없습니다.
게임 보드에 새로 채워 넣은 퍼즐 조각과 인접한 칸이 비어있으면 안 됩니다.
다음은 퍼즐 조각을 채우는 예시입니다.

puzzle_5.png

위 그림에서 왼쪽은 현재 게임 보드의 상태를, 오른쪽은 테이블 위에 놓인 퍼즐 조각들을 나타냅니다. 테이블 위에 놓인 퍼즐 조각들 또한 마찬가지로 [상,하,좌,우]로 인접해 붙어있는 경우는 없으며, 흰 칸은 퍼즐이 놓이지 않은 빈 공간을 나타냅니다. 모든 퍼즐 조각은 격자 칸에 딱 맞게 놓여있으며, 격자 칸을 벗어나거나, 걸쳐 있는 등 잘못 놓인 경우는 없습니다.

이때, 아래 그림과 같이 3,4,5번 조각을 격자 칸에 놓으면 규칙에 어긋나므로 불가능한 경우입니다.

puzzle_6.png

3번 조각을 놓고 4번 조각을 놓기 전에 위쪽으로 인접한 칸에 빈칸이 생깁니다.
5번 조각의 양 옆으로 인접한 칸에 빈칸이 생깁니다.
다음은 규칙에 맞게 최대한 많은 조각을 게임 보드에 채워 넣은 모습입니다.

puzzle_7.png

최대한 많은 조각을 채워 넣으면 총 14칸을 채울 수 있습니다.

현재 게임 보드의 상태 game_board, 테이블 위에 놓인 퍼즐 조각의 상태 table이 매개변수로 주어집니다. 규칙에 맞게 최대한 많은 퍼즐 조각을 채워 넣을 경우, 총 몇 칸을 채울 수 있는지 return 하도록 solution 함수를 완성해주세요.

제한사항
3 ≤ game_board의 행 길이 ≤ 50
game_board의 각 열 길이 = game_board의 행 길이
즉, 게임 보드는 정사각 격자 모양입니다.
game_board의 모든 원소는 0 또는 1입니다.
0은 빈칸, 1은 이미 채워진 칸을 나타냅니다.
퍼즐 조각이 놓일 빈칸은 1 x 1 크기 정사각형이 최소 1개에서 최대 6개까지 연결된 형태로만 주어집니다.
table의 행 길이 = game_board의 행 길이
table의 각 열 길이 = table의 행 길이
즉, 테이블은 game_board와 같은 크기의 정사각 격자 모양입니다.
table의 모든 원소는 0 또는 1입니다.
0은 빈칸, 1은 조각이 놓인 칸을 나타냅니다.
퍼즐 조각은 1 x 1 크기 정사각형이 최소 1개에서 최대 6개까지 연결된 형태로만 주어집니다.
game_board에는 반드시 하나 이상의 빈칸이 있습니다.
table에는 반드시 하나 이상의 블록이 놓여 있습니다.
입출력 예
game_board	table	result
[[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]	[[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]	14
[[0,0,0],[1,1,0],[1,1,1]]	[[1,1,1],[1,0,0],[0,0,0]]	0
입출력 예 설명
입출력 예 #1

입력은 다음과 같은 형태이며, 문제의 예시와 같습니다.

puzzle_9.png

입출력 예 #2

블록의 회전은 가능하지만, 뒤집을 수는 없습니다."""

# 블록들의 모양과 위치를 파악한다
# 근데 좌표가 안맞는것 어떻게 하지?
# 이때의 좌표를 정렬하여서 한다
# 두개를 비교하기 위해서 각각을 0,0부터 시작하도록 만든다.
# 회전 배열[y][x] => 배열[x][n-y-1]

from collections import deque
import copy
global answer
answer = 0

dx = [0,0,1,-1]
dy = [1,-1,0,0]

game = [] #게임 보드의 비어있는 공간
block = [] #블락들이 놓여져 있는 공간

def bfs(y,x,n,visited,array,check):
    space = []
    q = deque()
    q.append([y,x])
    space.append([y,x])
    visited[y][x] = True
    while q:
        now_y, now_x = q.popleft()
        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if visited[ny][nx] == False and array[ny][nx] == check:
                    visited[ny][nx] = True
                    q.append([ny,nx])
                    space.append([ny,nx])
    return sorted(space)


def rotate(block, n):
    new_board = []
    for b in block:
        new_board.append([b[1],n-1-b[0]])
    return sorted(fixed(new_board,n))

def fixed(block, n):
    change = []
    minimum_y = n
    minimum_x = n
    #원래의 블락값에서 가장 최소인 것들을 구해서 그걸 
    for i in block:
        minimum_y = min(minimum_y, i[0])
        minimum_x = min(minimum_x, i[1])
    for y, x in block:
        change.append([y-minimum_y, x-minimum_x])
    return sorted(change)

def solution(game_board, table):
    global answer
    n = len(game_board)
    
    # 게임 보드에 비어져있는 공간을 check
    visited_game = [[False for _ in range(n)]for _ in range(n)]
    # 테이블(블락)이 채워져 있는 공간을 check
    visited_table = [[False for _ in range(n)]for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            
            if game_board[i][j] == 0 and visited_game[i][j] == False:
                #비어져 있는 공간에 bfs를 사용해서 좌표값을 넣어준다
                game.append(bfs(i,j,n,visited_game,game_board,0))
            
            if table[i][j] ==1  and visited_table[i][j] == False:
                #블락이 채워져 있는 공간에 bfs를 사용해서 좌표값을 넣어준다
                block.append(bfs(i,j,n,visited_table, table, 1))
            else:
                continue

    table_block = []
    for i in block:
        table_block.append(fixed(i, n))
    game_block = []
    for j in game:
        game_block.append(fixed(j,n))
    for g in game_block:
        if g in table_block:
            answer+=len(g)
            table_block.remove(g)
        else:
            flag = False
            for t in table_block:
                temp = copy.copy(t)
                for i in range(4):
                    if g == temp:
                        answer += len(g)
                        table_block.remove(t)
                        flag=True
                        break
                    temp = rotate(temp, n)
                if flag:
                    break
    return answer
                
print(solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]],[[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]))