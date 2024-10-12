def check_brackets(statement):
    stack = ArrayStack(100)
    for ch in statement:
        if ch in ('(','[','{'): # if ch in'{[(' : 처럼 짧게 표현 가능
            stack.push(ch)
        elif ch in (')','}',']'):
            if stack.isEmpty():
                return False
            else :
                left = stack.pop()
                if (ch== "}" and left != "{") or \
                   (ch == "]" and left != "[") or \
                   (ch == ")" and left != "(") :
                    return False
    return stack.isEmpty()




