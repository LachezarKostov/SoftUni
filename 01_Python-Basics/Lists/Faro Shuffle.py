cards = input().split()
shuffles_count = int(input())

middle_len = len(cards)//2

for _ in range(shuffles_count):

    res = []
    for index in range(middle_len):
        first_card = cards[index]
        second_card = cards[index + middle_len]

        res.append(first_card)
        res.append(second_card)
    cards = res
print(res)

