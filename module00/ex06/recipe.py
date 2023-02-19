from colorama import Fore, Style
import os

meal_type = ["dessert", "lunch", "breakfast"]

cookbook = {
    "Sandwich": {
        "ingredients": ["ham", "bread", "cheese", "tomatoes"],
        "meal": meal_type[1],
        "prep_time": 10
    },
    "Cake": {
        "ingredients": ["flour", "sugar", "eggs"],
        "meal": meal_type[0],
        "prep_time": 60
    },
    "Salad": {
        "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
        "meal": meal_type[1],
        "prep_time": 15
    },
}


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def add_recipe():
    user_input = ""
    wrong_input = 0
    name = ""
    recipe = {
        'ingredients': [],
        'meal': '',
        'prep_time': 0,
    }

    while len(name) == 0 or name in cookbook:
        if wrong_input > 4 and len(name) == 0:
            print(f'{Fore.YELLOW}Name can\'t be empty{Style.RESET_ALL}')
            wrong_input = 0
        wrong_input += 1
        name = input("Enter a name:\n")
        if name in cookbook:
            print(f'"{name}" already exist.')
    user_input = input("Enter ingredients:\n")
    while len(user_input) != 0:
        recipe['ingredients'].append(user_input)
        user_input = input("")
    user_input = ""
    wrong_input = 0
    while recipe['meal'] not in meal_type:
        if wrong_input > 4:
            print(
                f'{Fore.YELLOW}Available meal types are :'
                f'{Style.RESET_ALL} {meal_type}'
            )
        wrong_input += 1
        recipe['meal'] = input("Enter a meal type:\n")
    wrong_input = 0
    while recipe['prep_time'] <= 0:
        if wrong_input > 4:
            print(
                f'{Fore.YELLOW}'
                f'Preparation time must be in minutes{Style.RESET_ALL}'
            )
        wrong_input += 1
        user_input = input("Enter a preparation time:\n")
        if user_input.isdigit():
            recipe['prep_time'] = int(user_input)
    cookbook[name] = recipe
    print(f'"{name}" added to cookbook.')


def delete_recipe():
    name = input("Select a recipe to remove\n")
    if name not in cookbook:
        print(f'"{name}" does not exist.')
        return
    del cookbook[name]
    print(f'"{name}" removed from cookbook.')


def print_recipe_details():
    name = input("Please enter a recipe name to get its details:\n")
    if name not in cookbook:
        print(f'{name} does not exist.')
        return
    print(f'Recipe for {Style.BRIGHT}{name}{Style.RESET_ALL}:')
    print(f'\t• Ingredients list: {cookbook[name]["ingredients"]}')
    print(f'\t• To be eaten for {cookbook[name]["meal"]}.')
    print(
        f'\t• Takes {cookbook[name]["prep_time"]} minute'
        f'{"s" if cookbook[name]["prep_time"] > 1 else ""} of cooking.\n'
    )


def print_all_recipes():
    print(Style.BRIGHT + "Available recipes :" + Style.RESET_ALL)
    for el in cookbook.keys():
        print(f'\t• {el}')
    print()


def is_valid_menu_input(user_input: str, options_count: int) -> int:
    if user_input.isdigit():
        nb = int(user_input)
        if nb > 0 and nb <= options_count:
            return nb
    return 0


def menu_prompt(options_count: int = 0):
    user_input = ''
    menu_msg = f'''List of available option:
        1: Add a recipe
        2: Delete a recipe
        3: Print a recipe
        4: Print the cookbook
        5: Quit
        '''

    print(menu_msg)
    while user_input != 5:
        user_input = is_valid_menu_input(
                        input("\nPlease select an option:\n"), options_count
        )
        while user_input == 0:
            clear_screen()
            print(
                f'{Fore.RED}Sorry, this option does not exist.'
                f'{Style.RESET_ALL}'
            )
            print(menu_msg)
            user_input = is_valid_menu_input(
                        input("\nPlease select an option:\n"), options_count
            )
        if user_input == 1:
            clear_screen()
            add_recipe()
        elif user_input == 2:
            clear_screen()
            delete_recipe()
        elif user_input == 3:
            clear_screen()
            print_recipe_details()
        elif user_input == 4:
            clear_screen()
            print_all_recipes()
        elif user_input == 5:
            print(Style.BRIGHT + "Cookbook closed. Goodbye !")


def main():
    print(Style.BRIGHT + "Welcome to the Python Cookbook !" + Style.RESET_ALL)
    menu_prompt(5)


if __name__ == "__main__":
    main()
