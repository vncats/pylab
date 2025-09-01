# set items are immutable type
def demo_set():
    S = {1, 2, "3", 4}
    print(S)

    B = {1, 2, 4, "a"}
    print(B)

    # union
    print(S | B)

    # intersect
    print(S & B)

    # diff
    print(S - B)

    # symmetric diff
    print(S ^ B)


# dict keys are immutable type
def demo_dict():
    D = {
        "a": 1,
        "b": 2,
        "c": {
            "d": 3,
            "e": [
                {"f": 4, "g": 5},
            ],
            (1, 2): 5,
            (2, 1): 6,
            (2, 1): 7,
        },
    }
    print(D)


if __name__ == "__main__":
    demo_dict()
    demo_set()
