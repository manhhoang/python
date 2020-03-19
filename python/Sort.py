a = [3, 6, 8, 2, 78, 1, 23, 45, 9]
a.sort()
print(a)

a.sort(reverse=True)
print(a)


x = {1: 'f', 3: 'c', 4: 'a', 2: 'b', 0: 'i'}
y = {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}
print(y)


x = {1: 'f', 3: 'c', 4: 'a', 2: 'b', 0: 'i'}
y = {k: v for k, v in sorted(x.items(), key=lambda item: item[0])}
print(y)
