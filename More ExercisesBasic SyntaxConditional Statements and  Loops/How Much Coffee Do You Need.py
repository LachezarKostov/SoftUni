intake = input()
check_list = ["CODING", "DOG", "CAT", "MOVIE"]
check_list2 = ["coding", "dog", "cat", "movie"]
count = 0

while intake != "END":

    if intake in check_list:
        count += 2
    elif intake in check_list2:
        count += 1

    intake = input()

if count >= 5:
    print("You need extra sleep")
else:
    print(count)