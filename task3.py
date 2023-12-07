import re
import unittest

def has_hiddden_shrug(line: str) -> bool:
    shrug_pattern = r'¯\\_\(ツ\)\\_/¯'
    return bool(re.search(shrug_pattern, line))

class TestEngine3(unittest.TestCase):

    def test_1(self):
        self.assertEqual(has_hiddden_shrug("¯\\_(ツ)_/¯"), True)

    def test_2(self):
        self.assertEqual(has_hiddden_shrug("¯\\_##(ツ)_/¯"), True)

    def test_3(self):
        self.assertEqual(has_hiddden_shrug("¯\\_(ツ)##_¯"), True)

    def test_4(self):
        self.assertEqual(has_hiddden_shrug("¯\\_##(ツ)##_/¯"), False)

    def test_5(self):
        # Dodatkowe napisy przed shrugiem nie są dozwolone
        self.assertEqual(has_hiddden_shrug("##¯\\_##(ツ)_/¯"), False)

    def test_6(self):
        # Shrugi z krótkimi rękoma nie są dozwolone
        self.assertEqual(has_hiddden_shrug("¯\(ツ)/¯"), False)

if __name__ == '__main__':
    unittest.main()
