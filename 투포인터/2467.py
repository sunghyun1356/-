n = int(input())
liquid = list(map(int, input().split()))

start = 0
end = len(liquid) - 1
best_pair = (liquid[start], liquid[end])
closest_sum = abs(liquid[start] + liquid[end])

while start < end:
    current_sum = liquid[start] + liquid[end]

    if abs(current_sum) < closest_sum:
        closest_sum = abs(current_sum)
        best_pair = (liquid[start], liquid[end])

    if current_sum > 0:
        end -= 1
    elif current_sum < 0:
        start += 1
    else:
        break

print(best_pair[0], best_pair[1])
