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
        base = Book("42.0")
        self.assertEqual(base.name, "42.0")
        self.assertEqual(base.creation_date.second, base.last_update.second)

    def test_Book_add_recipe(self):
        toast = Recipe("Toast1", 1, 2, ["bread", "butter"],
                       "Good old classic toasted bread", "starter")
        book = Book("42.1")
        bookNoUpdateDate = book.last_update
        with self.assertRaises(TypeError):
            book.add_recipe("string")
        toast.recipe_type = 'nope'
        with self.assertRaises(ValueError):
            book.add_recipe(toast)
        toast.recipe_type = 'starter'
        book.add_recipe(toast)
        self.assertEqual(book._Book__recipes_list["starter"][0],
                         book.get_recipe_by_name('Toast'))
        self.assertEqual(book._Book__recipes_list["starter"][0], toast)
        self.assertEqual(book.get_recipe_by_name('Toast1'), toast)
        self.assertGreater(book.last_update, bookNoUpdateDate)

    def test_Book_get_recipe_by_name(self):
        pizza = Recipe("pizza", 2, 30, ["floor", "water", "many things"],
                       "[racist italian accent]", "lunch")
        toast = Recipe("Toast", 1, 2, ["bread", "butter"],
                       "Good old classic toasted bread", "starter")
        book = Book("42.2")
        with self.assertRaises(TypeError):
            book.get_recipe_by_name(123)
        with self.assertRaises(ValueError):
            book.get_recipe_by_name("123")
        book.add_recipe(pizza)
        book.add_recipe(pizza)
        book.add_recipe(pizza)
        book.add_recipe(toast)
        self.assertEqual(book.get_recipe_by_name('pizza'), pizza)
        self.assertEqual(book.get_recipe_by_name('Toast'), toast)
        self.assertEqual(book._Book__recipes_list["lunch"][1],
                         book.get_recipe_by_name('pizza'))
        self.assertEqual(book._Book__recipes_list["lunch"][2], pizza)
        self.assertEqual(len(book._Book__recipes_list["starter"]), 1)
        self.assertEqual(len(book._Book__recipes_list["lunch"]), 3)
        self.assertEqual(len(book._Book__recipes_list["dessert"]), 0)

    def test_Book_get_recipe_by_type(self):
        pizza = Recipe("pizza", 2, 30, ["floor", "water", "many things"],
                       "[racist italian accent]", "lunch")
        toast = Recipe("Toast", 1, 2, ["bread", "butter"],
                       "Good old classic toasted bread", "starter")
        french = Recipe("French toast", 1, 5,
                        ["bread", "milk", "eggs", "sugar"],
                        "le pain perdu", "starter")
        fruit = Recipe("Apple", 1, 0, ["apple"], "it's a fruit", "dessert")
        book = Book("42.3")
        book.add_recipe(french)
        book.add_recipe(pizza)
        book.add_recipe(toast)
        book.add_recipe(fruit)
        with self.assertRaises(TypeError):
            book.get_recipes_by_types(123)
        with self.assertRaises(ValueError):
            book.get_recipes_by_types("123")
        self.assertEqual(len(book.get_recipes_by_types("starter")), 2)
        self.assertEqual(len(book.get_recipes_by_types("lunch")), 1)
        self.assertEqual(len(book.get_recipes_by_types("dessert")), 1)
        self.assertEqual(book.get_recipes_by_types("starter"),
                         ['French toast', 'Toast'])
        self.assertEqual(book.get_recipes_by_types("lunch"), ['pizza'])
        self.assertEqual(book.get_recipes_by_types("dessert"), ['Apple'])
        self.assertEqual(book.get_recipes_by_types("starter"),
                         ['French toast', 'Toast'])


if __name__ == '__main__':
    unittest.main()
