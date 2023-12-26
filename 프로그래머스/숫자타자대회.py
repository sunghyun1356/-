"""문제 설명
그림.png
위와 같은 모양으로 배열된 숫자 자판이 있습니다. 숫자 타자 대회는 이 동일한 자판을 사용하여 숫자로만 이루어진 긴 문자열을 누가 가장 빠르게 타이핑하는지 겨루는 대회입니다.

대회에 참가하려는 민희는 두 엄지 손가락을 이용하여 타이핑을 합니다. 민희는 항상 왼손 엄지를 4 위에, 오른손 엄지를 6 위에 두고 타이핑을 시작합니다. 엄지 손가락을 움직여 다음 숫자를 누르는 데에는 일정 시간이 듭니다. 민희는 어떤 두 숫자를 연속으로 입력하는 시간 비용을 몇몇 가중치로 분류하였습니다.

이동하지 않고 제자리에서 다시 누르는 것은 가중치가 1입니다.
상하좌우로 인접한 숫자로 이동하여 누르는 것은 가중치가 2입니다.
대각선으로 인접한 숫자로 이동하여 누르는 것은 가중치가 3입니다.
같지 않고 인접하지 않은 숫자를 누를 때는 위 규칙에 따라 가중치 합이 최소가 되는 경로를 따릅니다.
예를 들어 1 위에 있던 손가락을 0 으로 이동하여 누르는 것은 2 + 2 + 3 = 7 만큼의 가중치를 갖습니다.
단, 숫자 자판은 버튼의 크기가 작기 때문에 같은 숫자 버튼 위에 동시에 두 엄지 손가락을 올려놓을 수 없습니다. 즉, 어떤 숫자를 눌러야 할 차례에 그 숫자 위에 올려져 있는 손가락이 있다면 반드시 그 손가락으로 눌러야 합니다.

숫자로 이루어진 문자열 numbers가 주어졌을 때 최소한의 시간으로 타이핑을 하는 경우의 가중치 합을 return 하도록 solution 함수를 완성해주세요.

제한사항
1 ≤ numbers의 길이 ≤ 100,000
numbers는 아라비아 숫자로만 이루어진 문자열입니다.
입출력 예
numbers	result
"1756"	10
"5123"	8
입출력 예 설명
입출력 예 #1
왼손 엄지로 17, 오른손 엄지로 56을 누르면 가중치 10으로 최소입니다.

입출력 예 #2
오른손 엄지로 5, 왼손 엄지로 123을 누르거나 오른손 엄지로 5, 왼손 엄지로 1, 오른손 엄지로 23을 누르면 가중치 8로 최소입니다."""

# 못품 / 존나 어려움 어떻게 해야할지 모르겠음
# 해결은 각각의 숫자에서 갈 수 있는 가중치들을 모두 구해서



costs =     [[1, 7, 6, 7, 5, 4, 5, 3, 2, 3]
            ,[7, 1, 2, 4, 2, 3, 5, 4, 5, 6]
            ,[6, 2, 1, 2, 3, 2, 3, 5, 4, 5]
            ,[7, 4, 2, 1, 5, 3, 2, 6, 5, 4]
            ,[5, 2, 3, 5, 1, 2, 4, 2, 3, 5]
            ,[4, 3, 2, 3, 2, 1, 2, 3, 2, 3]
            ,[5, 5, 3, 2, 4, 2, 1, 5, 3, 2]
            ,[3, 4, 5, 6, 2, 3, 5, 1, 2, 4]
            ,[2, 5, 4, 5, 3, 2, 3, 2, 1, 2]
            ,[3, 6, 5, 4, 5, 3, 2, 4, 2, 1]]

def solution(numbers):
    now_weight = 0
    left_pos = 4
    right_pos = 6
    all_dict = {}
    finger_pos = (left_pos, right_pos)
    all_dict[finger_pos] = now_weight
    
    for str_num in numbers:
        num = int(str_num)
        curr_dict = {}
        for finger_pos, weight in all_dict.items():
            left_pos, right_pos = finger_pos
            if right_pos == num:
                # 기존의 손을 한번 더 사용해서 눌러줄거니까
                if not (left_pos, num) in curr_dict.keys() or curr_dict[(left_pos, num)] > weight + 1:
                    curr_dict[(left_pos, num)] = weight + 1
            elif left_pos == num:
                if not (num, right_pos) in curr_dict.keys() or curr_dict[(num, right_pos)] > weight + 1:
                    curr_dict[(num, right_pos)] = weight + 1
            else:
                # 다른 손이나 같은 손으로 다른 숫자를 눌러줘야 할 때
                
                # 왼쪽 손을 사용안할 때 -> 다시 왼쪽 손을 사용한다음 오른쪽을 사용하는데 오른쪽의 가중치를 더해준다
                if not (left_pos, num) in curr_dict.keys() or curr_dict[(left_pos, num)] > weight + costs[right_pos][num]:
                    curr_dict[(left_pos, num)] = weight + costs[right_pos][num]
                if not (num, right_pos) in curr_dict.keys() or curr_dict[(num, right_pos)] > weight + costs[left_pos][num]:
                    curr_dict[(num, right_pos)] = weight + costs[left_pos][num]
        all_dict = curr_dict

    return min(list(all_dict.values()))