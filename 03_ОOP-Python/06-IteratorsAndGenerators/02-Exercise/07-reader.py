def read_next(*iterables):
    for iterable in iterables:
        for el in iterable:
            yield el
        