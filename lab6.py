from LinkedStack import LinkedStack

def is_balanced(exp):
    s = LinkedStack()
    for character in exp:
       # Push open braces to stack
        if character in ['(', '[', '{']:
           s.push(character)
        elif character == '}':
           # Top of stack must be close curly brace
           if s.is_empty() or s.peek() != '{':
               return False
           else:
               s.pop()
        elif character == ')':
            # top of stack must be open parenthesis
            if s.is_empty() or s.peek() != '(':
                return False
            else:
                s.pop()
        elif character == ']':
            # top of stack must be open square bracket
            if s.is_empty() or s.peek() != '[':
                return False
            else:
                s.pop()
    return s.is_empty()
    

def precedence(operator):
    '''Assigns numerical value to operator precedence for comparison purposes'''
    if operator == "+" or operator == "-":
        return 1
    elif operator == "*" or operator == "/":
        return 2
    elif operator == "^":
        return 3
    elif operator in ["(", "[", "{"]:
        return 0
    

def convertToPostfix(infix):
    operatorStack = LinkedStack()
    postfix = ""
    invalidChar = False
    for char in infix:
        if char.isdigit():
            postfix += char + " "
        elif char == "^":
            operatorStack.push(char)
        elif char in ["+", "-", "*", "/"]:
            while not operatorStack.is_empty() and precedence(char) <= precedence(operatorStack.peek()):
                postfix += operatorStack.peek() + " "
                operatorStack.pop()
            operatorStack.push(char)            
        elif char == "(":
            operatorStack.push(char)
        elif char == ")":
            topOperator = operatorStack.pop()
            while topOperator != "(":
                postfix += topOperator + " "
                topOperator = operatorStack.pop()
        elif char == "[":
            operatorStack.push(char)
        elif char == "]":
            topOperator = operatorStack.pop()
            while topOperator != "[":
                postfix += topOperator + " "
                topOperator = operatorStack.pop() 
        elif char == "{":
            operatorStack.push(char)
        elif char == "}":
            topOperator = operatorStack.pop()
            while topOperator != "[":
                postfix += topOperator + " "
                topOperator = operatorStack.pop()              
        else:
            invalidChar = True
            break
    if invalidChar:
        return f"Invalid character in string: {char}"
    else:
        while not operatorStack.is_empty():
            topOperator = operatorStack.pop()
            postfix += topOperator + " "
        return postfix
    