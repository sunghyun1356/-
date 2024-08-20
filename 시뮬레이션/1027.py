import sys
import math
input = sys.stdin.readline

# 각도를 사용하자 -> 어차피 탄젠트 값은 같다

def main():
    n = int(input())
    buildings = list(map(int, input().split()))

    def count_visible_buildings(i):
        
        count = 0
        max_slope = float('inf')
        
        for j in range(i-1, -1, -1):
            slope = (buildings[i] - buildings[j]) / (i - j)
            if slope < max_slope:
                max_slope = slope
                count += 1

        max_slope = float('-inf')

        for j in range(i + 1, n):
            slope = (buildings[j] - buildings[i]) / (j - i)
            if slope > max_slope:
                max_slope = slope
                count += 1
        return count

    max_visible = 0

    for i in range(n):
        max_visible = max(max_visible, count_visible_buildings(i))
    if n == 1:
        max_visible=0
    print(max_visible)

if __name__ == "__main__":
    main()

