import random #forbiden

def generator(text, sep=" ", option=None):
    """Splits the text according to sep value and yield the substrings.
        option precise if a action is performed to the substrings before it is yielded."""

    if (not isinstance(text, str) or\
            not isinstance(sep, str)):
        print("ERROR")
        return
        # raise TypeError("All parameters must be strings")
    if option != None and option != 'shuffle' and option != 'unique' and option != 'ordered':
        print("ERROR")
        return
        # raise ValueError("Options : 'shuffle' or 'unique' or 'ordered'")
    i = 0
    lst = text.split(sep)
    substring = ""

    # create the list with good option
    if option == "ordered":
        lst.sort()
    if option == 'unique':
        lst_u = []
        for word in lst:
            find = 0
            for word_u in lst_u:
                if word_u == word:
                    find = 1
                    break
            if find == 0:
                lst_u.append(word)
        lst = lst_u
        del find, lst_u
    if option == 'shuffle':
        random.shuffle(lst) #forbiden

    # create the substring
    while  i < len(lst):
        substring = lst[i]
        i += 1
        yield substring

if __name__ == "__main__":
    txt = "lol intenet lorem lol ipsum canard lol internet"
    for word in generator(txt, ' ', 'unique'):
        print(word)