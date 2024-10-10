from collections import deque
def solution(plans):
    maximum = 0
    tasks = []
    
    for plan in plans:
        hour, minute = map(int, plan[1].split(":"))
        start_time = hour * 60 + minute 
        left = int(plan[2])
        maximum += left
        tasks.append((plan[0], start_time, left))
    
    tasks.sort(key=lambda x: x[1]) 
    
    temp = deque()  
    candidate = []  
    
    current_task = tasks.pop(0)
    current_subject, current_time, current_left = current_task
    time = current_time
    
    while temp or tasks or current_left > 0:
        time += 1
        current_left -= 1

        if current_left == 0:
            candidate.append(current_subject)
            if tasks and tasks[0][1] == time:
                current_task = tasks.pop(0) 
                current_subject, current_time, current_left = current_task
            elif temp: 
                current_task = temp.pop()
                current_subject, current_time, current_left = current_task


        if tasks and tasks[0][1] == time:
            temp.append((current_subject, current_time, current_left))
            current_task = tasks.pop(0) 
            current_subject, current_time, current_left = current_task

    
    return candidate
