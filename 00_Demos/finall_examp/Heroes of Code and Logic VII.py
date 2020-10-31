count = int(input())
party = {}

for i in range(count):
    hero_hp_mp = input().split()
    hero = hero_hp_mp[0]
    hp = int(hero_hp_mp[1])
    mp = int(hero_hp_mp[2])
    party[hero] = [hp, mp]

command = input().split(" - ")

while command[0] != "End":
    hero = command[1]

    if command[0] == "CastSpell":
        mp_needed = int(command[2])
        spell_name = command[3]

        if int(party[hero][1]) >= mp_needed:
            print(f"{hero} has successfully cast {spell_name} and now has {int(party[hero][1]) - mp_needed} MP!")
            party[hero][1] -= mp_needed
        else:
            print(f"{hero} does not have enough MP to cast {spell_name}!")

    elif command[0] == "TakeDamage":
        dmg = int(command[2])
        attacker = command[3]
        hp = int(party[hero][0])
        hp -= dmg
        party[hero][0] = hp

        if hp <= 0:
            print(f"{hero} has been killed by {attacker}!")
            party.pop(hero)
        else:
            print(f"{hero} was hit for {dmg} HP by {attacker} and now has {hp} HP left!")

    elif command[0] == "Recharge":
        amount_of_mp = int(command[2])
        mp = int(party[hero][1])

        if mp + amount_of_mp > 200:
            amount_of_mp = 200 - mp
            party[hero][1] = 200
        else:
            party[hero][1] = mp + amount_of_mp
        print(f"{hero} recharged for {amount_of_mp} MP!")

    elif command[0] == "Heal":
        amount_of_hp = int(command[2])
        hp = int(party[hero][0])

        if hp + amount_of_hp > 100:
            amount_of_hp = 100 - hp
            party[hero][0] = 100
        else:
            party[hero][0] = hp + amount_of_hp
        print(f"{hero} healed for {amount_of_hp} HP!")

    command = input().split(" - ")

party = dict(sorted(party.items(), key=lambda item: (-item[1][0], item[0][0])))

for hero in party:
    print(f"""{hero}
  HP: {party[hero][0]}
  MP: {party[hero][1]}""")