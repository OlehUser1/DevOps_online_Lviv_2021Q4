Main script solv_square_equation.py 



import math


def main():
    parameters = validate_param()
    a, b, c = parameters[0], parameters[1], parameters[2]
    square_print(a, b, c)


def validate_param():
    for i in range(0, 3):
        try:
            a = int(input("Enter a: "))
            b = int(input("Enter b: "))
            c = int(input("Enter c: "))
        except ValueError:
            print("Enter only numbers")
            continue
        else:
            break
    return a, b, c


def discriminant(a, b, c):
    D = b ** 2 - 4 * a * c
    print("Discriminant =", D)
    return D


def roots(D, a, b):
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        return print("Two roots: x1 = " + str(x1) + ", x2 = " + str(x2))
    elif D == 0:
        x = -b / (2 * a)
        return print("Only one root: x =", x)
    else:
        return print("No roots")


def solv_square(a, b, c):
    D = discriminant(a, b, c)
    return roots(D, a, b)


def square_print(a, b, c):
    print("Equation parameters: a = " + str(a) + ", b = " + str(b) + ", c = " + str(c))
    solv_square(a, b, c)


if __name__ == '__main__':
    main()


UnitTests


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

