def SORT(s):
    return "".join(sorted(s))

def REVERSE(s):
    s = list(s)
    s = s[::-1]
    return "".join(s)

def REPEAT(s, k):
    return s * int(k)

def solution(s):
    # 스택을 사용하여 중첩된 괄호 구조를 해결
    stack = []
    
    i = 0
    while i < len(s):
        if s[i] == ')':  # 닫는 괄호를 만나면
            # 가장 마지막 여는 괄호까지의 내용을 처리
            temp = []
            while stack and stack[-1] != '(':
                temp.append(stack.pop())
            temp.reverse()  # 원래 순서대로 재정렬
            
            stack.pop()  # 여는 괄호 '(' 제거
            
            # 함수 이름 추출
            function = []
            while stack and stack[-1].isupper():
                function.append(stack.pop())
            function.reverse()
            function_name = "".join(function)
            
            # temp를 문자열로 변환
            content = "".join(temp)
            
            # 함수 실행
            if function_name == "REVERSE":
                result = REVERSE(content)
            elif function_name == "SORT":
                result = SORT(content)
            elif function_name == "REPEAT":
                word, number = content.split(",")
                result = REPEAT(word, number)
            else:
                result = content  # 함수 이름이 잘못된 경우 원래 문자열 유지
            
            # 결과를 스택에 다시 추가
            stack.append(result)
        else:
            # '('나 함수 이름, 일반 문자를 스택에 추가
            stack.append(s[i])
        
        i += 1
    
    # 최종 결과 출력
    result = "".join(stack)
    print("결과:", result)

# 테스트 실행
s = "REVERSE(SORT(REPEAT(abc,3)ab(SORT(ab)d)))"
solution(s)
