"""문제 설명
두 개의 단어 begin, target과 단어의 집합 words가 있습니다. 아래와 같은 규칙을 이용하여 begin에서 target으로 변환하는 가장 짧은 변환 과정을 찾으려고 합니다.

1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
2. words에 있는 단어로만 변환할 수 있습니다.
예를 들어 begin이 "hit", target가 "cog", words가 ["hot","dot","dog","lot","log","cog"]라면 "hit" -> "hot" -> "dot" -> "dog" -> "cog"와 같이 4단계를 거쳐 변환할 수 있습니다.

두 개의 단어 begin, target과 단어의 집합 words가 매개변수로 주어질 때, 최소 몇 단계의 과정을 거쳐 begin을 target으로 변환할 수 있는지 return 하도록 solution 함수를 작성해주세요.

제한사항
각 단어는 알파벳 소문자로만 이루어져 있습니다.
각 단어의 길이는 3 이상 10 이하이며 모든 단어의 길이는 같습니다.
words에는 3개 이상 50개 이하의 단어가 있으며 중복되는 단어는 없습니다.
begin과 target은 같지 않습니다.
변환할 수 없는 경우에는 0를 return 합니다.
입출력 예
begin	target	words	return
"hit"	"cog"	["hot", "dot", "dog", "lot", "log", "cog"]	4
"hit"	"cog"	["hot", "dot", "dog", "lot", "log"]	0
입출력 예 설명
예제 #1
문제에 나온 예와 같습니다.

예제 #2
target인 "cog"는 words 안에 없기 때문에 변환할 수 없습니다."""

# begin에서 words로 이동할 수 있는지 확인
# 단어 차이가 1개만 나도록 해야한다. 
# 서로가 서로한테 연결되어있다면 bfs를 통해서 돌아가면서 최단거리를 찾아준다
from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    length = len(begin)
    graph = [[] for _ in range(len(words))]
    
    def compare(a, b):
        cnt = 0
        for i, j in zip(a, b):
            if i == j:
                cnt += 1
        return cnt == length - 1

    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if compare(words[i], words[j]):
                graph[i].append(j)
                graph[j].append(i)

    def BFS(begin):
        q = deque()
        visited = [False] * len(words)
        q.append(begin)
        ans = 0
        while q:
            size = len(q)
            for _ in range(size):
                now = q.popleft()
                if words[now] == target:
                    return ans
                visited[now] = True
                for word in graph[now]:
                    if not visited[word]:
                        q.append(word)
                        visited[word] = True
            ans += 1
        return 0  # BFS를 마치고도 target을 찾지 못했을 경우

    candidate = []
    for i in range(len(words)):
        if compare(begin, words[i]):
            candidate.append(i)

    answer = min(BFS(c) for c in candidate)+1
    return answer if answer != float('inf') else 0

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
