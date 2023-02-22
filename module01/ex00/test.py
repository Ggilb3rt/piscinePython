from book import Book
from recipe import Recipe
import time


try:
    grandma = Book("Grandma's secret")
    print(grandma.__doc__)
    print(str(grandma))
    
    print()
    time.sleep(0.2)

    toast = Recipe("Toast", 1, 2, ["bread", "butter"], "Good old classic toasted bread", "starter")
    print(toast.__doc__)
    print(toast)
    pizza = Recipe("Pizza", 2, 30, ["floor", "water", "many things"], "[racist italian accent]", "lunch")


    print("\nAdd recipe to book")
    grandma.add_recipe(toast)
    grandma.add_recipe(pizza)
    grandma.add_recipe(Recipe("French toast", 1, 5, ["bread", "milk", "eggs", "sugar"], "le pain perdu", "starter"))
    print(grandma)
    print(grandma.get_recipes_by_types("starter"))
    print(grandma.get_recipe_by_name("Toast"))
except TypeError as te:
    print(te)
except ValueError as ve:
    print(ve)

    grandma.get_recipe_by_name("POUET")