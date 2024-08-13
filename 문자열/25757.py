var = input().split()
n , g = int(var[0]), str(var[1])
name = []
for _ in range(n):
    name.append(input())
name = list(set(name))
def game(name, g):
    if g == 'Y':
        print(len(name))
    elif g == 'F':
        print(len(name)//2)
    elif g == 'O':
        print(len(name)//3)

game(name, g)