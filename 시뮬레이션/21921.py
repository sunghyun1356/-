import sys

input = sys.stdin.readline

def main():
    n, x = map(int, input().split())
    come = list(map(int, input().split()))

    current_sum = sum(come[:x])
    maximum = current_sum
    temp = 1

    for i in range(1, n - x + 1):
        current_sum = current_sum - come[i - 1] + come[i + x - 1]
        if current_sum > maximum:
            maximum = current_sum
            temp = 1
        elif current_sum == maximum:
            temp += 1

    if maximum == 0:
        print("SAD")
    else:
        print(maximum)
        print(temp)

if __name__ == "__main__":
    main()
