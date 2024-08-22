import sys

input = sys.stdin.readline

def main():
    n, m = map(int, input().split())    
    keywords = set(input().strip() for _ in range(n))
    for _ in range(m):
        word_set = set(input().strip().split(','))
        keywords -= word_set
        print(len(keywords))
        
if __name__ == "__main__":
    main()
