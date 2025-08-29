def demo():
    # A list of integers
    L = [1, 2, 3]
    print(L)

    # A list of strings
    L = ["red", "green", "blue"]
    print(L)

    # A list of mixed datatypes
    L = [1, "abc", 1.23, (3 + 4j), True]
    print(L)

    # Convert a string to a list
    L = list("abc")
    print(L)

    # Convert a tuple to a list
    L = list((1, 2, 3))
    print(L)

    # Basic nested list
    L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(L)

    # Nested list with different lengths of inner lists
    L = [[1, 2], [3, 4, 5], [6, 7, 8, 9]]
    print(L)

    # Nested list with mixed data types
    L = [["Alice", 30], ["Bob", 25], ["Charlie", 35]]
    print(L)

    # Deeper nested lists
    L = ['a', 'b', ['cc', 'dd', ['eee', 'fff']], 'g', 'h']
    print(L)
    print(L[2])  # Output: ['cc', 'dd', ['eee', 'fff']]
    print(L[2][2])  # Output: ['eee', 'fff']
    print(L[2][2][0])  # Output: eee

    # List slicing
    L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    print(L[:3])
    print(L[6:])
    print(L[2:7])
    print(L[-7:-2])

    # Slicing with a Step
    print(L[2:7:2])
    print(L[6:1:-2])

    # Reversing a List
    print(L[::-1])

    # Modify multiple list items
    L = ['a', 'b', 'c', 'd', 'e']
    L[1:4] = [1, 2, 3]
    print(L)

    # Replace multiple elements in place of a single element
    L = ['a', 'b', 'c', 'd', 'e']
    L[1:2] = [1, 2, 3]
    print(L)
    # Output: ['a', 1, 2, 3, 'c', 'd', 'e']

    pass


if __name__ == "__main__":
    demo()
