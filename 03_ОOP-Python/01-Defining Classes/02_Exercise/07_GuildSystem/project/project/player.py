class Player:
    name: str
    hp: int
    mp: int
    skills = dict

    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name: str, mana_cost: int) -> str:

        if skill_name in [s for s in self.skills]:
            return "Skill already added"
        self.skills.update({skill_name: mana_cost})
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        skill_set = []
        for key, value in self.skills.items():
            skill_set.append(f"==={key} – {value}")
        return "\n".join([
            f"Name: {self.name}",
            f"Guild: {self.guild}",
            f"HP: {self.hp}",
            f"MP: {self.mp}", ] + skill_set) + "\n"
