from project.pokemon import Pokemon
from typing import List


class Trainer:
    name: str
    pokemon: List[Pokemon]

    def __init__(self, name: str):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon: list) -> str:
        pokemon_names = [p.name for p in self.pokemon]
        if pokemon.name in pokemon_names:
            return "This pokemon is already caught"
        self.pokemon.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str) -> str:
        pokemon_names = [p.name for p in self.pokemon]
        if pokemon_name in pokemon_names:
            del self.pokemon[pokemon_names.index(pokemon_name)]
            return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        data_to_return = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemon)}\n"
        pokemon_info = "\n".join([f'- {p.pokemon_details()}' for p in self.pokemon])

        return data_to_return + pokemon_info + "\n"






