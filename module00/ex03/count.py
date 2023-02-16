import sys


def text_analyzer(text: str):
    totalChar = len(text)
    upperLetters = sum(1 for c in text if c.isupper())
    lowerLetters = sum(1 for c in text if c.islower())
    punctMark = 0
    space = sum(1 for c in text if c.isspace())
    print("The text contains %d character(s):" % totalChar)
    print("- %d upper letter(s)" % upperLetters)
    print("- %d lower letter(s)" % lowerLetters)
    print("- %d punctuation mark(s)" % punctMark)
    print("- %d space(s)" % space)


if __name__ == "__main__":
    if len(sys.argv) != 2 :
        print("Error: only one string argument")
        sys.exit(0)
    text_analyzer(sys.argv[1])
    sys.exit(1)