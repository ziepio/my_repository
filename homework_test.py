import unittest
from homework import Homework

class HomeworkTestCase(unittest.TestCase):
    def test_prime_num(self):
        prim = Homework()

        self.assertEqual(prim.prime_num(13), 'Tak')
        self.assertEqual(prim.prime_num(6), 'Nie')

    def test_val_pesel(self):
        pes = Homework()

        self.assertEqual(pes.val_pesel(44051401458), 'D')
        self.assertEqual(pes.val_pesel(12345678912), 'N')


if __name__ == '__main__':
    unittest.main()
