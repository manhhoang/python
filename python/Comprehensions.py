a_list = [1, '4', 9, 'a', 0, 4]
squared_ints = [e**2 for e in a_list if type(e) is int]
print(squared_ints)
print('\n')


print({s for s in [1, 2, 1, 0] if s > 0})
print('\n')


dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
double_dict1 = {k: v*2 for (k, v) in dict1.items()}
print(double_dict1)
print('\n')


gen = (i**2 for i in range(100))
print(gen)
print((("apple" if i < 3 else "pie") for i in range(6)))


example_gen = (i/2 for i in [0, 9, 21, 32])
print(example_gen)
for item in example_gen:
    print(item)