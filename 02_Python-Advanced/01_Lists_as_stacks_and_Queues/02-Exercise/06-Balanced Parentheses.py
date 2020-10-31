# Имаме стринг от скоби
# Ползваме стак, когато видим затваряща скоба
# проверяваме коя е последната отваряща

parentheses = input()
stack = []
valid = True

if parentheses:
    for i in parentheses:
        stack.append(i)

        if i == "]":

            if stack[-2] != "[":
                valid = False
            try:
                stack.pop()
                stack.pop()
            except:
                continue

        elif i == ")":
            if stack[-2] != "(":
                valid = False
            try:
                stack.pop()
                stack.pop()
            except:
                continue

        elif i == "}":
            if stack[-2] != "{":
                valid = False
            try:
                stack.pop()
                stack.pop()
            except:
                continue

if valid:
    print("YES")
else:
    print("NO")
