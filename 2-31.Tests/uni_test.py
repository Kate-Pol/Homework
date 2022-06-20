import unittest
import convert as c

class TestConvert(unittest.TestCase):

    def test_temp(self):
        self.assertEqual(c.converter('30C'), (86, 'F', '86F'))

    def test_temp2(self):
        self.assertEqual(c.converter('75F'), (24, 'C', '24C'))

    def test_measure_typo(self):
        with self.assertRaises(ValueError):
            c.converter('30j')


if __name__ == '__main__':
    unittest.main()
