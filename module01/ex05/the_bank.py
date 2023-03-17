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
        # if self.__isCorrupted(new_account):
        #     return False
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
            amount < 0
            ):
            return False
        valid_or = [in_account for in_account in self.accounts if in_account.name == origin]
        valid_dest = [in_account for in_account in self.accounts if in_account.name == dest]
        if len(valid_dest) != 1 or len(valid_or) != 1:
            return False
        valid_dest = valid_dest[0]
        valid_or = valid_or[0]
        if valid_or.value < amount:
            return False
        if self.__isCorrupted(valid_or) or self.__isCorrupted(valid_dest):
            return False
        valid_or.value = valid_or.value - amount
        valid_dest.value = valid_dest.value + amount
        return True

    def fix_account(self, name: str) -> bool:
        """ fix account associated to name if corrupted
        @name: str(name) of the account
        @return True if success, False if an error occured
        """
        if not isinstance(name, str):
            return False
        account = [in_account for in_account in self.accounts if in_account.name == name]
        if len(account) != 1:
            return False
        account = account[0]
        if not self.__isCorrupted(account):
            return False
        attrs = dir(account)
        # remove attrs starting with b
        for el in filter(lambda el: el.startswith('b'), attrs):
            delattr(account, el)
        # no attr starting with zip or addr
        finder = list(filter(lambda el: el.startswith('zip'), attrs))
        if len(finder) == 0:
            account.zip = "0000"
        finder = list(filter(lambda el: el.startswith('addr'), attrs))
        if len(finder) == 0:
            account.addr = "0000"
        # no attr id and not int
        if not hasattr(account, "id"):
            setattr(account, "id", Account.ID_COUNT)
            Account.ID_COUNT += 1
        else:
            if not isinstance(account.id, int):
                account.id = Account.ID_COUNT
                Account.ID_COUNT += 1
        # if name is corrupted the method return before
        # no attr value and not int or float
        if not hasattr(account, "value"):
            account.value = 0.0
        else:
            if not isinstance(account.value, int) and not isinstance(account.value, float):
                account.value = 0.0
        # fix even number of attributes with dummy attr
        if len(dir(account)) % 2 == 0:
            account.dont_like_even_nb_of_attr = True
        return True




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

    def test_Bank_transfer(self):
        b = Bank()
        a1 = Account('Watson',
            zip='NW1 6XE',
            addr='221B Baker street',
            value=25000,)
        a2 = Account('Web',
            zip='NW1 6XE',
            addr='221B Baker street',
            value=25000,)
        b.add(a1)
        b.add(a2)
        self.assertEqual(b.transfer(a1.name, a2.name, 20.0), True)
        self.assertEqual(b.accounts[0].value, 24980.0)
        self.assertEqual(b.accounts[1].value, 25020.0)
        b.accounts[0].value = 0
        self.assertEqual(b.transfer(a1.name, a2.name, 20.0), False)
        b.accounts[0].value = 100
        self.assertEqual(b.transfer(a1.name, a2.name, 200.0), False)
        self.assertEqual(b.transfer(a1.name, "Bob", 20.0), False)
        self.assertEqual(b.transfer("Roger", a2.name, 20.0), False)
        self.assertEqual(b.transfer(a1.name, 1, 20.0), False)
        self.assertEqual(b.transfer(1, a2.name, 20.0), False)
        self.assertEqual(b.transfer(a1.name, a2.name, 2), False)
        self.assertEqual(b.transfer(a1.name, a2.name, "20.0"), False)
        self.assertEqual(b.transfer(a1.name, a2.name, -20.0), False)
        b.accounts[0].brioche = True
        self.assertEqual(b.transfer(a1.name, a2.name, 20.0), False)
        self.assertEqual(b.transfer(a2.name, a1.name, 20.0), False)
        delattr(b.accounts[0], "brioche")
        self.assertEqual(b.transfer(a2.name, a1.name, 100.0), True)
        self.assertEqual(b.accounts[0].value, 200.0)
        self.assertEqual(b.accounts[1].value, 24920.0)
        self.assertEqual(b.transfer(a1.name, a1.name, 100.0), True)
        self.assertEqual(b.accounts[0].value, 200.0)
        self.assertEqual(b.accounts[1].value, 24920.0)

    def test_Bank_fix_account(self):
        b = Bank()
        a1 = Account('Watson',
            zip='NW1 6XE',
            addr='221B Baker street',
            value=25000,)
        a2 = Account('Web',
            zip='NW1 6XE',
            addr='221B Baker street',
            value=25000,)
        to_fix = Account("Bad")
        b.add(a1)
        b.add(a2)
        b.add(to_fix)
        self.assertEqual(b.fix_account(42), False)
        self.assertEqual(b.fix_account(a1.name), False)
        b.accounts[0].brioche = True
        self.assertEqual(b.fix_account(a1.name), True)

        self.assertEqual(b.fix_account(a1.name), False)
        self.assertEqual(b.accounts[0].value, 25000)
        delattr(b.accounts[0], "value")
        self.assertEqual(hasattr(b.accounts[0], "value"), False)
        self.assertEqual(b.fix_account(a1.name), True)
        self.assertEqual(b.accounts[0].value, 0.0)
        self.assertEqual(b.accounts[2].name, "Bad")
        self.assertEqual(hasattr(b.accounts[2], "id"), True)
        delattr(b.accounts[2], "id")
        self.assertEqual(hasattr(b.accounts[2], "id"), False)
        self.assertEqual(b.fix_account(to_fix.name), True)
        self.assertEqual(b.accounts[2].value, 0.0)
        self.assertEqual(b.accounts[2].id, 6)
        self.assertEqual(Account("useless").id, 7)
        b.accounts[0].add_dummy_to_be_even = True
        self.assertEqual(b.fix_account(a1.name), True)
        self.assertEqual(hasattr(b.accounts[0], "dont_like_even_nb_of_attr"), True)








if __name__ == "__main__":
    unittest.main()
