s1 = "afb 123 345"
s2 = "adf adf adsfadsf"
s3 = "jsg bfs ads"
s4 = "aty bfs ads"

dic = {}

key1 = s1[:s1.index(" ")]
val1 = s1[s1.index(" ") + 1:]
if not val1[0].isdigit():
    dic[key1] = val1

key2 = s2[:s2.index(" ")]
val2 = s2[s2.index(" ") + 1:]
if not val2[0].isdigit():
    dic[key2] = val2

key3 = s3[:s3.index(" ")]
val3 = s3[s3.index(" ") + 1:]
if not val3[0].isdigit():
    dic[key3] = val3

key4 = s4[:s4.index(" ")]
val4 = s4[s4.index(" ") + 1:]
if not val4[0].isdigit():
    dic[key4] = val4

print(dic)
print('\n')


sortedList = sorted(dic.items(), key=lambda x: (x[1], x[0]))
print(sortedList)
print('\n')


result = []
for key, value in sortedList:
    result.append(key + " " + value)
print(result)
print('\n')


y = {100: 1, 90: 4, 99: 3, 92: 1, 101: 1}
ans = sorted(y.items(), key=lambda x: (x[1], x[0]), reverse=True)

print(ans)

# [(90, 4), (99, 3), (101, 1), (100, 1), (92, 1)]