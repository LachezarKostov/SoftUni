N = int(input())


stack = []
while N > 0:

    token = input()

    if token == "2":
        if stack:
            try:
                stack.pop()
            except:
                continue

    elif token == "3":
        print(max(stack))
    elif token == "4":
        print(min(stack))
    else:
        token = token.split(" ")
        stack.append(int(token[1]))
    N = N - 1

fina_stack = []
for s in range(len(stack)):
    temp = str(stack.pop())
    fina_stack.append(temp)

print(", ".join(fina_stack))
