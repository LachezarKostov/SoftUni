age = int(input())
msg = "drink "

if age <= 14:
    msg += "toddy"
elif age <= 18:
    msg += "coke"
elif age <= 21:
    msg += "beer"
else:
    msg += "whisky"

print(msg)

