import unittest
import solv_square_equation


class test_solv_square(unittest.TestCase):
    def discriminant_gt_1(self):
        self.assertEqual(solv_square_equation.discriminant(1, 26, 120), 196)

    def discriminant_eq_1(self):
        self.assertEqual(solv_square_equation.discriminant(2, 4, 2), 16)

    def discriminant_lt_1(self):
        self.assertEqual(solv_square_equation.discriminant(5, 6, 7), -104)

    def roots_discriminant_gt_1(self):
        self.assertEqual(solv_square_equation.roots(196, 1, 26), -6.0, -20.0)

    def roots_discriminant_eq_1(self):
        self.assertEqual(solv_square_equation.roots(16, 2, 4), -1.0)

    def roots_discriminant_lt_1(self):
        self.assertEqual(solv_square_equation.roots(-104, 5, 6), False)

if __name__ == '__main__':
    unittest.main()
