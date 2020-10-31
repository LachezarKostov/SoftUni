n1 = int(input())
n2 = int(input())
op = str(input())
num = 0
add = ""

if op == "+":
    num = n1+n2
elif op == "-":
    num = n1 - n2
elif op == "*":
    num = n1 * n2

if num % 2 == 0:
    add = "even"
elif num % 2 != 0:
    add = "odd"

if op == "-" or op == "+" or op == "*":
    print(f"{n1} {op} {n2} = {num} - {add}")

if op == "/" and n2!=0 :
    num = n1 / n2
    print(f"{n1} {op} {n2} = {num:.2f}")

elif op == "%" and n2 != 0:
    num = n1 % n2
    print(f"{n1} {op} {n2} = {num}")

elif n2 == 0:
    print(f"Cannot divide {n1} by zero")
