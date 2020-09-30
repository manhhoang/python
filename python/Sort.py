# Basic sort
a = [3, 6, 8, 2, 78, 1, 23, 45, 9]
a.sort()
print(a)
print('\n')


a.sort(reverse=True)
print(a)
print('\n')


# Sort dictionary by value
x = {1: 'f', 3: 'c', 4: 'a', 2: 'b', 0: 'i'}
y = {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}
print(y)
print('\n')


# Sort dictionary by key
x = {1: 'f', 3: 'c', 4: 'a', 2: 'b', 0: 'i'}
y = {k: v for k, v in sorted(x.items(), key=lambda item: item[0])}
print(y)
print('\n')


# Sort class
class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
    def __repr__(self):
        return repr((self.name, self.grade, self.age))
student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]
print(sorted(student_objects, key=lambda student: student.age, reverse=True))
print('\n')


# Sort tuples
student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
    ('anna', 'C', 10),
]
print(sorted(student_tuples, key=lambda student: (student[2], student[0])))
print('\n')


# Sort dictionary
orders = {
    'cappuccino': 54,
    'latte': 56,
    'espresso': 72,
    'americano': 48,
    'cortado': 41
}
sort_orders = sorted(orders.items(), key=lambda x: x[1], reverse=True)
for i in sort_orders:
    print(i[0], i[1])
print('\n')


# Sort nested dictionary
keys = {
  'KEY1': {
    'name': 'google',
    'date': 20100701,
    'downloads': 0
  },
  'KEY2': {
    'name': 'chrome',
    'date': 20071010,
    'downloads': 0
  },
  'KEY3': {
    'name': 'python',
    'date': 20100710,
    'downloads': 100
  }
}
sorted_key = sorted(keys, key=lambda x: (keys[x]['downloads'], keys[x]['date']))
for a in sorted_key:
    print(f"'{a}'" + ':' + str(keys[a]))