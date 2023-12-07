import unittest

def eat_small_fish(fishes: list[int], min_size: int, max_size: int) -> int:
    return sum(1 for fish in fishes if min_size <= fish <= max_size)

class TestEngine1(unittest.TestCase):

    def test_1(self):
        result = eat_small_fish([1, 2, 3, 4, 5], 2, 3)
        print(result)  
        self.assertEqual(result, 2)

    def test_2(self):
        result = eat_small_fish([1, 1, 1, 2, 2], 2, 3)
        print(result)  
        self.assertEqual(result, 2)

    def test_3(self):
        result = eat_small_fish([1, 10], 2, 3)
        print(result)  
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
