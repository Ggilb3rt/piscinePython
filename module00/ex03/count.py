import sys
import string


def text_analyzer(text: str = ""):
    """Print the sums of upper-case, lower-case,
    punctiation and space characters of a string
    """
    if type(text) != str:
        print("AssertionError: argument is not a string")
        return
    totalChar = len(text)
    while totalChar == 0:
        text = input("What is the text to analyze ?\n")
        totalChar = len(text)
    upperLetters = sum(1 for c in text if c.isupper())
    lowerLetters = sum(1 for c in text if c.islower())
    punctMark = sum(1 for c in text if c in string.punctuation)
    space = sum(1 for c in text if c.isspace())
    print("The text contains %d character(s):" % totalChar)
    print("- %d upper letter(s)" % upperLetters)
    print("- %d lower letter(s)" % lowerLetters)
    print("- %d punctuation mark(s)" % punctMark)
    print("- %d space(s)" % space)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error: need only one string argument")
        sys.exit(0)
    text_analyzer(sys.argv[1])
    sys.exit(1)
