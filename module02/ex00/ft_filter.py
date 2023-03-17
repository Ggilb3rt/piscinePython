import unittest
from collections.abc import Iterable

def ft_filter(function_to_apply, iterable):
    """Filter the result of function apply to all elements of the iterable.
    Args:
        function_to_apply: a function taking an iterable.
        iterable: an iterable object (list, tuple, iterator).
    Return:
        An iterable.
        None if the iterable can not be used by the function.
    """
    if not callable(function_to_apply):
        raise TypeError(f'{type(function_to_apply)} object is not callable')
    if not isinstance(iterable, Iterable):
        raise TypeError(f'{type(iterable)} object is not iterable')
    for it in iterable:
        if (function_to_apply(it)):
            yield it


class TestFilter(unittest.TestCase):
    def test_error(self):
        with self.assertRaises(TypeError):
            l = ft_filter(23, [el for el in range(2)])
            for el in l:
                print(el)
        with self.assertRaises(TypeError):
            l = ft_filter(lambda x:x, 23)
            for el in l:
                print(el)
        with self.assertRaises(TypeError):
            l = ft_filter(lambda x:x % 2 == 0, "123")
            for el in l:
                print(el)
        with self.assertRaises(TypeError):
            rl = filter(23, [el for el in range(2)])
            for el in rl:
                print(el)
        with self.assertRaises(TypeError):
            rl = filter(lambda x:x, 23)
            for el in rl:
                print(el)
        with self.assertRaises(TypeError):
            rl = filter(lambda x:x % 2 == 0, "123")
            for el in rl:
                print(el)
    
    def test_work(self):
        l = ft_filter(lambda x:x, "0123")
        rl = filter(lambda x:x, "0123")
        rres = [el for el in rl]
        res = [el for el in l]
        self.assertEqual(res, rres)
        l = ft_filter(lambda x:x % 2 == 0, range(5))
        rl = filter(lambda x:x % 2 == 0, range(5))
        rres = [el for el in rl]
        res = [el for el in l]
        self.assertEqual(res, rres)
    
    def test_subject(self):
        x = [1, 2, 3, 4, 5]
        self.assertEqual(list(ft_filter(lambda dum: not (dum % 2), x)), [2, 4])


if __name__ == "__main__":
    print(ft_filter(lambda dum: not (dum % 2), [1, 2, 3, 4, 5]))
    unittest.main()
