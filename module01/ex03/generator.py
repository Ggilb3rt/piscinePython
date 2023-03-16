import random


def generator(text, sep=" ", option=None):
    """Splits the text according to sep value and yield the substrings.
        option precise if a action is performed to the substrings
        before it is yielded."""

    if (not isinstance(text, str) or
            not isinstance(sep, str)):
        print("ERROR")
        return
        # raise TypeError("All parameters must be strings")
    if (option is not None
            and option != 'shuffle'
            and option != 'unique'
            and option != 'ordered'):
        print("ERROR")
        return
        # raise ValueError("Options : 'shuffle' or 'unique' or 'ordered'")
    i = 0
    lst = text.split(sep)

    # create the list with good option
    if option == "ordered":
        lst.sort()
    if option == 'unique':
        # Sexy but unordered
        # lst = list(set(lst))
        find = set()
        result = []
        for word in lst:
            if word not in find:
                find.add(word)
                result.append(word)
        lst = result
        del find, result
        # C like
        # lst_u = []
        # for word in lst:
        #     find = 0
        #     for word_u in lst_u:
        #         if word_u == word:
        #             find = 1
        #             break
        #     if find == 0:
        #         lst_u.append(word)
        # lst = lst_u
        # del find, lst_u
    if option == 'shuffle':
        for i in reversed(range(0, len(lst))):
            j = int(random.random() * (i + 1))
            lst[i], lst[j] = lst[j], lst[i]

    while i < len(lst):
        yield lst[i]
        i += 1


if __name__ == "__main__":
    txt = "lol intenet lorem lol ipsum canard lol internet"
    print("No option :")
    for word in generator(txt):
        print(word)
    print("\nUnique :")
    for word in generator(txt, ' ', 'unique'):
        print(word)
    print("\nOrdered :")
    for word in generator(txt, ' ', 'ordered'):
        print(word)
    print("\nShuffled :")
    for word in generator(txt, ' ', 'shuffle'):
        print(word)
    print("\nBad :")
    for word in generator(txt, ' ', 'lol'):
        print(word)
    for word in generator(txt, 34):
        print(word)
    for word in generator(txt, ' ', 42):
        print(word)
    txt = 1.0
    for word in generator(txt, '.'):
        print(word)
