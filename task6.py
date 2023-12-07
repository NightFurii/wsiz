import unittest
from collections import Counter

def is_even_beautiful(number: int) -> bool:
    str_number = str(number)

    digit_counts = Counter(str_number)
    is_beautiful = all(count % 2 == 0 for count in digit_counts.values())

    if is_beautiful:
        beautiful_digits = [digit for digit, count in digit_counts.items() if count == 2]
        print(f'Liczby parzyście piękne w liczbie {number}: {beautiful_digits}')
    else:
        print(f'Brak liczb parzyście pięknych w liczbie {number}')

    return is_beautiful
class TestEngine6(unittest.TestCase):

    def test_1(self):
        self.assertEqual(is_even_beautiful(2233), True)

    def test_2(self):
        self.assertEqual(is_even_beautiful(11), True)

    def test_3(self):
        self.assertEqual(is_even_beautiful(1212), True)

    def test_4(self):
        self.assertEqual(is_even_beautiful(1221), True)

    def test_5(self):
        self.assertEqual(is_even_beautiful(121), False)

    def test_6(self):
        self.assertEqual(is_even_beautiful(33441156), False)

    def test_7(self):
        self.assertEqual(is_even_beautiful(2222), True)

if __name__ == '__main__':
    unittest.main()
