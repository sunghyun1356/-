def solution(n, t, m, timetable):
    # timetable을 분 단위로 변환하고 오름차순으로 정렬
    timetable = sorted([int(time[:2]) * 60 + int(time[3:]) for time in timetable])
    
    # 첫 번째 버스는 9:00에 출발 (540분)
    bus_times = [540 + i * t for i in range(n)]  # 각 버스의 출발 시간 목록
    
    # 각 버스에 탑승할 크루를 추적하기 위한 인덱스
    index = 0
    
    for bus_time in bus_times:
        # 현재 버스에 태울 수 있는 크루 수 확인
        count = 0
        
        # 현재 버스 출발 시간에 도착한 크루들 중에서 태우기
        while index < len(timetable) and timetable[index] <= bus_time and count < m:
            index += 1
            count += 1
            
    # 마지막 버스에 탑승한 크루 확인
    if count < m:
        # 마지막 버스에 자리가 남아있으면
        return f"{bus_time // 60:02d}:{bus_time % 60:02d}"
    else:
        # 마지막으로 탑승한 크루의 시간 -1
        last_crew_time = timetable[index - 1] - 1
        return f"{last_crew_time // 60:02d}:{last_crew_time % 60:02d}"
