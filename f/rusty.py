# rusty calculator
#
# solution by Zesheng Li
# rexeneo@gmail.com


def answer(str):
    output = ''
    stack = []
    rank = {'+': 2,
            '-': 2,
            '*': 3,
            '/': 3}

    for token in str:
        if token.isnumeric():   # if is a number, append to output
            output += token
        else:   # if not, comapre with what's in the stack
            while stack.__len__() != 0 and rank[token] < rank[stack[-1]]:
                # if token is inferior to the guy on top of stack, kick the guy out
                # normally token needs to be superior and kicking equal ranks as well,
                # but in order to get lexicographically largest result,
                # token needs to live with equally ranked dudes in the stack
                # thus delaying the equally ranked operations
                output += stack.pop()
            else:
                # token gets into stack only when he feels superior
                stack.append(token)

    # now str is exhausted, pop everything in stack to output
    while stack.__len__() > 0:
        output += stack.pop()

    return output
