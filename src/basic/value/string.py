def demo():
    S = "Hello, World!"
    print(S)

    S = """String literals can
    span multiple lines."""
    print(S)

    # an integer to a string
    S = str(42)
    print(S)
    # Prints '42'

    # a complex number to a string
    S = str(3 + 4j)
    print(S)
    # Prints '(3+4j)

    # a list to a string
    S = str([1, 1])
    print(S)
    # Prints '[1, 1]'

    # Indexing
    S = "ABCDEFGHI"
    print(S[0])  # Prints A
    print(S[4])  # Prints E

    # Negative Indexing
    S = "ABCDEFGHI"
    print(S[-1])  # Prints I
    print(S[-6])  # Prints D

    S = "ABCDEFGHI"
    print(S[2:5])  # Prints CDE
    print(S[5:-1])  # Prints FGH
    print(S[1:6:2])  # Prints BDF

    S = "Hello, world!"
    new_S = "J" + S[1:]
    print(new_S)

    # Join the list of substrings
    L = ["red", "green", "blue", "yellow"]
    S = ",".join(L)
    print(S)

    # Case conversion
    S = "Hello, World!"
    print(S.lower())
    # Prints hello, world!

    S = "Hello, World!"
    print(S.upper())
    # Prints HELLO, WORLD!

    S = "Hello, World!"
    print(S.capitalize())
    # Prints Hello, world!

    S = "Hello, World!"
    print(S.swapcase())
    # Prints hELLO, wORLD!

    S = "hello, world!"
    print(S.title())
    # Prints Hello, World!

if __name__ == "__main__":
    demo()
