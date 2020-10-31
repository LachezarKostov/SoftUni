import math

income = float(input())
grade = float(input())
minimal_wage = float(input())

Socialscholarship = 0.35*minimal_wage
Socialscholarship = math.floor(Socialscholarship)
results = grade * 25
results = math.floor(results)

if (grade < 4.5) or \
        ((income > minimal_wage) & (grade < 5.5)):

    print("You cannot get a scholarship!")

elif ((grade < 5.5) & (income < minimal_wage)) or \
        ((grade >= 5.5) & (Socialscholarship > results) & (income <= minimal_wage)):

    print(f"You get a Social scholarship {Socialscholarship:.0f} BGN")

#elif ((grade >= 5.5) & (income >= minimal_wage)) or \
     #   ((grade >= 5.5) & (Socialscholarship <= results) & (income <= minimal_wage)):
else:
    print(f"You get a scholarship for excellent results {results:.0f} BGN")
