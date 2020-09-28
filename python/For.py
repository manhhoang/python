for i in range(5):
    print(i, end=",")
print('\n')


for i in range(1, 5):
    print(i, end=' ')
print('\n')


for animal in ["dog", "cat", "mouse"]:
    print(f"{animal} is a mammal")
print('\n')


a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
for key in a_dict:
    print(key)
print('\n')


for key in a_dict.keys():
    print(key)
print('\n')


for value in a_dict.values():
    print(value)
print('\n')


for item in a_dict.items():
    print(item)
    print(type(item))
print('\n')


for key, value in a_dict.items():
    print(key, '->', value)
print('\n')