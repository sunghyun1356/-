from collections import deque

def bfs(person, money):
    q = deque([(person, money)])
    while q:
        now_person, now_money = q.popleft()
        if now_person == "-":
            continue
        my_share = now_money - now_money // 10
        result[now_person] += my_share
        next_person = connection[now_person]
        next_money = now_money // 10
        if next_money > 0:
            q.append((next_person, next_money))

def solution(enroll, referral, seller, amount):
    global result, connection
    result = {person: 0 for person in enroll}
    connection = {enroll_person: referral_person for enroll_person, referral_person in zip(enroll, referral)}

    for seller_person, money in zip(seller, amount):
        bfs(seller_person, money * 100) 

    return [result[person] for person in enroll]