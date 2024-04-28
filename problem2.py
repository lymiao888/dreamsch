def check_brackets(str):
    '''
    Args:
        str: 输入的字符串，包含括号和其他字符
    Returns:
        result_str: 修改后的字符串，将括号中的内容标记为空格，未匹配的左括号标记为问号，未匹配的右括号标记为字母"x"
    '''
    pass

    stack = []
    result = []
    result_str = ''

    for i, char in enumerate(str):
        if char == '(':
            stack.append(i)
            result.append(' ')
        elif char == ')':
            if stack:
                stack.pop()
                result.append(' ')
            else:
                result.append('?')
        else:
            result.append(' ')
    
    while stack:
        result[stack.pop()] = 'x'
    
    result_str.join(result)
    return result_str

# test
test_cases = [
    "bge)))))))))",
    "((IIII)))))",
    "()()()()(uuu",
    "))))UUUU((()"
]

for test in test_cases:
    print(test)
    print(check_brackets(test))
