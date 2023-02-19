import sys
import string


def check_args(arg1="", arg2=""):
    if not isinstance(arg1, str):
        raise TypeError('First arg must be a string')
    try:
        int(arg2)
    except KeyError:
        raise TypeError('Second arg must be an integer')


def remove_punctuation(str=""):
    exclude = set(string.punctuation)
    return ''.join(char for char in str if char not in exclude)


def filter_words(words="", min_len=0):
    words = remove_punctuation(words)
    splitted = words.split(' ')
    return [word for word in splitted if len(word) > min_len]


def main():
    if len(sys.argv) != 3:
        print("ERROR")
        sys.exit(0)
    try:
        check_args(sys.argv[1], sys.argv[2])
        words = sys.argv[1]
        min_len = int(sys.argv[2])
        words = filter_words(words, min_len)
        print(words)
    except TypeError as e:
        print(str(e))
        sys.exit(0)


if __name__ == "__main__":
    main()
