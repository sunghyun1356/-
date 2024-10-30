# 그냥 순서대로 존재하는지를 check 한다
skill = list(input())
skill_trees = list(input().split(","))
answer = 0

def check(skill):
    temp = ""
    for i in skill:
        if i in skill:
            temp+=i
    if temp == skill:
        return True
    return False
for s in skill_trees:
    if check(skill):
        answer+=1