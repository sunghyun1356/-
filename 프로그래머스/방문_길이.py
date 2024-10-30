order = list(input())

dx = [1,-1,0,0]
dy= [0,0,1,-1]

y = 0
x = 0
route = []
for o in order:
    if o == "U":
        y, x = y+dy[3],x+dx[3]
        route.append((y,x,y+dy[3],x+dx[3]),(y+dy[3],x+dx[3],y,x))
    elif o == "R":
        pass
    elif o == "L":
        pass
    else:
        pass

route = list(set(route))
print(len(route))