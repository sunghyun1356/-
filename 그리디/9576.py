case = int(input())  # 테스트 케이스 개수 입력
for _ in range(case):
    n, m = map(int, input().split())  # 책의 개수와 학생의 수 입력
    books = list(range(1, n + 1))  # 책 리스트 생성
    students = []  # 학생 요청 리스트 생성
    for _ in range(m):
        start, end = map(int, input().split())
        students.append((start, end))  # 학생이 원하는 범위 추가

    count = 0  # 배정된 책 개수 카운트
    students = sorted(students, key=lambda x: (x[1], x[0]))  # 끝나는 책 번호 기준으로 정렬

    for student in students:
        start, end = student
        for i in range(start, end + 1):
            if i in books:  # 책이 아직 남아있는지 확인
                books.remove(i)  # 해당 책 제거
                count += 1  # 책 배정
                break  # 한 명의 학생에게 한 권만 배정되므로 다음 학생으로 넘어감

    print(count)  # 배정된 책 개수 출력
