import unittest


def ft_map(function_to_apply, iterable):
    """Map the function to all elements of the iterable.
    Args:
        function_to_apply: a function taking an iterable.
        iterable: an iterable object (list, tuple, iterator).
    Return:
        An iterable.
        None if the iterable can not be used by the function.
    """
    if not callable(function_to_apply):
        raise TypeError(f'{type(function_to_apply)} object is not callable')
    try:
        _ = (e for e in iterable)
    except TypeError:
        return iterable
    for it in iterable:
        yield function_to_apply(it)


class Testmap(unittest.TestCase):
    def test_error(self):
        with self.assertRaises(TypeError):
            l = ft_map(23, [el for el in range(2)])
            for el in l:
                print(el)
        with self.assertRaises(TypeError):
            l = ft_map(lambda x:x, 23)
            for el in l:
                print(el)
        with self.assertRaises(TypeError):
            l = ft_map(lambda x:x % 2 == 0, "123")
            for el in l:
                print(el)
        with self.assertRaises(TypeError):
            rl = map(23, [el for el in range(2)])
            for el in rl:
                print(el)
        with self.assertRaises(TypeError):
            rl = map(lambda x:x, 23)
            for el in rl:
                print(el)
        with self.assertRaises(TypeError):
            rl = map(lambda x:x % 2 == 0, "123")
            for el in rl:
                print(el)
    
    def test_work(self):
        l = ft_map(lambda x:int(x), "0123")
        rl = map(lambda x:int(x), "0123")
        for el in rl:
            self.assertEqual(el, l[el])
        l = ft_map(lambda x:x % 2 == 0, range(5))
        rl = map(lambda x:x % 2 == 0, range(5))
        i = 0
        for el in rl:
            self.assertEqual(el, l[i])
            i += 1

if __name__ == "__main__":
    unittest.main()
