import time


def get_local_time():
    """Retrieve the local time."""
    return time.localtime()


def print_local_time():
    """Print the local time."""
    current_time = get_local_time()
    print(current_time)  # Replace this with formatted output if needed.


if __name__ == "__main__":
    print_local_time()