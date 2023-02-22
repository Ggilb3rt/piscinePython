import datetime
from recipe import Recipe


class Book():
    """A cookbook"""
    creation_date = datetime.datetime.now()
    last_update = datetime.datetime.now()
    __recipes_list = {
        "starter": [],
        "lunch": [],
        "dessert": [],
    }

    def __init__(self, name: str):
        if not isinstance(name, str):
            raise TypeError('The name of a cookbook must be a string.')
        self.name = name

    def get_recipe_by_name(self, name: str) -> Recipe:
        """Prints a recipe with the name \
        {name} and returns the instance"""
        if not isinstance(name, str):
            raise TypeError("Recipe name must be a string")
        for recipes in self.__recipes_list.values():
            for recipe in recipes:
                if name in recipe.name:
                    print(str(recipe))
                    return recipe
        raise ValueError(f'{name} not in {self.name}')

    def get_recipes_by_types(self, recipe_type: str) -> list:
        """Get all recipe names for a given recipe_type """
        if not isinstance(recipe_type, str):
            raise TypeError("Recipe type must be a string")
        if recipe_type not in self.__recipes_list:
            raise ValueError(f"Recipe types : {self.__recipes_list.keys()}")
        names_list = [recipe.name for recipe in self.__recipes_list[recipe_type] if len(self.__recipes_list[recipe_type])]
        return names_list
        # print(f'{recipe_type}')
        # for recipes in self.__recipes_list[recipe_type]:
        #     if not len(self.__recipes_list[recipe_type]):
        #         print("\tempty")
        #     else:
        #         print(f'\t{recipes.name}')

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if not isinstance(recipe, Recipe):
            raise TypeError("add_recipe must be Recipe instance")
        if recipe.recipe_type not in self.__recipes_list:
            raise ValueError("how can you do that you strange wizard ?")
        self.__recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.datetime.now()
        print(f'{recipe.name} added to the cookbook {self.name}')

    def __str__(self):
        return f'"{self.name}" created at {self.creation_date}, last update {self.last_update}'