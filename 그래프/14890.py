import sys
input = sys.stdin.readline



def check_path(line,n,l):
    # 경사로가 불가능
    # 중첩되는 경우
    # 차이가 1이 아닌경우
    # 낮은 칸의 높이가 같지 x
    # 경사로를 높다가 범위를 벗어남

    check = [False for _ in range(n)]
    for i in range(1, n):
        if abs(line[i-1] - line[i])>1:
            return False
        else:
            if (line[i-1]-line[i])==1:
                for j in range(l):
                    if i+j>=n:
                        return False
                    if line[i]!=line[i+j]:
                        return False
                    if check[i+j] == True:
                        return False
                    if check[i+j] == False:
                        check[i+j] = True
            elif (line[i-1] - line[i]) == -1:
                for j in range(l):
                    if i-1-j < 0:
                        return False
                    if line[i-1]!=line[i-1-j]:
                        return False
                    if check[i-1-j]== True:
                        return False
                    if check[i-j-1]== False:
                        check[i-j-1]= True
    return True




def main():
    n, l = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    count = 0
    for i in range(n):
        if check_path(graph[i],n,l):
            count += 1

    for i in range(n):
        column = [graph[j][i] for j in range(n)]
        if check_path(column,n,l):
            count += 1
    print(count)
    
if __name__ == "__main__":
    main()