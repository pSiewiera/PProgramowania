import unittest
from Code import Add

class TestCase(unittest.TestCase):
    def test_AddEmptyString(self):
        self.assertEqual(Add(""), 0)
    def test_AddOne(self):
        self.assertEqual(Add("1"), 1)
    def test_AddTwo(self):
        self.assertEqual(Add("1,2"), 3)
    def test_AddHard(self):
        self.assertEqual(Add("1\n2,3"), 6)
    def test_AddError(self):
        self.assertEqual(Add("1,\n"), 1)

        
unittest.main(argv=['first-arg-is-ignored'], exit=False)
if __name__ == '__main__':
    unittest.main()