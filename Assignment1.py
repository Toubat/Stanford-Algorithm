
def karatsuba(x, y, num_digits):
    # base case

    if num_digits == 1:
        return x * y

    exp = 10 ** (num_digits // 2)
    a, c = x // exp, y // exp
    b, d = x % exp, y % exp
    ac = karatsuba(a, c, num_digits // 2)
    bd = karatsuba(b, d, num_digits // 2)
    sum = karatsuba(a + b, c + d, (num_digits // 2)) - ac - bd

    return ac * (10 ** num_digits) + exp * sum + bd


def main():
    a = 3141592653589793238462643383279502884197169399375105820974944592
    b = 2718281828459045235360287471352662497757247093699959574966967627
    print(karatsuba(a, b, 64))

    return 0


main()