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
