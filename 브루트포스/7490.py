import sys
input = sys.stdin.readline

operators = ["+", "-", ""]

def evaluate_expression(expression):
    expression = expression.replace(" ", "")
    return eval(expression)

def find_expressions(depth, length, current_expression, results, numbers):
    if depth == length:
        if evaluate_expression(current_expression) == 0:
            results.append(current_expression)
        return
    
    for operator in operators:
        next_num = numbers[depth]
        find_expressions(depth + 1, length, current_expression + operator + str(next_num), results, numbers)

def main():
    n = int(input().strip())
    for _ in range(n):
        number = int(input().strip())
        numbers = list(range(1, number + 1))
        results = []
        find_expressions(1, number, str(numbers[0]), results, numbers)
        for expression in results:
            print(expression)

if __name__ == "__main__":
    main()
