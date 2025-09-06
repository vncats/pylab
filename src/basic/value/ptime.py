import time


def demo_time():
    print(time.time())
    print(time.localtime())
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

    # create a time = now + 5 minutes
    print(time.time() + 5 * 60)

    # print unix timestamp integer
    print(int(time.time()))

    # diff time
    x = time.time()
    y = time.time() + 5 * 60
    print(y - x)

    # parse time from string
    print(time.strptime("2023-10-01 12:00:00", "%Y-%m-%d %H:%M:%S"))


if __name__ == "__main__":
    demo_time()
