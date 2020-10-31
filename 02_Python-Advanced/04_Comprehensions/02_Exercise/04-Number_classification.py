numbers = [int(x) for x in input().split(", ")]

positive = [str(num) for num in numbers if num >= 0]
negative = [str(num) for num in numbers if num < 0]
even = [str(num) for num in numbers if num % 2 == 0]
odd = [str(num) for num in numbers if num % 2 != 0]

print(f"""
Positive: {", ".join(positive)}
Negative: {", ".join(negative)}
Even: {", ".join(even)}
Odd: {", ".join(odd)}
""")