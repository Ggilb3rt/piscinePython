class Recipe():
    """A recipe"""
    __recipe_type_lst = ("starter", "lunch", "dessert")

    def __init__(
        self,
        name,
        cooking_lvl,
        cooking_time,
        ingredients,
        description,
        recipe_type,
    ):
        self.__check_name(name)
        self.__check_cooking_lvl(cooking_lvl)
        self.__check_cooking_time(cooking_time)
        self.__check_ingredients(ingredients)
        self.__check_description(description)
        self.__check_recipe_type(recipe_type)
        self.name = name

    def __check_name(self, name):
        if type(name) != str:
            raise TypeError('Recipe name must be a string')
        if len(name) == 0:
            raise ValueError('Recipe name can\'t be empty')

    def __check_cooking_lvl(self, cooking_lvl):
        if type(cooking_lvl) != int:
            raise TypeError('Cooking level must be an integer [1-5]')
        if cooking_lvl < 1 or cooking_lvl > 5:
            raise ValueError('Cooking level must be between 1 and 5.')
        self.cooking_lvl = cooking_lvl

    def __check_cooking_time(self, cooking_time):
        if type(cooking_time) != int:
            raise TypeError('Cooking time must be positive integer')
        if cooking_time < 0:
            raise ValueError('Cooking time must be positive')
        self.cooking_time = cooking_time

    def __check_ingredients(self, ingredients):
        if type(ingredients) != list:
            raise TypeError('Ingredients must be a list of strings')
        if len(ingredients) == 0:
            raise ValueError('Ingredients list can\'t be empty')
        for el in ingredients:
            if not isinstance(el, str):
                raise TypeError('Each ingredients must be a string')
        self.ingredients = ingredients

    def __check_description(self, description):
        if not isinstance(description, str):
            raise TypeError('Recipe description must be a string')
        self.description = description

    def __check_recipe_type(self, recipe_type):
        if not isinstance(recipe_type, str):
            raise TypeError('Recipe type must be a string')
        if recipe_type not in self.__recipe_type_lst:
            raise ValueError(
                f'Available recipe types : {self.__recipe_type_lst}'
            )
        self.recipe_type = recipe_type

    # def __del__(self):
    #     print("I can't be a Recipe in this world")

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = f'{self.name}: {self.description}'
        return txt
