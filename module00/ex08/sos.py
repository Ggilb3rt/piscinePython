import sys
import string


def has_special_char(msg: str = ""):
    for c in msg:
        if c in string.punctuation:
            return True
    return False


def morse_convert(msg: str = "") -> str:
    """Convert alphanumeric characters to morse code.
        Supported characters : [0-9] [a-Z] and space ' '
    """
    morse_alphabet = {
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        " ": "/",
    }
    if not isinstance(msg, str):
        return "ERROR"
    if has_special_char(msg):
        return "ERROR"
    msg = msg.upper()
    msg = ' '.join(morse_alphabet[c] for c in msg if c in morse_alphabet)
    return msg


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(
            f'{morse_convert.__doc__}'
            f'\nUsage : python sos.py <string> (<string>)*'
        )
        sys.exit(0)
    msg = ' '.join(sys.argv[1::])
    print(morse_convert(msg))
    sys.exit(0)
