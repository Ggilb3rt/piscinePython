import unittest

class Account(object):
    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)
        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, 'value'):
            self.value = 0
        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")

    def transfer(self, amount):
        self.value += amount


class Bank(object):
    """The bank"""
    def __init__(self):
        self.accounts = []

    def __isCorrupted(self, account: Account) -> bool:
        """Check if the account is corrupted
        Account is corrupted if :
            • an even number of attributes
            • an attribute starting with b
            • no attribute starting with
                zip,
                addr
            • no attribute 
                name,
                id,
                value
            • name not being a string
            • id not being an int
            • value not being an
                int,
                float
        """
        attrs = dir(account)
        # print(len(attrs))
        # print(attrs)
        if (len(attrs) % 2 == 0 or
            any(el[0] == 'b' for el in attrs) or
            not any(el.startswith("zip") for el in attrs) or
            not any(el.startswith("addr") for el in attrs) or
            not hasattr(account, 'name') or
            not hasattr(account, 'id') or
            not hasattr(account, 'value') or
            not isinstance(account.name, str) or
            not isinstance(account.id, int) or
            ((not isinstance(account.value, int) and
                 not isinstance(account.value, float)))
            ):
            return True
        return False

    def add(self, new_account: Account) -> bool:
        """ Add new_account in the Bank
        @new_account: Account() new account to append
        @return True if success, False if an error occured
        """
        if not isinstance(new_account, Account):
            return False
            # raise TypeError(self.add.__doc__)
        if self.__isCorrupted(new_account):
            return False
            # raise ValueError("The account is corrupted")
        if any(in_account.name == new_account.name for in_account in self.accounts):
            return False
            # raise ValueError("One account has same name")
        self.accounts.append(new_account)
        return True

    def transfer(self, origin: str, dest: str, amount: float) -> bool:
        """" Perform the fund transfer
        @origin: str(name) of the first account
        @dest: str(name) of the destination account
        @amount: float(amount) amount to transfer
        @return True if success, False if an error occured
        """
        if (not isinstance(origin, str) or
            not isinstance(dest, str) or
            not isinstance(amount, float) or
            amount < 0 or
            in_account.value < amount for in_account in self.accounts if in_account.name == origin
            ):
            return False
        # j'aimerai mettre ca (lignes 91) dans la condition mais c'est quand meme sale (et pas sur que ca marche),
        # il vaut mieux trouver origin et dest dans self.accounts puis tester si ils existent et sont valides
        # mais en dessous je pense pas que ca marche, il faudrait que je pass une ref
        valid_or = [in_account.reference for in_account in self.accounts if in_account.name == origin]
        valid_dest = [in_account.reference for in_account in self.accounts if in_account.name == dest]

    def fix_account(self, name):
        """ fix account associated to name if corrupted
        @name: str(name) of the account
        @return True if success, False if an error occured
        """
        # ... Your code ...


class TestBank(unittest.TestCase):
    def test___isCorrupted(self):
        b = Bank()
        valid = Account('James Watson',
            zip='NW1 6XE',
            addr='221B Baker street',
            value=25000.0,)
        self.assertEqual(b._Bank__isCorrupted(valid), False)
        even = Account('James Watson',
            lol='ert',
            zip='NW1 6XE',
            addr='221B Baker street',
            value=25000.0,)
        self.assertEqual(b._Bank__isCorrupted(even), True)
        has_b = Account('James Watson',
            bab='ert',
            lol='ert',
            zip='NW1 6XE',
            addr='221B Baker street',
            value=25000.0,)
        self.assertEqual(b._Bank__isCorrupted(has_b), True)
        no_zip = Account('James Watson',
            pip='NW1 6XE',
            addr='221B Baker street',
            value=25000.0,)
        self.assertEqual(b._Bank__isCorrupted(no_zip), True)
        no_addr = Account('James Watson',
            zip='NW1 6XE',
            lddr='221B Baker street',
            value=25000.0,)
        self.assertEqual(b._Bank__isCorrupted(no_addr), True)
        no_name = Account('James Watson',
            zip='NW1 6XE',
            addr='221B Baker street',
            value=25000.0,
            replace_name='name2')
        del no_name.name
        self.assertEqual(b._Bank__isCorrupted(no_name), True)
        no_id = Account('James Watson',
            zip='NW1 6XE',
            addr='221B Baker street',
            value=25000.0,
            replace_id=23)
        del no_id.id
        self.assertEqual(b._Bank__isCorrupted(no_id), True)
        no_value = Account('James Watson',
            zip='NW1 6XE',
            addr='221B Baker street',
            not_value=25000.0,)
        del no_value.value
        self.assertEqual(b._Bank__isCorrupted(no_value), True)
        name_not_str = Account('James Watson',
            zip='NW1 6XE',
            addr='221B Baker street',
            value=25000.0,)
        name_not_str.name = 1
        self.assertEqual(b._Bank__isCorrupted(name_not_str), True)
        id_not_int = Account('James Watson',
            zip='NW1 6XE',
            addr='221B Baker street',
            value=25000.0,)
        id_not_int.id = "coucou"
        self.assertEqual(b._Bank__isCorrupted(id_not_int), True)
        value_not_int_float = Account('James Watson',
            zip='NW1 6XE',
            addr='221B Baker street',
            value=25000.0,)
        value_not_int_float.value = "coucou"
        self.assertEqual(b._Bank__isCorrupted(value_not_int_float), True)
        value_is_int = Account('James Watson',
            zip='NW1 6XE',
            addr='221B Baker street',
            value=25000,)
        self.assertEqual(b._Bank__isCorrupted(value_is_int), False)

    def test_Bank_add(self):
        b = Bank()
        a1 = Account('James Watson',
            zip='NW1 6XE',
            addr='221B Baker street',
            value=25000,)
        a2 = Account('James Web',
            zip='NW1 6XE',
            addr='221B Baker street',
            value=25000,)
        self.assertEqual(b.add(a1), True)
        self.assertEqual(b.add(a2), True)
        self.assertEqual(b.add(a2), False)
        self.assertEqual(b.add(a1), False)



if __name__ == "__main__":
    unittest.main()

