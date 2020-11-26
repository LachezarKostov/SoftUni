def numbers():
    i = 1
    while True:
        yield i
        i += 1


def take(count_to_take, sequence):
    return [x for _, x in zip(range(count_to_take), sequence)]


def halves():
    for x in numbers():
        yield x / 2


def solution():
    return take, halves, numbers


def main():
    def test_numbers():
        print(list(x for x, _ in zip(numbers(), range(4))))

    test_numbers()

    def test_halves():
        print(list(x for x, _ in zip(halves(), range(4))))

    test_halves()

    def test_numbers():
        print(list(take(5, iter(range(6)))))

    test_numbers()


if __name__ == "__main__":
    main()
