from book import Book
from recipe import Recipe
import unittest
import time


class TestRecipe(unittest.TestCase):
    def test_Recipe_init_name(self):
        with self.assertRaises(TypeError):
            Recipe(34, 1, 2, ['butter'], '', 'starter')
        with self.assertRaises(ValueError):
            Recipe("", 1, 2, ['butter'], '', 'starter')
        base = Recipe("base", 1, 2, ['butter'], '', 'starter')
        self.assertEqual(base.name, "base")

    def test_Recipe_init_cooking_lvl(self):
        with self.assertRaises(TypeError):
            Recipe("Recipe1", '10', 2, ['butter'], '', 'starter')
        with self.assertRaises(ValueError):
            Recipe("Recipe1", 6, 2, ['butter'], '', 'starter')
        with self.assertRaises(ValueError):
            Recipe("Recipe1", 0, 2, ['butter'], '', 'starter')
        base = Recipe("base", 1, 2, ['butter'], '', 'starter')
        self.assertEqual(base.cooking_lvl, 1)

    def test_Recipe_init_cooking_time(self):
        with self.assertRaises(TypeError):
            Recipe("Recipe1", 1, '2', ['butter'], '', 'starter')
        with self.assertRaises(ValueError):
            Recipe("Recipe1", 6, -1, ['butter'], '', 'starter')
        base = Recipe("base", 1, 2, ['butter'], '', 'starter')
        self.assertEqual(base.cooking_time, 2)

    def test_Recipe_init_ingredients(self):
        with self.assertRaises(TypeError):
            Recipe("Recipe1", 1, 2, (), '', 'starter')
        with self.assertRaises(ValueError):
            Recipe("Recipe1", 5, 2, [], '', 'starter')
        with self.assertRaises(TypeError):
            Recipe("Recipe1", 5, 2, [42], '', 'starter')
        with self.assertRaises(TypeError):
            Recipe("Recipe1", 5, 2, ["butter", 42], '', 'starter')
        base = Recipe("base", 1, 2, ['butter', "bread"], '', 'starter')
        self.assertEqual(base.ingredients, ['butter', "bread"])
        self.assertEqual(base.ingredients[1], "bread")

    def test_Recipe_init_description(self):
        with self.assertRaises(TypeError):
            Recipe("base", 1, 2, ['butter', "bread"], 23, 'starter')
        base = Recipe("base", 1, 2, ['butter', "bread"], '', 'starter')
        self.assertEqual(base.description, "")
        base.description = "not empty"
        self.assertEqual(base.description, "not empty")

    def test_Recipe_init_type(self):
        with self.assertRaises(TypeError):
            Recipe("base", 1, 2, ['butter', "bread"], '', [])
        with self.assertRaises(ValueError):
            Recipe("base", 1, 2, ['butter', "bread"], '', '')
        with self.assertRaises(ValueError):
            Recipe("base", 1, 2, ['butter', "bread"], '', 'pouet')
        base = Recipe("base", 1, 2, ['butter', "bread"], '', 'starter')
        self.assertEqual(base.recipe_type, "starter")
        base.recipe_type = 'lunch'
        self.assertEqual(base.recipe_type, "lunch")
        base.recipe_type = 'dessert'
        self.assertEqual(base.recipe_type, "dessert")
        # with self.assertRaises(ValueError):
        #     base.recipe_type = 'nope'


class TestBook(unittest.TestCase):
    def test_Book_init_name(self):
        with self.assertRaises(TypeError):
            Book(42)
        base = Book("42")
        self.assertEqual(base.name, "42")
        self.assertEqual(base.creation_date.second, base.last_update.second)

    def test_Book_add_recipe(self):
        toast = Recipe("Toast", 1, 2, ["bread", "butter"], "Good old classic toasted bread", "starter")
        book = Book("42")
        bookNoUpdateDate = book.last_update
        with self.assertRaises(TypeError):
            book.add_recipe("string")
        toast.recipe_type = 'nope'
        with self.assertRaises(ValueError):
            book.add_recipe(toast)
        toast.recipe_type = 'starter'
        book.add_recipe(toast)
        self.assertEqual(book._Book__recipes_list["starter"][0], toast)
        self.assertEqual(book.get_recipe_by_name('Toast'), toast)
        self.assertGreater(book.last_update, bookNoUpdateDate)

    def test_Book_get_recipe_by_name(self):
        toast = Recipe("Toast", 1, 2, ["bread", "butter"], "Good old classic toasted bread", "starter")
        # toast2 = Recipe("Toast2", 1, 2, ["bread", "butter"], "Good old classic toasted bread", "starter")
        book = Book("42.2")
        book.add_recipe(toast)
        # book.add_recipe(toast2)
        with self.assertRaises(TypeError):
            book.get_recipe_by_name(123)
        with self.assertRaises(ValueError):
            book.get_recipe_by_name("123")
        self.assertEqual(book._Book__recipes_list["starter"][0], toast)
        self.assertEqual(book.get_recipe_by_name("Toast"), toast)



if __name__ == '__main__':
    unittest.main()


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
