def demo_file():
    # write to file
    f = open("test.txt", "w")
    f.write("hello world")
    f.close()

    # read a file
    f = open("test.txt", "r")
    print(f.read())

if __name__ == '__main__':
    demo_file()