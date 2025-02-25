import unittest
from agentic_tools.example import add


class TestExample(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)


if __name__ == "__main__":
    unittest.main()
