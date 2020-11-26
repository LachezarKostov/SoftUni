from typing import Any, Dict


class dictionary_iter():
    def __init__(self, data: Dict[Any, Any]):
        self.data = data
        self.__data = iter(self.data.items())

    def __iter__(self):
        self.__data = iter(self.data.items())
        return self

    def __next__(self):
        val = next(self.__data)
        return val


# test zero
import unittest


class DictionaryIteratorTests(unittest.TestCase):
    def test_zero(self):
        result = dictionary_iter({1: "1", 2: "2"})
        expected = []
        for x in result:
            expected.append(x)
        self.assertEqual(expected, [(1, "1"), (2, "2")])


if __name__ == '__main__':
    unittest.main()