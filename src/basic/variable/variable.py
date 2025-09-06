def demo():
    # Constant
    # There is no "constant" in Python. So use a convention to indicate that
    MAX_CONN = 100
    print(MAX_CONN)

    # Multiple return values
    def demo_return():
        return 1, 2, 3

    a, b, c = demo_return()
    print(a, b, c)


if __name__ == "__main__":
    demo()
