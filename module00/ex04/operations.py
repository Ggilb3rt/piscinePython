import sys
import math


def operations(nb1: int = 0, nb2: int = 0):
    if type(nb1) != int or type(nb2) != int:
        print("AssertionError: only integers")
        return
    tab = 15
    print(
        f'{"Sum:":{tab}}{nb1 + nb2}\n'
        f'{"Differences:":{tab}}{nb1 - nb2}\n'
        f'{"Product:":{tab}}{nb1 * nb2}'
    )
# '{0:15}{1}\n'.format('Product:', nb1 * nb2)
# '{string:15}{product}\n'.format(string='Product:', product=nb1 * nb2)
    if nb2 == 0:
        print(f'{"Quotient:":{tab}}ERROR (division by zero)')
        print(f'{"Remainder:":{tab}}ERROR (modulo by zero)')
    else:
        quotient = nb1 / nb2
        print(f'{"Quotient:":{tab}}{round(quotient, 4)}'
              f'{"..." if not (math.isclose(quotient, round(quotient, 4))) else ""}')
        print(f'{"Remainder:":{tab}}{nb1 % nb2}')


def str_to_int(s: str) -> int:
    try:
        return int(s)
    except ValueError:
        print("Error: %s is not an integer" % s)
        sys.exit(0)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(
            "Usage: python operation.py <number1> <number2>\n"
            "Exemple:\n"
            "\tpython operation.py 10 3"
        )
        sys.exit(0)
    elif len(sys.argv) != 3:
        print("AssertionError: need 3 arguments")
        sys.exit(0)
    operations(str_to_int(sys.argv[1]), str_to_int(sys.argv[2]))
