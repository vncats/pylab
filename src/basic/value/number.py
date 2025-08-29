def main():
    # Following numbers are integers
    print("Integer:", 10)
    print("Big integer:", 123456789)
    big_int = 99999999999999999999999999999999999999999999999999999999999999999999999999999999
    print("Very big integer:", big_int)

    # Integers in binary, octal and hexadecimal formats
    print("Integer value of 0b10111011:", 0b10111011)  # binary
    print("Integer value of 0o10:", 0o10)  # binary
    print("Integer value of 0o10:", 0xFF)  # hex

    # Binary is subtype of integer
    print(True)
    print(False)

    # Floating Point
    print(10.1)
    print(1.123456)

    # Scientific notation
    print(42e3)
    print(4.2e-3)

if __name__ == '__main__':
    main()
