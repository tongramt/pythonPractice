import unittest
import countMain


class MyTestCase(unittest.TestCase):
    def test_ints(self):
        countMain.inputHandling()
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
