class Evaluator():
    @staticmethod
    def zip_evaluate(coefs: list[float] = (), words: list[str] = ()):
        if (not isinstance(coefs, list)
                and not isinstance(words, list)):
            raise TypeError(f"coefs is a list of float,"
                            f"words is a list of string")
        if len(coefs) != len(words):
            return -1
        if not all(isinstance(val, float) for val in coefs):
            raise TypeError("coefs is a list of float")
        if not all(isinstance(val, str) for val in words):
            raise TypeError("words is a list of string")
        return sum(num * len(word) for num, word in zip(coefs, words))

    def enumerate_evaluate(coefs: list[float] = (), words: list[str] = ()):
        if (not isinstance(coefs, list)
                and not isinstance(words, list)):
            raise TypeError(f"coefs is a list of float,"
                            f"words is a list of string")
        if len(coefs) != len(words):
            return -1
        if not all(isinstance(val, float) for val in coefs):
            raise TypeError("coefs is a list of float")
        if not all(isinstance(val, str) for val in words):
            raise TypeError("words is a list of string")
        return sum(float(num) * len(word) for num, word in enumerate(words))


if __name__ == "__main__":
    print(Evaluator.zip_evaluate)
    print(Evaluator.enumerate_evaluate)
    print(Evaluator().zip_evaluate)
    print(Evaluator().enumerate_evaluate)

    print("\nStart real tests")
    words = ["Le", "Lorem", "Ipsum", "est", "simple"]
    coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
    print(Evaluator.zip_evaluate(coefs, words))
    print(Evaluator.enumerate_evaluate(coefs, words))

    words = ["Le", "Lorem", "Ipsum", "n’", "est", "pas", "simple"]
    coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
    print(Evaluator.zip_evaluate(coefs, words))
    print(Evaluator.enumerate_evaluate(coefs, words))
