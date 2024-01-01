"""문제 설명
n명의 권투선수가 권투 대회에 참여했고 각각 1번부터 n번까지 번호를 받았습니다. 권투 경기는 1대1 방식으로 진행이 되고, 만약 A 선수가 B 선수보다 실력이 좋다면 A 선수는 B 선수를 항상 이깁니다. 심판은 주어진 경기 결과를 가지고 선수들의 순위를 매기려 합니다. 하지만 몇몇 경기 결과를 분실하여 정확하게 순위를 매길 수 없습니다.

선수의 수 n, 경기 결과를 담은 2차원 배열 results가 매개변수로 주어질 때 정확하게 순위를 매길 수 있는 선수의 수를 return 하도록 solution 함수를 작성해주세요.

제한사항
선수의 수는 1명 이상 100명 이하입니다.
경기 결과는 1개 이상 4,500개 이하입니다.
results 배열 각 행 [A, B]는 A 선수가 B 선수를 이겼다는 의미입니다.
모든 경기 결과에는 모순이 없습니다.
입출력 예
n	results	return
5	[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]	2
입출력 예 설명
2번 선수는 [1, 3, 4] 선수에게 패배했고 5번 선수에게 승리했기 때문에 4위입니다.
5번 선수는 4위인 2번 선수에게 패배했기 때문에 5위입니다."""

from collections import deque

def solution(n, results):
    # 각 선수에 대한 이긴 경우와 진 경우를 저장할 딕셔너리 생성
    win = {i: set() for i in range(1, n + 1)}
    lose = {i: set() for i in range(1, n + 1)}

    # 각 선수에 대한 이긴 선수와 진 선수 정보 업데이트
    for player in results:
        win[player[0]].add(player[1])
        lose[player[1]].add(player[0])

    # 이긴 경우에 대한 BFS 탐색
    def WIN_BFS(start, result_dict):
        q = deque([start])
        visited = set()

        while q:
            now = q.popleft()
            visited.add(now)
            
            for player in result_dict[now]:
                if player not in visited:
                    q.append(player)
                    result_dict[start].add(player)
                    visited.add(player)

    # 진 경우에 대한 BFS 탐색
    def LOSE_BFS(start, result_dict):
        q = deque([start])
        visited = set()

        while q:
            now = q.popleft()
            visited.add(now)

            for player in result_dict[now]:
                if player not in visited:
                    q.append(player)
                    result_dict[start].add(player)
                    visited.add(player)

    # 모든 선수에 대해 이긴 경우와 진 경우를 BFS로 업데이트
    for i in range(1, n + 1):
        WIN_BFS(i, win)
        LOSE_BFS(i, lose)

    # 순위를 확정할 수 있는 선수 개수 세기
    answer = 0
    for i in range(1, n + 1):
        if len(win[i]) + len(lose[i]) == n - 1:
            answer += 1

    return answer


