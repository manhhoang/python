def double_numbers(iterable):
    for i in iterable:
        yield i + i


print(double_numbers([1, 2]))
