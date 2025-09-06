def hello():
    print("Hello, World!")

    def title(name, job):
        print(name, "is a", job)

    # Positional arguments
    title("John", "Developer")

    # Keyword arguments
    title(name="John", job="Developer")

    # Set default value 'developer' to a 'job' parameter
    def title_with_default(name, job="Driver"):
        print(name, "is a", job)

    title_with_default("John")

    # Variadic arguments
    def title_variadic(*names):
        for name in names:
            print(name)

    title_variadic("John", "Jane", "Jack")

    # Variadic keyword arguments
    def title_variadic_keyword(**args):
        print(args)

    title_variadic_keyword(a="hello", b={"x": 1, "y": 2}, c=[1, 2, 3])

    # Use / argument to indicate required positional arguments
    def title_with_slash(name, age, /, job):
        print(name, "is a", job, "and", age, "years old")

    title_with_slash("John", 25, job="Developer")

    # Use * argument to indicate keyword-only parameters
    def title_with_star(name, *, job):
        print(name, "is a", job)

    title_with_star("John", job="Developer")

if __name__ == "__main__":
    hello()
