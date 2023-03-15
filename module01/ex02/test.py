import unittest
from vector import Vector


class TestVector(unittest.TestCase):
    def test_init_list_row(self):
        with self.assertRaises(TypeError):
            Vector()
        with self.assertRaises(ValueError):
            Vector([])
        with self.assertRaises(TypeError):
            Vector(["se"])
        with self.assertRaises(TypeError):
            Vector([[23]])
        with self.assertRaises(TypeError):
            Vector([[1.0, "sd"]])
        with self.assertRaises(TypeError):
            Vector([[1.0, 2.0, 23]])
        vect = Vector([[0.0, 1.0, 2.0, 3.0]])
        self.assertEqual(vect.shape, (1, 4))
        self.assertEqual(vect.values, [[0.0, 1.0, 2.0, 3.0]])

    def test_init_list_col(self):
        with self.assertRaises(TypeError):
            Vector([1.0], "sd")
        with self.assertRaises(TypeError):
            Vector([[1.0], "sd"])
        with self.assertRaises(TypeError):
            Vector([[1.0], ["sd"]])
        with self.assertRaises(ValueError):
            Vector([[1.0], []])
        with self.assertRaises(ValueError):
            Vector([[1.0], [1.0, 0.0]])
        vect = Vector([[0.0], [1.0], [2.0], [3.0]])
        self.assertEqual(vect.shape, (4, 1))
        self.assertEqual(vect.values, [[0.0], [1.0], [2.0], [3.0]])

    def test_init_int(self):
        with self.assertRaises(TypeError):
            Vector("sd")
        with self.assertRaises(ValueError):
            Vector(-12)
        with self.assertRaises(ValueError):
            Vector(0)
        with self.assertRaises(TypeError):
            Vector(2.3)
        vect = Vector(3)
        self.assertEqual(vect.values, [[0.0], [1.0], [2.0]])
        self.assertEqual(vect.shape, (3, 1))

    def test_init_tuple(self):
        with self.assertRaises(ValueError):
            Vector(())
        # don't raise because if len((2)) == 1; (2) -> 2
        # with self.assertRaises(ValueError):
        #     Vector((1))
        with self.assertRaises(ValueError):
            Vector((1, 2, 3))
        with self.assertRaises(TypeError):
            Vector(("sdf", 234))
        with self.assertRaises(ValueError):
            Vector((5, -34))
        vect = Vector((2, 6))
        self.assertEqual(vect.values, [[2.0], [3.0], [4.0], [5.0]])
        self.assertEqual(vect.shape, (4, 1))

    def test_T(self):
        vect = Vector([[0.0], [1.0], [2.0], [3.0]])
        transposed = vect.T()
        self.assertEqual(vect.shape, (4, 1))
        self.assertEqual(transposed.shape, (1, 4))
        self.assertEqual(transposed.values, [[0.0, 1.0, 2.0, 3.0]])
        self.assertNotEqual(vect.T().shape, (4, 1))
        vect = transposed.T()
        self.assertEqual(vect.shape, (4, 1))
        self.assertEqual(vect.values, [[0.0], [1.0], [2.0], [3.0]])

    def test_add(self):
        with self.assertRaises(TypeError):
            vect = Vector([[0.0]]) + 5
        with self.assertRaises(TypeError):
            vect = Vector([[0.0]]) + "sd"
        with self.assertRaises(ValueError):
            vect = Vector([[0.0]]) + Vector([[0.0], [0.0]])
        vect1 = Vector([[0.0], [1.0], [2.0], [3.0]])
        vect2 = Vector([[3.0], [2.0], [1.0], [0.0]])
        vect = vect1 + vect2
        self.assertEqual(vect.values,
                         Vector([[3.0], [3.0], [3.0], [3.0]]).values)
        vect1 = Vector([[0.0, 1.0, 2.0, 3.0]])
        vect2 = Vector([[0.0, 1.0, 2.0, 3.0]])
        vect = vect1 + vect2
        self.assertEqual(vect.values,
                         Vector([[0.0, 2.0, 4.0, 6.0]]).values)
        vect1 = Vector([[-9.0]])
        vect2 = Vector([[18.0]])
        vect = vect1 + vect2
        self.assertEqual(vect.values, Vector([[9.0]]).values)

    def test_sub(self):
        with self.assertRaises(TypeError):
            vect = Vector([[0.0]]) - 5
        with self.assertRaises(TypeError):
            vect = 5.0 - Vector([[0.0]])
        with self.assertRaises(TypeError):
            vect = Vector([[0.0]]) - "sd"
        with self.assertRaises(ValueError):
            vect = Vector([[0.0]]) - Vector([[0.0], [0.0]])
        vect1 = Vector([[0.0], [1.0], [2.0], [3.0]])
        vect2 = Vector([[3.0], [2.0], [1.0], [0.0]])
        vect = vect1 - vect2
        self.assertEqual(vect.values,
                         Vector([[-3.0], [-1.0], [1.0], [3.0]]).values)
        vect1 = Vector([[0.0, 1.0, 2.0, 3.0]])
        vect2 = Vector([[0.0, 1.0, 2.0, 3.0]])
        vect = vect1 - vect2
        self.assertEqual(vect.values,
                         Vector([[0.0, 0.0, 0.0, 0.0]]).values)
        vect1 = Vector([[-9.0]])
        vect2 = Vector([[18.0]])
        vect = vect1 - vect2
        self.assertEqual(vect.values, Vector([[-27.0]]).values)
        vect = vect2 - vect1
        self.assertEqual(vect.values, Vector([[27.0]]).values)

    def test_divide(self):
        with self.assertRaises(TypeError):
            vect = Vector([[0.0]]) / Vector([1.0])
        with self.assertRaises(TypeError):
            vect = Vector([[0.0]]) / "sd"
        with self.assertRaises(TypeError):
            vect = Vector([[0.0]]) / 5
        with self.assertRaises(ZeroDivisionError):
            vect = Vector([[5.0]]) / 0.0
        vect1 = Vector([[6.0], [2.0], [12.0]])
        vect = vect1 / 2.0
        self.assertEqual(vect.values, Vector([[3.0], [1.0], [6.0]]).values)
        vect1 = Vector([[6.0, 2.0, 12.0]])
        vect = vect1 / 2.0
        self.assertEqual(vect.values, Vector([[3.0, 1.0, 6.0]]).values)
        with self.assertRaises(NotImplementedError):
            vect = 2.0 / vect1

    def test_mul(self):
        with self.assertRaises(TypeError):
            vect = Vector([[0.0]]) * Vector([1.0])
        with self.assertRaises(TypeError):
            vect = Vector([[0.0]]) * "sd"
        with self.assertRaises(TypeError):
            vect = Vector([[0.0]]) * 5
        vect1 = Vector([[6.0], [2.0], [12.0]])
        vect = vect1 * 2.0
        self.assertEqual(vect.values, Vector([[12.0], [4.0], [24.0]]).values)
        vect1 = Vector([[6.0, 2.0, 12.0]])
        vect = vect1 * 2.0
        self.assertEqual(vect.values, Vector([[12.0, 4.0, 24.0]]).values)
        vect = 2.0 * vect1
        self.assertEqual(vect.values, Vector([[12.0, 4.0, 24.0]]).values)

    def test_dot(self):
        with self.assertRaises(TypeError):
            vect = Vector([[0.0]]).dot(5)
        with self.assertRaises(TypeError):
            vect = Vector([[0.0]]).dot("sd")
        with self.assertRaises(ValueError):
            vect = Vector([[0.0]]).dot(Vector([[0.0], [0.0]]))
        with self.assertRaises(ValueError):
            vect = Vector([[0.0, 1.0]]).dot(Vector([[0.0]]))
        with self.assertRaises(ValueError):
            vect = Vector([[0.0], [1.0]]).dot(Vector([[0.0]]))
        v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
        v2 = Vector([[2.0], [1.5], [2.25], [4.0]])
        self.assertEqual(v1.dot(v2), 18.0)
        v3 = Vector([[1.0, 3.0]])
        v4 = Vector([[2.0, 4.0]])
        self.assertEqual(v3.dot(v4), 14.0)

    def test_str_repr(self):
        v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
        self.assertEqual(str(v1), "[[0.0], [1.0], [2.0], [3.0]]")
        self.assertEqual(repr(v1), "[[0.0], [1.0], [2.0], [3.0]]")

if __name__ == '__main__':
    unittest.main()
