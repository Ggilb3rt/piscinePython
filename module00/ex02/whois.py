import sys


def comp(nb: int):
    if nb % 2:
        print("I'm Odd.")
    else:
        print("I'm Even.")


if __name__ == "__main__":
    argc = len(sys.argv)
    if argc == 1:
        print("Usage: python whois.py integer")
    elif argc > 2:
        print("AssertionError: more than one argument are provided")
    else:
        try:
            comp(int(sys.argv[1]))
        except ValueError:
            print("AssertionError: argument is not an integer")
