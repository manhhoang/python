'''
Find the pair in 2 arrays if sum of them equal a number X

Input:
a1 = {1, 2, 5}
a2 = {2, 4, 7}
X = 3

Output:
{0, 0} because 1 + 2 = 3

Run Pytest: pytest Pairs.py
'''
def solution(a, b, x):
    ans = []
    a.sort()
    b.sort()
    i = 0
    j = len(b) - 1
    while i < len(a):
        while a[i] + b[j] > x and j > 0:
            j -= 1
        if a[i] + b[j] == x:
            ans.append(i)
            ans.append(j)
            break
        i += 1
    return ans


print(solution([1, 2, 5], [2, 4, 7], 3))


def test1():
    assert solution([1, 2, 5], [2, 4, 7], 3) == [0, 0]


def test2():
    assert solution([1, 4, 6], [2, 4, 7], 5) == [0, 1]
