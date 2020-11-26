def is_prime(num):
    for n in range(2, num):
        if num % n == 0:
            return False
    return num not in (0, 1)


def get_primes(sequence):
    yield [x for x in sequence if is_prime(x)]

# test zero
import unittest

class Tests(unittest.TestCase):
    def test_zero(self):
        res = list(get_primes([2, 4, 3, 5, 6, 9, 1, 0]))
        self.assertEqual(res, [2, 3, 5])

if __name__ == '__main__':
    unittest.main()
