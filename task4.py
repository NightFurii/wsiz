import unittest

def find_greatest_number(line: str) -> int:
    digits = [int(char) for char in line if char.isdigit()]
    
    if not digits:
        return 0
    

    digits.sort(reverse=True)
    
   
    result = int(''.join(map(str, digits)))
    
    return result

class TestEngine4(unittest.TestCase):

    def test_1(self):
        result = find_greatest_number("abc123abc")
        print(result)
        self.assertEqual(result, 321)

    def test_2(self):
        result = find_greatest_number("aeqf9adasde9awdadae0adaed9")
        print(result)
        self.assertEqual(result, 9990)

    def test_3(self):
        result = find_greatest_number("12345678")
        print(result)
        self.assertEqual(result, 87654321)

    def test_4(self):
        result = find_greatest_number("2233x")
        print(result)
        self.assertEqual(result, 3322)

if __name__ == '__main__':
    unittest.main()
