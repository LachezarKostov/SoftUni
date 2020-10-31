steps = 10000

while steps > 0 :
    text = input()
    if text != "Going home":
        num_steps = int(text)
        steps -= num_steps
    else:
        num_steps = int(input())
        steps -= num_steps
        break
if steps <= 0:
    print("""Goal reached! Good job!""")
else:
    print(f"{steps} more steps to reach goal.")
