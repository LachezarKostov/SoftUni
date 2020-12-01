import time
import unittest


def exec_time(func):
    def wrapper(*args):
        start_time = time.time()
        func(*args)
        end_time = time.time()
        return end_time - start_time
    return wrapper


# test first zero
class ExecTimeTests(unittest.TestCase):
    def test_zero_first(self):
        @exec_time
        def loop(start, end):
            total = 0
            for x in range(start, end):
                total += x
            return total
        self.assertEqual(round(loop(1, 10000000)), 1)

if __name__ == '__main__':
    unittest.main()
