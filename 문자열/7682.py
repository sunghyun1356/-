"""문제
틱택토 게임은 두 명의 사람이 번갈아가며 말을 놓는 게임이다. 게임판은 3×3 격자판이며, 처음에는 비어 있다. 두 사람은 각각 X 또는 O 말을 번갈아가며 놓는데, 반드시 첫 번째 사람이 X를 놓고 두 번째 사람이 O를 놓는다. 어느 때든지 한 사람의 말이 가로, 세로, 대각선 방향으로 3칸을 잇는 데 성공하면 게임은 즉시 끝난다. 게임판이 가득 차도 게임은 끝난다.

게임판의 상태가 주어지면, 그 상태가 틱택토 게임에서 발생할 수 있는 최종 상태인지를 판별하시오.

입력
입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 줄은 9개의 문자를 포함하며, 'X', 'O', '.' 중 하나이다. '.'은 빈칸을 의미하며, 9개의 문자는 게임판에서 제일 윗 줄 왼쪽부터의 순서이다. 입력의 마지막에는 문자열 "end"가 주어진다.

출력
각 테스트 케이스마다 한 줄에 정답을 출력한다. 가능할 경우 "valid", 불가능할 경우 "invalid"를 출력한다."""

# 먼저 o의 개수와 x의 개수를 체크하고 x의 개수가 o보다 2개 많거나 o의 개수가 x의 개수보다 한개 더 많으면 안됨
# 
import sys
input = sys.stdin.readline

# 이길 수 있다면 체크 하기
def checking(string, player):
    result = False
    if player == string[0] == string[1] == string[2]\
        or player == string[3] == string[4] == string[5]\
            or player == string[0] == string[3] == string[6]\
                or player == string[1] == string[4] == string[7]\
                    or player == string[2] == string[5] == string[8]\
                        or player == string[0] == string[4] == string[8]\
                            or player == string[2] == string[4] == string[6]\
                                or player == string[6] == string[7] == string[8]:
                                    result = True
    return result

def checking_2(string):
    win_x, win_o = checking(string, 'X'), checking(string, 'O')
    num_x, num_o, num_dot = string.count('X'), string.count('O'), string.count('.')
    if (win_x and not win_o and num_x == num_o +1)\
        or (not win_x and win_o and num_x == num_o)\
            or (not win_x and not win_o and num_x == 5 and num_o == 4):
                return "valid"
    return "invalid"
answer =[]
while True:
    string = input().strip()
    if string == "end":
        break
    else:
        answer.append(checking_2(string))
if answer:
    print(*answer, sep="\n")

