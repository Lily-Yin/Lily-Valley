import unittest
from teste import Player  # ou qualquer classe que você queira testar

class TestDummy(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(1 + 1, 2)

if __name__ == "__main__":
    unittest.main()
