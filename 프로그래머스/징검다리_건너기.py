"""문제 설명
[본 문제는 정확성과 효율성 테스트 각각 점수가 있는 문제입니다.]

카카오 초등학교의 "니니즈 친구들"이 "라이언" 선생님과 함께 가을 소풍을 가는 중에 징검다리가 있는 개울을 만나서 건너편으로 건너려고 합니다. "라이언" 선생님은 "니니즈 친구들"이 무사히 징검다리를 건널 수 있도록 다음과 같이 규칙을 만들었습니다.

징검다리는 일렬로 놓여 있고 각 징검다리의 디딤돌에는 모두 숫자가 적혀 있으며 디딤돌의 숫자는 한 번 밟을 때마다 1씩 줄어듭니다.
디딤돌의 숫자가 0이 되면 더 이상 밟을 수 없으며 이때는 그 다음 디딤돌로 한번에 여러 칸을 건너 뛸 수 있습니다.
단, 다음으로 밟을 수 있는 디딤돌이 여러 개인 경우 무조건 가장 가까운 디딤돌로만 건너뛸 수 있습니다.
"니니즈 친구들"은 개울의 왼쪽에 있으며, 개울의 오른쪽 건너편에 도착해야 징검다리를 건넌 것으로 인정합니다.
"니니즈 친구들"은 한 번에 한 명씩 징검다리를 건너야 하며, 한 친구가 징검다리를 모두 건넌 후에 그 다음 친구가 건너기 시작합니다.

디딤돌에 적힌 숫자가 순서대로 담긴 배열 stones와 한 번에 건너뛸 수 있는 디딤돌의 최대 칸수 k가 매개변수로 주어질 때, 최대 몇 명까지 징검다리를 건널 수 있는지 return 하도록 solution 함수를 완성해주세요.

[제한사항]
징검다리를 건너야 하는 니니즈 친구들의 수는 무제한 이라고 간주합니다.
stones 배열의 크기는 1 이상 200,000 이하입니다.
stones 배열 각 원소들의 값은 1 이상 200,000,000 이하인 자연수입니다.
k는 1 이상 stones의 길이 이하인 자연수입니다.
[입출력 예]
stones	k	result
[2, 4, 5, 3, 2, 1, 4, 2, 5, 1]	3	3
입출력 예에 대한 설명
입출력 예 #1

첫 번째 친구는 다음과 같이 징검다리를 건널 수 있습니다.
step_stones_104.png

첫 번째 친구가 징검다리를 건넌 후 디딤돌에 적힌 숫자는 아래 그림과 같습니다.
두 번째 친구도 아래 그림과 같이 징검다리를 건널 수 있습니다.
step_stones_101.png

두 번째 친구가 징검다리를 건넌 후 디딤돌에 적힌 숫자는 아래 그림과 같습니다.
세 번째 친구도 아래 그림과 같이 징검다리를 건널 수 있습니다.
step_stones_102.png

세 번째 친구가 징검다리를 건넌 후 디딤돌에 적힌 숫자는 아래 그림과 같습니다.
네 번째 친구가 징검다리를 건너려면, 세 번째 디딤돌에서 일곱 번째 디딤돌로 네 칸을 건너뛰어야 합니다. 하지만 k = 3 이므로 건너뛸 수 없습니다.
step_stones_103.png

따라서 최대 3명이 디딤돌을 모두 건널 수 있습니다."""

# 왜 에러가 뜨는 것일 까????
def solution1(stones, k):
    n = len(stones)
    idx = -1
    max_gap = 1
    minimum = 0
    while True:
        minimum+=1
        idx = -1
        for i in range(n):
            stones[i] -=1
            if stones[i] > 0:
                max_gap = max(max_gap,i-idx)
                idx = i
            print(stones, idx,i, max_gap)
        if max_gap > k:
            return(minimum)


# 코드 공유

def solution(stones, k):
    stone = []
    for i,v in enumerate(stones):
        stone.append((v, i+1))
    stone.sort()
    
    before = [i-1 for i in range(len(stones)+2)]
    after = [i+1 for i in range(len(stones)+2)]
    
    answer = 0
    for i in stone:
        now_weight, now_index = i
        
        if after[now_index] - before[now_index] > k:
            answer = now_weight
            break
        
        # 그 전의 돌에 있던 것의 다음것은 현재의 다음 것이고
        after[before[now_index]] = after[now_index]
        # 지금기준 다음것에 해당하는 돌의 전의 것은 지금의 전것이다
        before[after[now_index]] = before[now_index]

    return answer
    
print(solution( [2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))