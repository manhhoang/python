s1 = "afb 123 345"
print(s1[0])
print('\n')


print(s1[:s1.index(" ")])
print('\n')


print(s1[s1.index(" ") + 1:])
print('\n')


s = 'hi'
print(ord(s[0]))
print([ord(c) for c in s])
print('\n')


L = [104, 101, 108, 108, 111, 44, 32, 119, 111, 114, 108, 100]
print(''.join(chr(i) for i in L))
print('\n')


print(' '.join(['1', '2']))

