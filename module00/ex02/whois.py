import sys


def comp(nb: int):
    try:
        nb = int(nb)
    except ValueError:
        print("AssertionError: argument is not an integer")
        return
    if nb == 0:
        print("I'm Zero.")
    elif nb % 2:
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
        comp(sys.argv[1])
