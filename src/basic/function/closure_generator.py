def counter_closure(max_value: int):
    i = 0

    def counter():
        nonlocal i, max_value
        if i == max_value:
            raise StopIteration
        i += 1
        return i

    return counter


def demo_closure():
    counter = counter_closure(2)
    print(counter())
    print(counter())
    # print(counter()) # will raise StopIteration


def counter_generator(max_value: int):
    i = 1
    while i <= max_value:
        yield i
        i += 1


def demo_generator():
    counter = counter_generator(2)
    print(next(counter))
    print(next(counter))
    # print(next(counter)) # will raise StopIteration


if __name__ == "__main__":
    demo_generator()
    demo_closure()
