from book import Book
from recipe import Recipe


try :
    grandma = Book("Grandma")
    lol = Recipe("lol", 2, 0, ["flop"], "I'm not a real recipe", "starter")
except TypeError as te:
    print(te)
except ValueError as ve:
    print(ve)