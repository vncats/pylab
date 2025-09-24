def demo_dataframe():
    import pandas as pd

    data = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']
    }

    df = pd.DataFrame(data)

    # get first value of Age column
    first_age = df['Age'][0]
    print(f"First age: {first_age}")


    df2 = pd.DataFrame()
    simple_dict = {'a': 1, 'b': 2, 'c': 3}
    for key, value in simple_dict.items():
        df2 = pd.concat([df2, pd.DataFrame({'key': [key], 'value': [value]})], ignore_index=True)
    print(df2)


if __name__ == '__main__':
    demo_dataframe()