from itertools import product

def check(users, emoticons, emoticon_discounts):
    target = 0
    total_profit = 0
    for user in users:
        profit = 0
        for disc, price in emoticon_discounts:
            if disc >= user[0]:
                profit += price * (1 - disc / 100)
        if profit >= user[1]:
            target += 1
        else:
            total_profit += profit
    return (target, total_profit)

def solution(users, emoticons):
    discounts = [10, 20, 30, 40]
    ways = list(product(discounts, repeat=len(emoticons)))
    candidate = []
    
    for way in ways:
        emoticon_discounts = list(zip(way, emoticons))
        candidate.append(check(users, emoticons, emoticon_discounts))
    
    candidate = sorted(candidate, key=lambda x: (-x[0], -x[1]))
    
    return list(candidate[0])
