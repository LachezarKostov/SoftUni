thing = str(input())

list_a = ["banana", "apple", "kiwi", "cherry", "lemon", "grapes"]
list_b = ["tomato", "cucumber", "pepper", "carrot"]

if thing in list_a :
    print("fruit")
elif thing in list_b:
    print("vegetable")

else:
    print("unknown")
