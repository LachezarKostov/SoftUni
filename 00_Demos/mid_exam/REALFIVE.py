FOOOOOOD = int(input())
food_par_day = input()
FOOOOOOD = FOOOOOOD*1000

while food_par_day != "Adopted":
    food_par_day = int(food_par_day)
    FOOOOOOD = FOOOOOOD - food_par_day
    food_par_day = input()
if FOOOOOOD >= 0:
    print(f"Food is enough! Leftovers: {FOOOOOOD} grams." )
else:
    print(f"Food is not enough. You need {abs(FOOOOOOD)} grams more." )
