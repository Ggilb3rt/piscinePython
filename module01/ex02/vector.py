class Vector():
    """A vector
        column vector with m elements (is a m * 1 matrix)
        it's a single column of m entries :
                 _  _
                | x1 |
                | x2 |
            x = | .. |
                | .. |
                |_xm_|

        row vector with n elements (is a 1 * n matrix)
        it's a single row of n entries :

            y = [y1 y2 .. .. yn]
    """

    def __init__(self, arg) -> None:
        """Vector initialize allowed:
            a list of a list of floats: Vector([[0.0, 1.0, 2.0, 3.0]])
            a list of lists of single float:
                                Vector([[0.0], [1.0], [2.0], [3.0]])
            a size: Vector(3)
            a range (from tuple of len 2): Vector((10,16))
        """
        if isinstance(arg, list):
            if not all(isinstance(el, list) for el in arg):
                raise TypeError(self.__init__.__doc__)
            for el in arg:
                if not all(isinstance(val, float) for val in el):
                    raise TypeError("Only floats in list(s)")
            self.values = arg
            if len(arg) == 0:
                raise ValueError("The list of values can't be empty")
            elif len(arg) == 1:
                # is row
                self.shape = (1, len(arg[0]))
            else:
                # is column
                for el in arg:
                    if len(el) != 1:
                        raise ValueError("Each column must has one value")
                self.shape = (len(arg), 1)

        elif isinstance(arg, int):
            if arg <= 0:
                raise ValueError("Vector must have positive dimensions")
            self.values = [[float(el)] for el in range(arg)]
            self.shape = (arg, 1)

        elif isinstance(arg, tuple):
            if len(arg) != 2:
                raise ValueError("Range must be 2 integers")
            if not all(isinstance(val, int) for val in arg):
                raise TypeError("Range must be integers")
            if arg[0] > arg[1]:
                raise ValueError("Vector((a, b)), must be a < b")
            self.values = [[float(el)] for el in range(arg[0], arg[1])]
            self.shape = (len(self.values), 1)

        else:
            raise TypeError(self.__init__.__doc__)

    def dot(self, vector):
        """Produce a dot product between two vectors of same shape"""
        # check if vector isinstance of Vector
        # check if same shape

    def T(self):
        """Returns the transpose vector
        (i.e. a column vector into a row vector,
        or a row vector into a column vector).
        """
        if self.shape[0] == 1:
            # row change to column ie change [[1,2,3]] -> [[1],[2],[3]]
            return Vector([[x] for x in self.values[0]])
        else:
            # column change to row ie change [[1],[2],[3]] -> [[1,2,3]]
            return Vector([[x[0] for x in self.values]])

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Addition only with Vector of same shape")
        if self.shape != other.shape:
            raise ValueError("Addition only with Vector of same shape")
        if self.shape[0] == 1:
            # [[1,2,3]]
            return [[self.values[0][i] + other.values[0][i] for i in range(self.shape[1])]]
        else:
            # [[1],[2],[3]]
            return [[self.values[i][0] + other.values[i][0]] for i in range(self.shape[0])]
