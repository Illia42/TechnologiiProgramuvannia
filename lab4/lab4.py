import re

def get_tokens(expression):
    expr = expression.replace(' ', '')
    return re.findall(r'\d+\.\d+|\d+|[+\-*/^()]', expr)

def to_rpn(tokens):
    priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    result = []
    stack = []

    for item in tokens:
        if re.match(r'\d+\.\d+|\d+', item):
            result.append(item)
        elif item == '(':
            stack.append(item)
        elif item == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            if stack:
                stack.pop() 
        elif item in priority:
            while stack and stack[-1] != '(' and priority.get(stack[-1], 0) >= priority[item]:
                result.append(stack.pop())
            stack.append(item)

    while stack:
        result.append(stack.pop())

    return result


def calculate_rpn(rpn_list):
    stack = []
    
    for item in rpn_list:
        if re.match(r'\d+\.\d+|\d+', item):
            stack.append(float(item))
        else:
            b = stack.pop()
            a = stack.pop()
            
            if item == '+':
                stack.append(a + b)
            elif item == '-':
                stack.append(a - b)
            elif item == '*':
                stack.append(a * b)
            elif item == '/':
                stack.append(a / b)
            elif item == '^':
                stack.append(a ** b)
                
    return stack[0]

expr = input("Введіть математичний вираз: ")

tokens = get_tokens(expr)
rpn = to_rpn(tokens)
res = calculate_rpn(rpn)

print("1. ЗПЗ:", " ".join(rpn))
print("2. Результат:", res)