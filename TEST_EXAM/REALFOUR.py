group_count = int(input())
musala = 0
monblan = 0
kilimandjaro = 0
k2 = 0
everest = 0
total_people = 0
for i in range(1, group_count+1):
    people_in_a_group = int(input())
    total_people += people_in_a_group

    if people_in_a_group <= 5:
        musala += people_in_a_group

    elif people_in_a_group <= 12:
        monblan += people_in_a_group

    elif people_in_a_group <= 25:
        kilimandjaro += people_in_a_group

    elif people_in_a_group <= 40:
        k2 += people_in_a_group

    else:
        everest += people_in_a_group
print(f"""{(musala/total_people*100):.2f}%
{(monblan/total_people*100):.2f}%
{(kilimandjaro/total_people*100):.2f}%
{(k2/total_people*100):.2f}%
{(everest/total_people*100):.2f}%""")
