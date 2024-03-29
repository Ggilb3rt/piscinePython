class GotCharacter():
    """A game of throne character"""

    def __init__(self, first_name: str = None, is_alive: bool = True) -> None:
        if not isinstance(first_name, str):
            raise TypeError("First name must be a string")
        if not isinstance(is_alive, bool):
            raise TypeError("is_alive must be True of False")
        self.first_name = first_name
        self.is_alive = is_alive


class Stark(GotCharacter):
    """A class representing the Stark family.
    Or when bad things happen to good people."""

    def __init__(self, first_name: str = None, is_alive: bool = True) -> None:
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False


class Lannister(GotCharacter):
    """A class representing the Lannister family. They pay their debts."""

    def __init__(self, first_name: str = None, is_alive: bool = True) -> None:
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Lannister"
        self.house_words = "Hear Me Roar"

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False
