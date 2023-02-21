import time
from recipe import Recipe

class Book():
    creation_date = time()
    last_update = time()
    __recipes_list = {
        "starter": [],
        "lunch": [],
        "dessert": [],
    }

    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError('The name of a cookbook must be a string.')
        self.name = name

    def get_recipe_by_name(self, name):
        """Prints a recipe with the name \
        texttt{name} and returns the instance"""
        if not isinstance(name, str):
            raise TypeError("Recipe name must be a string")
        for recipe in self.__recipes_list.values():
            if name in recipe:
                print(str(recipe[name]))
                return recipe[name]
    
    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        if not isinstance(recipe_type, str):
            raise TypeError("Recipe type must be a string")
        if recipe_type not in self.__recipes_list:
            raise ValueError(f"Recipe type can be {self.__recipes_list.keys()}")

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if not isinstance(recipe, Recipe):
            raise TypeError("add_recipe must be Recipe instance")
        if recipe.recipe_type not in self.__recipes_list:
            raise ValueError("how can you do that you strange wizard ?")
        self.__recipes_list[recipe.recipe_type].append(recipe)
        last_update = time()
        print(f'{recipe.name} added to the cookbook {self.name}')
