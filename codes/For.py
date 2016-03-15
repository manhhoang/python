for i in range(5):
    print(i, end=",")

print('\n')

for i in range(1,5):
    print(i, end=' ')

print('\n')

for animal in ["dog", "cat", "mouse"]:
    # You can use format() to interpolate formatted strings
    print("{} is a mammal".format(animal))