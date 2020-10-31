book_name = input()
num_of_books = int(input())
count = 0
is_book_found = False

while num_of_books > count:
    random_book = input()

    if random_book == book_name:
        is_book_found = True
        print(f"You checked {count} books and found it. ")
        break
    count += 1

    if count == num_of_books:
        print(f"The book you search is not here!\n You checked {count} books.")
        break
