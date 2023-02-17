import sys


def reverse(string):
    if type(string) != str:
        return
    string = string[::-1].swapcase()
    print(string)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        reverse(' '.join(sys.argv[1::]))
