import sys
input = sys.stdin.readline


def main():
    thanos = list(input().strip())
    
    thanos_one_half = thanos.count('1')//2
    thanos_zero_half = thanos.count('0')//2
    one_temp = 0
    zero_temp = 0
    for i in range(len(thanos)-1, -1, -1):
        if thanos[i] == '0'  and zero_temp != thanos_zero_half:
            thanos[i] = ''
            zero_temp+=1
    for j in range(len(thanos)):
        if thanos[j] == '1' and one_temp != thanos_one_half:
            thanos[j] = ''
            one_temp +=1
    thanos = ''.join(thanos)
    print(thanos)

if __name__ == "__main__":
    main()
