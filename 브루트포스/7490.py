import sys
input = sys.stdin.readline

operators = ["+", "-", ""]
digit = ["1","2","3","4","5","6","7","8","9"]
def evaluate_expression(expression):
    total = 0
    current_number = 0
    current_operator = '+'
    i = 0

    while i < len(expression):
        char = expression[i]

        if char.isdigit():
            num_str = char
            while i + 1 < len(expression) and expression[i + 1].isdigit():
                i += 1
                num_str += expression[i]
            current_number = int(num_str)

        if char in "+-" or i == len(expression) - 1:
            if current_operator == '+':
                total += current_number
            elif current_operator == '-':
                total -= current_number
            current_operator = char
            current_number = 0

        i += 1

    return total

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
        news = []
        find_expressions(1, number, str(numbers[0]), results, numbers)
        for expression in results:
            new = ""
            for i in range(len(expression)):
                if i == len(expression)-1:
                    new += expression[i]
                    break
                if expression[i] in "123456789" and expression[i+1] in "123456789":
                    new += expression[i] + " "
                else:
                    new += expression[i]
            news.append(new)
        news.sort()
        for n in news:
            print(n)
        print()

if __name__ == "__main__":
    main()
