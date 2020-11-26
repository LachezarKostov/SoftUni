from itertools import permutations


def possible_permutations(sequence):
    for perm in permutations(sequence):
        yield list(perm)
